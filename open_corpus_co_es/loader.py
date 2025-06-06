from nltk.text import Text
from nltk.tokenize import word_tokenize, sent_tokenize
import os, json, nltk

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

from .downloader import get_corpus_path, CATALOG

def list_corpus():
    return {name: meta["description"] for name, meta in CATALOG.items()}

def load_corpus(name):
    if name not in CATALOG:
        raise ValueError(f"Corpus '{name}' no está en el catálogo.")

    corpus_dir = get_corpus_path(name)
    if not os.path.exists(corpus_dir):
        raise FileNotFoundError(f"Corpus '{name}' no descargado. Usa download_corpus('{name}') primero.")

    all_text = ""
    for fname in os.listdir(corpus_dir):
        path = os.path.join(corpus_dir, fname)
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                all_text += "\n" + f.read()

    tok = CATALOG[name]["tokenizer"]
    tokens = word_tokenize(all_text) if tok == "word" else sent_tokenize(all_text)
    return Text(tokens)
