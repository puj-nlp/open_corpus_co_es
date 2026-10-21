import argparse
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import gdown


def verify(entry, directory):
    name = entry.get("nombre", Path(entry["archivo"]).stem)
    path = directory / (name + "." + entry["extension"])
    if not path.exists():
        result = gdown.download(id=entry["id"], output=str(path), quiet=True, use_cookies=False)
        if result is None:
            raise IOError("Google Drive no devolvió el archivo")
    checksum = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            checksum.update(chunk)
    if path.stat().st_size != entry["bytes"] or checksum.hexdigest() != entry["sha256"]:
        raise ValueError("La descarga difiere del archivo local auditado")
    return {"nombre": name, "id": entry["id"], "bytes": path.stat().st_size,
            "sha256": checksum.hexdigest(), "estado": "ok"}


def main():
    parser = argparse.ArgumentParser(description="Verifica descargas anónimas de todas las entradas habilitadas.")
    parser.add_argument("--catalog", type=Path, default=Path("open_corpus_co_es/catalog.json"))
    parser.add_argument("--output", type=Path, default=Path("temp/download_audit.json"))
    parser.add_argument("--directory", type=Path, default=Path("temp/audited_downloads"))
    args = parser.parse_args()
    args.directory.mkdir(parents=True, exist_ok=True)
    catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    report = {"fecha_utc": datetime.now(timezone.utc).isoformat(), "resultados": []}
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(verify, entry, args.directory): entry for entry in catalog if entry["enabled"]}
        for future in as_completed(futures):
            entry = futures[future]
            name = entry.get("nombre", Path(entry["archivo"]).stem)
            try:
                result = future.result()
            except Exception as error:
                result = {"nombre": name, "estado": "error", "error": str(error)}
            report["resultados"].append(result)
            print(result["estado"], name, result.get("error", ""), flush=True)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    failures = sum(result["estado"] != "ok" for result in report["resultados"])
    print("DOWNLOAD_AUDIT", len(report["resultados"]), "failures", failures, flush=True)
    raise SystemExit(bool(failures))


if __name__ == "__main__":
    main()
