# downloader.py
import os
import urllib.request
import zipfile
import json

BASE_DIR = os.path.expanduser("~/.open_corpus_co_es/data")
CATALOG_PATH = os.path.join(os.path.dirname(__file__), "catalog.json")

def load_catalog():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return {os.path.splitext(entry["archivo"])[0]: entry for entry in raw}

CATALOG = load_catalog()

def get_corpus_path(name):
    return os.path.join(BASE_DIR, name)

def download_corpus(name):
    if name not in CATALOG:
        raise ValueError(f"Corpus '{name}' no está en el catálogo.")
    os.makedirs(BASE_DIR, exist_ok=True)
    url = CATALOG[name]["url_descarga"]
    extension = CATALOG[name]["extension"]
    dest_path = os.path.join(BASE_DIR, f"{name}.{extension}")
    print(f"Descargando {name} desde {url}...")
    urllib.request.urlretrieve(url, dest_path)
    if extension == "zip":
        with zipfile.ZipFile(dest_path, "r") as zip_ref:
            zip_ref.extractall(get_corpus_path(name))
        os.remove(dest_path)
    else:
        os.makedirs(get_corpus_path(name), exist_ok=True)
        os.replace(dest_path, os.path.join(get_corpus_path(name), f"{name}.{extension}"))
    print(f"{name} descargado y listo.")

def download_all_corpus():
    for name in CATALOG:
        download_corpus(name)
