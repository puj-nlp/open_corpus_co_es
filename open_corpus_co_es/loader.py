from nltk.text import Text
import ast
from nltk.tokenize import word_tokenize, sent_tokenize
import os, json, nltk, pandas as pd
from pathlib import Path
from .downloader import get_corpus_path, load_catalog
import csv

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
    nltk.download('punkt_tab')

CATALOG, CATALOG_ENABLED = load_catalog()


def detectar_separador(path, encoding="utf-8"):
    with open(path, encoding=encoding) as f:
        sample = f.read(2048)
        sniffer = csv.Sniffer()
        try:
            dialect = sniffer.sniff(sample)
            return dialect.delimiter
        except csv.Error:
            return ','


def list_corpus():
    fields_to_exclude = {"archivo", "url", "id", "url_descarga"}
    return {
        name: {k: v for k, v in meta.items() if k not in fields_to_exclude}
        for name, meta in CATALOG.items() if CATALOG_ENABLED.get(name, False)
    }


def extract_documents_from_dataframe(df):
    possible_names = ["text", "contenido", "tweet", "mensaje", "comentario", "descripcion", "texto"]
    text_col = next((col for col in df.columns if any(k in col.lower() for k in possible_names)), None)

    docs = []

    for _, row in df.iterrows():
        row_dict = row.dropna().to_dict()
        if text_col and text_col in row_dict:
            text = str(row_dict.pop(text_col))
        else:
            # Concatenar todas las columnas como texto si no hay columna clara
            text = " | ".join(str(v) for v in row_dict.values())
        if text.strip():
            docs.append({"text": text, **row_dict})

    return docs


def extract_documents_from_dataframe_old(df):
    possible_names = ["text", "contenido", "tweet", "mensaje", "comentario", "descripcion", "texto",
                      "Hit Sentence", "Hit Text", "sentence", "frase", "content"]
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
    df = None
    if ext == ".txt":
        try:
            with open(path, encoding="utf-8") as f:
                return f.read()
        except UnicodeDecodeError:
            try:
                with open(path, encoding="latin1") as f:
                    return f.read()
            except UnicodeDecodeError:
                with open(path, encoding="windows-1252", errors="replace") as f:
                    return f.read()
    elif ext == ".csv":
        try:
            sep = detectar_separador(path)
            df = pd.read_csv(path, sep=sep, encoding="utf-8")
        except UnicodeDecodeError:
            sep = detectar_separador(path, encoding="latin1")
            df = pd.read_csv(path, sep=sep, encoding="latin1")
    elif ext == ".xlsx":
        df = pd.read_excel(path)
    elif ext == ".parquet":
        df = pd.read_parquet(path)
    elif ext in [".jsonl", ".json"]:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        try:
            return [json.loads(line) for line in lines if line.strip()]
        except json.JSONDecodeError as e:
            print(f"[ERROR] No se pudo decodificar JSON: {e}")
            return []
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
    base_path = Path(get_corpus_path(name))

    if not base_path.exists():
        raise FileNotFoundError(
            f"Corpus '{name}' no descargado. Usa download_corpus('{name}') primero."
        )

    files = [f for f in base_path.rglob("*") if f.is_file()]
    if not files:
        raise FileNotFoundError(f"No se encontraron archivos en el corpus '{name}'.")

    all_text = []
    is_json_mode = False
    #is_txt_mode = all(f.suffix == ".txt" for f in files)

    #if is_txt_mode:
    txt_files = [f for f in files if f.suffix == ".txt"]

    if txt_files:
        documentos = {}
        for file in files:
            content = extract_text_from_file(str(file))
            rel_parts = list(file.relative_to(base_path).parts)
            # clave = carpeta1_carpeta2_nombrearchivo
            if len(rel_parts) > 1:
                key = "_".join(rel_parts[:-1] + [file.stem])
            else:
                key = file.stem
            tokenizer = meta.get("tokenizacion", "Word").lower()
            tokens = word_tokenize(content) if tokenizer == "word" else sent_tokenize(content)
            documentos[key] = Text(tokens)
        return documentos

    for file in files:
        content = extract_text_from_file(str(file))
        if isinstance(content, list):
            all_text.extend(content)
            is_json_mode = True
        else:
            all_text.append(content)

    if is_json_mode:
        return all_text

    tokenizer = meta.get("tokenizacion", "Word").lower()
    joined_text = "\n".join(map(str, all_text))
    tokens = word_tokenize(joined_text) if tokenizer == "word" else sent_tokenize(joined_text)
    return Text(tokens)
