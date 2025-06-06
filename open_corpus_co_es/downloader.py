import os
import urllib.request
import zipfile
import json

BASE_DIR = os.path.expanduser("~/.open_corpus_co_es/data")
CATALOG_PATH = os.path.join(os.path.dirname(__file__), "catalog.json")

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    CATALOG = json.load(f)

def get_corpus_path(name):
    return os.path.join(BASE_DIR, name)

def download_corpus(name):
    if name not in CATALOG:
        raise ValueError(f"Corpus '{name}' no está en el catálogo.")
    os.makedirs(BASE_DIR, exist_ok=True)
    url = CATALOG[name]["url"]
    zip_path = os.path.join(BASE_DIR, f"{name}.zip")
    print(f"Descargando {name} desde {url}...")
    urllib.request.urlretrieve(url, zip_path)
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(get_corpus_path(name))
    os.remove(zip_path)
    print(f"{name} descargado y listo.")

def download_all_corpus():
    for name in CATALOG:
        download_corpus(name)
