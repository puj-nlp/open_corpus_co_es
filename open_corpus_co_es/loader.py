# loader.py
from nltk.text import Text
import ast
from nltk.tokenize import word_tokenize, sent_tokenize
import os, json, nltk, pandas as pd
import rdflib
from .downloader import get_corpus_path, load_catalog


try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
    nltk.download("punkt_tokenizer")

CATALOG, CATALOG_ENABLED  = load_catalog()


def list_corpus():
    fields_to_exclude = {"archivo", "url", "id", "url_descarga"}
    return {
        name: {k: v for k, v in meta.items() if k not in fields_to_exclude}
        for name, meta in CATALOG.items() if CATALOG_ENABLED.get('enabled', False) is True
    }


def extract_documents_from_dataframe(df):
    """
    Convierte un DataFrame en una lista de documentos, donde cada documento es un diccionario.
    Se busca una columna de texto principal y se agregan los demás campos como metadatos.
    """
    possible_names = ["text", "contenido", "tweet", "mensaje", "comentario", "descripcion", "texto"]
    text_col = next((col for col in df.columns if any(k in col.lower() for k in possible_names)), None)

    if text_col:
        docs = []
        for _, row in df.iterrows():
            row_dict = row.dropna().to_dict()
            text = row_dict.pop(text_col, None)
            if text:
                docs.append({"text": str(text), **row_dict})
        return docs
    else:
        print("[ADVERTENCIA] No se encontró columna de texto clara. Se retorna el DataFrame como dicts.")
        return df.to_dict(orient="records")


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

    return extract_documents_from_dataframe(df)


def load_corpus(name):
    if name not in CATALOG:
        raise ValueError(f"Corpus '{name}' no está en el catálogo.")

    meta = CATALOG[name]
    corpus_dir = get_corpus_path(name)

    if not os.path.exists(corpus_dir):
        raise FileNotFoundError(f"Corpus '{name}' no descargado. Usa download_corpus('{name}') primero.")

    # Si es un recurso tipo RDF
    if meta.get("tipo") == "resource" and meta.get("extension") == "rdf":
        rdf_files = [f for f in os.listdir(corpus_dir) if f.endswith(".rdf")]
        if not rdf_files:
            raise FileNotFoundError(f"No se encontró archivo .rdf para el recurso '{name}' en {corpus_dir}.")
        path = os.path.join(corpus_dir, rdf_files[0])
        g = rdflib.Graph()
        g.parse(path, format="xml")
        return g


    files = [f for f in os.listdir(corpus_dir) if os.path.isfile(os.path.join(corpus_dir, f))]
    all_text = []
    is_json_mode = False
    is_txt_mode = all(f.endswith(".txt") for f in files)


    if is_txt_mode:
        documentos = {}
        for fname in files:
            path = os.path.join(corpus_dir, fname)
            content = extract_text_from_file(path)
            nombre = os.path.splitext(fname)[0]
            documentos[nombre] = content
        return documentos

    for fname in files:
        path = os.path.join(corpus_dir, fname)
        content = extract_text_from_file(path)
        if isinstance(content, list):
            all_text.extend(content)
            is_json_mode = True
        else:
            all_text.append(content)

    if is_json_mode:
        return all_text

    tokenizer = CATALOG[name].get("tokenizacion", "Word").lower()
    joined_text = "\n".join(all_text)
    tokens = word_tokenize(joined_text) if tokenizer == "word" else sent_tokenize(joined_text)
    return Text(tokens)
