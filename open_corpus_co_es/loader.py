from nltk.text import Text
import ast
from nltk.tokenize import word_tokenize, sent_tokenize
import os, json, nltk, pandas as pd
from pathlib import Path
from .downloader import get_corpus_path, load_catalog
import csv

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


def extract_documents_from_dataframe(df, text_column=None):
    possible_names = ["text", "texto", "contenido", "tweet", "mensaje", "comentario", "descripcion",
                      "description", "hit sentence", "hit text", "content", "lyrics", "res", "word", "palabra"]
    columns = {str(column).lower(): column for column in df.columns}
    text_col = text_column or next((columns[name] for name in possible_names if name in columns), None)
    if text_col is not None and text_col not in df.columns:
        raise ValueError(f"No se encontró la columna de texto: {text_col}")

    docs = []

    for record in df.to_dict(orient="records"):
        row_dict = {
            key: value for key, value in record.items()
            if not (pd.api.types.is_scalar(value) and pd.isna(value))
        }
        if text_col:
            text = str(row_dict.pop(text_col, ""))
        else:
            # Concatenar todas las columnas como texto si no hay columna clara
            text = " | ".join(str(v) for v in row_dict.values())
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


def extract_text_from_file(path, metadata=None):
    metadata = metadata or {}
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
            df = pd.read_csv(path, sep=sep, encoding="utf-8", **metadata.get("opciones_lectura", {}))
        except UnicodeDecodeError:
            sep = detectar_separador(path, encoding="latin1")
            df = pd.read_csv(path, sep=sep, encoding="latin1", **metadata.get("opciones_lectura", {}))
    elif ext == ".xlsx":
        df = pd.read_excel(path)
    elif ext == ".parquet":
        df = pd.read_parquet(path)
    elif ext in [".jsonl", ".json"]:
        with open(path, encoding="utf-8") as f:
            if ext == ".json":
                payload = json.load(f)
                return payload if isinstance(payload, list) else [payload]
            return [json.loads(line) for line in f if line.strip()]
    else:
        return ""

    if "Raw_data" in df.columns:
        json_objects = []
        for idx, raw in df["Raw_data"].dropna().items():
            if isinstance(raw, dict):
                json_objects.append(raw)
                continue
            try:
                obj = json.loads(raw)
            except json.JSONDecodeError:
                try:
                    obj = ast.literal_eval(raw)
                except Exception as e:
                    raise ValueError(f"Raw_data inválido en la fila {idx} de {path}") from e
            if isinstance(obj, dict):
                json_objects.append(obj)
        return json_objects

    return extract_documents_from_dataframe(df, metadata.get("columna_texto"))


def load_corpus(name):
    if name not in CATALOG:
        raise ValueError(f"Corpus '{name}' no está en el catálogo.")

    meta = CATALOG[name]
    base_path = Path(get_corpus_path(name))

    if not base_path.exists():
        raise FileNotFoundError(
            f"Corpus '{name}' no descargado. Usa download_corpus('{name}') primero."
        )

    extensions = {".txt", ".csv", ".xlsx", ".parquet", ".json", ".jsonl"}
    files = sorted(f for f in base_path.rglob("*") if f.is_file() and f.suffix.lower() in extensions
                   and not f.name.endswith(".manifest.json"))
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
            if file.suffix != ".txt":
                continue
            content = extract_text_from_file(str(file), meta)
            rel_parts = list(file.relative_to(base_path).parts)
            # clave = carpeta1_carpeta2_nombrearchivo
            if len(rel_parts) > 1:
                key = "_".join(rel_parts[:-1] + [file.stem])
            else:
                key = file.stem
            tokenizer = (meta.get("tokenizacion") or "Word").lower()
            tokens = word_tokenize(content) if tokenizer == "word" else sent_tokenize(content)
            documentos[key] = Text(tokens)
        return documentos

    for file in files:
        content = extract_text_from_file(str(file), meta)
        if isinstance(content, list):
            all_text.extend(content)
            is_json_mode = True
        else:
            all_text.append(content)

    if is_json_mode:
        return all_text

    tokenizer = (meta.get("tokenizacion") or "Word").lower()
    joined_text = "\n".join(map(str, all_text))
    tokens = word_tokenize(joined_text) if tokenizer == "word" else sent_tokenize(joined_text)
    return Text(tokens)
