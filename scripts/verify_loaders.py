import gc
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from open_corpus_co_es.loader import extract_text_from_file


def main():
    root = Path(sys.argv[1])
    catalog = json.loads(Path("open_corpus_co_es/catalog.json").read_text(encoding="utf-8"))
    report = {"fecha_utc": datetime.now(timezone.utc).isoformat(), "resultados": []}
    for entry in catalog:
        name = entry.get("nombre", Path(entry["archivo"]).stem)
        try:
            documents = extract_text_from_file(str(root / entry["ruta_drive"]), entry)
            result = {"nombre": name, "filas_archivo": entry["filas"], "registros_cargados": len(documents),
                      "estado": "ok" if len(documents) == entry["filas"] else "diferencia_filas"}
            del documents
            gc.collect()
        except Exception as error:
            result = {"nombre": name, "estado": "error", "error": str(error)}
        report["resultados"].append(result)
        print(json.dumps(result, ensure_ascii=True), flush=True)
        Path("temp/loader_audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    raise SystemExit(any(result["estado"] != "ok" for result in report["resultados"]))


if __name__ == "__main__":
    main()
