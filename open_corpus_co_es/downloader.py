import hashlib
import importlib.resources
import json
import logging
import os
from pathlib import Path
from zipfile import ZipFile, is_zipfile

import gdown
import requests

from .utils import ensure_data_dir

logger = logging.getLogger("corpus_downloader")


def load_catalog():
    resource = importlib.resources.files("open_corpus_co_es").joinpath("catalog.json")
    with resource.open(encoding="utf-8") as source:
        entries = json.load(source)
    catalog = {}
    enabled_map = {}
    for entry in entries:
        name = entry.get("nombre", Path(entry["archivo"]).stem)
        if name in catalog:
            raise ValueError(f"Nombre duplicado en el catálogo: {name}")
        if Path(entry["archivo"]).suffix.lower() != "." + entry["extension"].lower():
            raise ValueError(f"Extensión inconsistente: {name}")
        catalog[name] = entry
        enabled_map[name] = entry.get("enabled", True)
    return catalog, enabled_map


CATALOG, CATALOG_ENABLED = load_catalog()


def get_corpus_path(name):
    return os.path.join(ensure_data_dir(), name)


def validate_corpus_structure(corpus_dir, expected_subfolder=None):
    path = Path(corpus_dir)
    if expected_subfolder:
        path = path / expected_subfolder
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el recurso: {path}")
    extensions = {".txt", ".json", ".jsonl", ".csv", ".parquet", ".xlsx"}
    candidates = [path] if path.is_file() else path.rglob("*")
    if not any(candidate.is_file() and candidate.suffix.lower() in extensions
               and candidate.stat().st_size for candidate in candidates):
        raise ValueError(f"No se encontraron archivos compatibles en {path}")


def validate_download(path, metadata):
    size = os.path.getsize(path)
    if size == 0:
        raise ValueError("El archivo descargado está vacío.")
    if metadata.get("bytes") is not None and size != metadata["bytes"]:
        raise ValueError("El tamaño descargado no coincide con el catálogo.")
    if metadata.get("sha256"):
        checksum = hashlib.sha256()
        with open(path, "rb") as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                checksum.update(chunk)
        if checksum.hexdigest() != metadata["sha256"]:
            raise ValueError("La huella SHA-256 no coincide con el catálogo.")


def download_corpus(name, force=False):
    if name not in CATALOG:
        raise ValueError(f"Corpus '{name}' no está en el catálogo.")
    if not CATALOG_ENABLED[name]:
        raise ValueError(f"Corpus '{name}' no está habilitado.")
    metadata = CATALOG[name]
    path = Path(get_corpus_path(name))
    extension = metadata["extension"].lower()
    final_path = path / f"{name}.{extension}"
    if path.exists() and not force:
        if final_path.is_file():
            try:
                validate_download(final_path, metadata)
            except ValueError as error:
                raise ValueError(f"La copia local de '{name}' difiere del catálogo. "
                                 f"Usa download_corpus('{name}', force=True) para actualizarla.") from error
            return
        if extension == "zip" and any(path.iterdir()):
            validate_corpus_structure(path)
            return
    path.mkdir(parents=True, exist_ok=True)
    temporary_path = path / ".tmp_download"
    try:
        if metadata.get("id"):
            try:
                result = gdown.download(id=metadata["id"], output=str(temporary_path), quiet=True, use_cookies=False)
                if result is None:
                    raise IOError(f"Google Drive no devolvió el archivo de '{name}'.")
            except gdown.exceptions.FileURLRetrievalError:
                if not metadata.get("url_descarga"):
                    raise
                download_url(metadata["url_descarga"], temporary_path)
        elif metadata.get("url_descarga"):
            download_url(metadata["url_descarga"], temporary_path)
        else:
            raise ValueError(f"El corpus '{name}' no tiene una fuente de descarga.")
        validate_download(temporary_path, metadata)
        if extension == "zip":
            if not is_zipfile(temporary_path):
                raise ValueError("El archivo descargado no es un ZIP válido.")
            with ZipFile(temporary_path) as archive:
                for member in archive.namelist():
                    target = (path / member).resolve()
                    if os.path.commonpath([str(path.resolve()), str(target)]) != str(path.resolve()):
                        raise ValueError("El ZIP contiene una ruta fuera del directorio del corpus.")
                archive.extractall(path)
            temporary_path.unlink()
            validate_corpus_structure(path)
        else:
            os.replace(temporary_path, final_path)
            validate_corpus_structure(final_path)
        logger.info("Corpus '%s' listo en %s", name, path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def download_url(url, path):
    with requests.get(url, stream=True, timeout=(15, 120)) as response:
        response.raise_for_status()
        with Path(path).open("wb") as destination:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    destination.write(chunk)


def download_all_corpus(force=False):
    failures = {}
    for name in CATALOG:
        if not CATALOG_ENABLED[name]:
            continue
        try:
            download_corpus(name, force=force)
        except Exception as error:
            failures[name] = str(error)
            logger.error("Error con corpus '%s': %s", name, error)
    return failures
