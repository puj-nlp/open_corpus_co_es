import argparse
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import pyarrow.parquet as pq


def inspect_file(path):
    checksum = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            checksum.update(chunk)
    if path.suffix == ".parquet":
        parquet = pq.ParquetFile(path)
        rows = parquet.metadata.num_rows
        columns = parquet.schema_arrow.names
        sample = next(parquet.iter_batches(batch_size=100), None)
        frame = sample.to_pandas() if sample is not None else pd.DataFrame(columns=columns)
        for batch in parquet.iter_batches(batch_size=16384):
            batch.validate(full=True)
    elif path.suffix == ".xlsx":
        frame = pd.read_excel(path)
        rows = len(frame)
        columns = list(frame.columns)
    else:
        for encoding in ("utf-8-sig", "cp1252", "latin1"):
            try:
                options = {"header": None, "names": ["word", "freq", "norm"]} if path.name == "lexicon_referencia_crea.csv" else {}
                frame = pd.read_csv(path, sep=None, engine="python", encoding=encoding, **options)
                break
            except UnicodeDecodeError:
                continue
        rows = len(frame)
        columns = list(frame.columns)
    result = {
        "archivo": path.name,
        "bytes": path.stat().st_size,
        "sha256": checksum.hexdigest(),
        "filas": rows,
        "columnas": [str(column) for column in columns],
        "muestra_filas": len(frame),
        "muestra_columnas_vacias": [str(column) for column in columns if frame[column].isna().all()],
        "lectura_completa": True,
    }
    if path.name == "presidentes.parquet":
        frame = pd.read_parquet(path)
        result["periodos"] = frame.drop(columns="text").to_dict("records")
        result["textos_vacios"] = int(frame["text"].fillna("").str.strip().eq("").sum())
    return result


def main():
    parser = argparse.ArgumentParser(description="Audita los archivos tabulares de Corpus sin modificarlos.")
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("temp/corpus_audit_local.json"))
    args = parser.parse_args()
    paths = [
        path for folder in ("corpora", "resource") for path in (args.root / folder).rglob("*")
        if path.suffix in {".parquet", ".xlsx", ".csv"} and path.is_file() and not path.name.startswith("~$")
    ]
    report = {"fecha_utc": datetime.now(timezone.utc).isoformat(), "archivos": [], "errores": []}
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(inspect_file, path): path for path in paths}
        for future in as_completed(futures):
            path = futures[future]
            try:
                result = future.result()
                result["ruta_relativa"] = path.relative_to(args.root).as_posix()
                report["archivos"].append(result)
                print("OK", path.name, result["filas"], flush=True)
            except Exception as error:
                report["errores"].append({"archivo": path.name, "error": str(error)})
                print("ERROR", path.name, str(error), flush=True)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("AUDIT", len(report["archivos"]), "OK", len(report["errores"]), "errors", flush=True)


if __name__ == "__main__":
    main()
