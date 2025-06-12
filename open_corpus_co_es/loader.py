# loader.py
from nltk.text import Text
import ast
from nltk.tokenize import word_tokenize, sent_tokenize
import os, json, nltk, pandas as pd
from .downloader import get_corpus_path, load_catalog

try:
    nltk.download("punkt_tab")
    nltk.download("punkt")
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

CATALOG = load_catalog()

def list_corpus():
    fields_to_exclude = {"archivo", "url", "id", "url_descarga"}
    return {
        name: {k: v for k, v in meta.items() if k not in fields_to_exclude}
        for name, meta in CATALOG.items()
    }

def extract_text_from_file(path):
    ext = os.path.splitext(path)[-1].lower()
    if ext == ".txt":
        with open(path, encoding="utf-8") as f:
            return f.read()
    elif ext == ".csv":
        df = pd.read_csv(path)
    elif ext == ".xlsx":
        df = pd.read_excel(path)
    elif ext == ".parquet":
        df = pd.read_parquet(path)
    else:
        return ""

    # Detectar columna tipo JSON crudo
    if "Raw_data" in df.columns:
        json_objects = []
        for idx, raw in df["Raw_data"].dropna().astype(str).items():
            try:
                obj = json.loads(raw)
            except json.JSONDecodeError:
                try:
                    obj = ast.literal_eval(raw)
                except Exception as e:
                    print(f"[ERROR] Fila {idx} en Raw_data no se pudo parsear como JSON: {e}")
                    continue
            if isinstance(obj, dict):
                json_objects.append(obj)
        return json_objects

    # Si no es JSON, buscamos columnas con texto plano
    possible_names = ["text", "contenido", "tweet", "mensaje", "comentario", "descripcion", "texto"]
    text_columns = [col for col in df.columns if any(k in col.lower() for k in possible_names)]

    if not text_columns:
        print(f"[ADVERTENCIA] No se encontraron columnas de texto en {path}")
        print(f"Columnas disponibles: {list(df.columns)}")
        return df.to_dict(orient="records")

    textos = []
    for col in text_columns:
        textos.extend(df[col].dropna().astype(str).str.strip().tolist())
    return "\n".join(textos)

def load_corpus(name):
    if name not in CATALOG:
        raise ValueError(f"Corpus '{name}' no está en el catálogo.")
    corpus_dir = get_corpus_path(name)
    if not os.path.exists(corpus_dir):
        raise FileNotFoundError(f"Corpus '{name}' no descargado. Usa download_corpus('{name}') primero.")

    all_text = []
    is_json_mode = False

    for fname in os.listdir(corpus_dir):
        path = os.path.join(corpus_dir, fname)
        if os.path.isfile(path):
            content = extract_text_from_file(path)
            if isinstance(content, list):  # Lista de objetos JSON
                all_text.extend(content)
                is_json_mode = True
            else:
                all_text.append(content)

    if is_json_mode:
        return all_text  # No tokenizamos, retornamos objetos JSON

    tokenizer = CATALOG[name].get("tokenizacion", "Word").lower()
    joined_text = "\n".join(all_text)
    tokens = word_tokenize(joined_text) if tokenizer == "word" else sent_tokenize(joined_text)
    return Text(tokens)

