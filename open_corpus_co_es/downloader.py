# -*- coding: utf-8 -*-
import requests
from tqdm import tqdm
from zipfile import ZipFile
from .utils import ensure_data_dir
import json
import importlib.resources
import os
import importlib.resources


def load_catalog():
    """
    Lee catalog_v2.json desde el paquete `open_corpus_co_es` y devuelve dos objetos:
    1. catalog (dict): {nombre_sin_ext: entry_dict_completo}
    2. enabled_map (dict): {nombre_sin_ext: bool_enabled}

    Para los registros que aún no incluyan la clave "enabled",
    se asume True por compatibilidad.
    """
    # Abrir el recurso de texto dentro del paquete
    with importlib.resources.open_text(
        "open_corpus_co_es", "catalog_v2.json", encoding="utf-8"
    ) as f:
        raw = json.load(f)

    catalog = {}
    enabled_map = {}

    for entry in raw:
        key = os.path.splitext(entry["archivo"])[0]
        # Aseguramos que todos tengan 'enabled' (por defecto True)
        enabled = entry.get("enabled", True)
        entry["enabled"] = enabled

        catalog[key] = entry
        enabled_map[key] = enabled

    return catalog, enabled_map



def get_corpus_path(name):
    return os.path.join(ensure_data_dir(), name)

CATALOG, CATALOG_ENABLED = load_catalog()

def download_corpus(name):
    if name not in CATALOG:
        raise ValueError(f"Corpus '{name}' no está disponible en el catálogo. Por favor, revisa el nombre.")

    if CATALOG_ENABLED[name] is False:
        raise Exception(f"Corpus '{name}' no está habilitado en el catálogo. Por favor, revisa el nombre.")

    corpus_dir = get_corpus_path(name)
    if os.path.exists(corpus_dir) and os.listdir(corpus_dir):
        print(f"[INFO] Corpus '{name}'. Ya esta cargado.")
        return

    os.makedirs(corpus_dir, exist_ok=True)

    url = CATALOG[name].get("url_descarga")
    if not url:
        raise ValueError(f"Corpus '{name}' no tiene una URL de descarga válida.")

    print(f"Cargando {name} ...")
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception(f"No se pudo cargar el archivo {name}.")

    file_path = os.path.join(corpus_dir, f"{name}.zip")
    with open(file_path, "wb") as f:
        for chunk in tqdm(response.iter_content(chunk_size=8192)):
            if chunk:
                f.write(chunk)

    print(f"{name} cargado. Descomprimiendo...")
    with ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(corpus_dir)

    os.remove(file_path)
    print(f"{name} listo en {corpus_dir}.")

def download_all_corpus():
    for name in CATALOG:
        download_corpus(name)