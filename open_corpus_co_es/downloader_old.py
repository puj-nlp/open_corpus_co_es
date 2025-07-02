import requests
from tqdm import tqdm
from zipfile import ZipFile, is_zipfile
from .utils import ensure_data_dir
import json
import importlib.resources
import os

def load_catalog():
    with importlib.resources.open_text("open_corpus_co_es", "catalog_v2.json", encoding="utf-8") as f:
        raw = json.load(f)

    catalog = {}
    enabled_map = {}

    for entry in raw:
        key = os.path.splitext(entry["archivo"])[0]
        enabled = entry.get("enabled", True)
        entry["enabled"] = enabled

        catalog[key] = entry
        enabled_map[key] = enabled

    return catalog, enabled_map


def get_corpus_path(name):
    return os.path.join(ensure_data_dir(), name)

CATALOG, CATALOG_ENABLED = load_catalog()


def is_zipfile_from_url(response):
    content_type = response.headers.get("Content-Type", "")
    # First check content-type header
    if "zip" in content_type:
        return True
    # Peek at the first 4 bytes without consuming the stream
    peek = next(response.iter_content(4, False))
    return peek == b"PK\x03\x04"


def download_corpus_old(name, force=False):
    if name not in CATALOG:
        raise ValueError(f"Corpus '{name}' no está disponible en el catálogo. Por favor, revisa el nombre.")

    if CATALOG_ENABLED[name] is False:
        raise Exception(f"Corpus '{name}' no está habilitado en el catálogo. Por favor, revisa el nombre.")

    corpus_dir = get_corpus_path(name)
    if os.path.exists(corpus_dir):
        if os.listdir(corpus_dir):
            if not force:
                print(f"[INFO] Corpus '{name}' ya está cargado. Usa force=True para forzar descarga.")
                return
            else:
                print(f"[INFO] Reescribiendo corpus '{name}'...")
                for f in os.listdir(corpus_dir):
                    file_path = os.path.join(corpus_dir, f)
                    if os.path.isdir(file_path):
                        import shutil
                        shutil.rmtree(file_path)
                    else:
                        os.remove(file_path)

    os.makedirs(corpus_dir, exist_ok=True)
    url = CATALOG[name].get("url_descarga")
    if not url:
        raise ValueError(f"Corpus '{name}' no tiene una URL de descarga válida.")

    print(f"⬇️ Cargando corpus '{name}' ...")
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception(f"No se pudo cargar el archivo '{name}' (status {response.status_code}).")

    tmp_path = os.path.join(corpus_dir, "tmp_download")

    # Check if it's a zip file before writing
    is_zip = is_zipfile_from_url(response)

    with open(tmp_path, "wb") as f:
        for chunk in tqdm(response.iter_content(chunk_size=8192)):
            if chunk:
                f.write(chunk)

    if is_zip:
        print(f"📦 Archivo ZIP detectado. Descomprimiendo...")
        print('tmp_path', tmp_path)
        print('corpus_dir', corpus_dir)
        with ZipFile(tmp_path, "r") as zip_ref:
            zip_ref.extractall(corpus_dir)
        os.remove(tmp_path)

        subfolder = CATALOG[name].get("subfolder")
        if subfolder:
            subfolder_path = os.path.join(corpus_dir, subfolder)
            if not os.path.exists(subfolder_path):
                raise FileNotFoundError(
                    f"[ERROR] Se esperaba la subcarpeta '{subfolder}' dentro del corpus '{name}', pero no se encontró."
                )
    else:
        ext = CATALOG[name].get("extension", "")
        final_path = os.path.join(corpus_dir, f"{name}.{ext}")
        os.rename(tmp_path, final_path)

    print(f"✅ Corpus '{name}' listo en: {corpus_dir}")

def download_corpus(name, force=False):
    if name not in CATALOG:
        raise ValueError(f"Corpus '{name}' no está disponible en el catálogo. Por favor, revisa el nombre.")

    if CATALOG_ENABLED[name] is False:
        raise Exception(f"Corpus '{name}' no está habilitado en el catálogo. Por favor, revisa el nombre.")

    corpus_dir = get_corpus_path(name)
    if os.path.exists(corpus_dir):
        if os.listdir(corpus_dir):
            if not force:
                print(f"[INFO] Corpus '{name}' ya está cargado. Usa force=True para forzar descarga.")
                return
            else:
                print(f"[INFO] Reescribiendo corpus '{name}'...")
                for f in os.listdir(corpus_dir):
                    file_path = os.path.join(corpus_dir, f)
                    if os.path.isdir(file_path):
                        import shutil
                        shutil.rmtree(file_path)
                    else:
                        os.remove(file_path)

    os.makedirs(corpus_dir, exist_ok=True)
    url = CATALOG[name].get("url_descarga")
    if not url:
        raise ValueError(f"Corpus '{name}' no tiene una URL de descarga válida.")

    print(f"⬇️ Cargando corpus '{name}' ...")
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception(f"No se pudo cargar el archivo '{name}' (status {response.status_code}).")

    tmp_path = os.path.join(corpus_dir, "tmp_download")
    is_zip = is_zipfile_from_url(response)

    with open(tmp_path, "wb") as f:
        for chunk in tqdm(response.iter_content(chunk_size=8192)):
            if chunk:
                f.write(chunk)

    if is_zip:
        print(f"📦 Archivo ZIP detectado. Descomprimiendo...")
        with ZipFile(tmp_path, "r") as zip_ref:
            zip_ref.extractall(corpus_dir)
        os.remove(tmp_path)

        subfolder = CATALOG[name].get("subfolder")
        if subfolder:
            subfolder_path = os.path.join(corpus_dir, subfolder)
            if not os.path.exists(subfolder_path):
                raise FileNotFoundError(
                    f"[ERROR] Se esperaba la subcarpeta '{subfolder}' dentro del corpus '{name}', pero no se encontró. "
                    f"Verifica que el ZIP tenga la estructura correcta o ajusta el campo 'subfolder' en el catálogo."
                )
        else:
            print(f"[INFO] No se especificó subcarpeta. Archivos extraídos directamente en {corpus_dir}.")
    else:
        ext = CATALOG[name].get("extension", "")
        final_path = os.path.join(corpus_dir, f"{name}.{ext}")
        os.rename(tmp_path, final_path)

    print(f"✅ Corpus '{name}' listo en: {corpus_dir}")


def download_all_corpus(force=False):
    for name in CATALOG:
        download_corpus(name, force)
