import argparse
from .downloader import download_corpus, download_all_corpus
from .loader import list_corpus


def main():
    parser = argparse.ArgumentParser(description="Gestión CLI para Open Corpus CO-ES")
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--list", action="store_true", help="Listar corpus disponibles")
    actions.add_argument("--download", help="Descargar un corpus específico por nombre")
    actions.add_argument("--download_all", action="store_true", help="Descargar todos los corpus habilitados")
    parser.add_argument("--force", action="store_true", help="Descargar nuevamente el archivo")

    args = parser.parse_args()

    if args.list:
        print("\n📂 Corpus disponibles:")
        for nombre in list_corpus():
            print(f"- {nombre}")
    elif args.download:
        print(f"\n📥 Descargando corpus: {args.download}")
        try:
            download_corpus(args.download, force=args.force)
            print("✅ Descarga completada.")
        except Exception as e:
            parser.exit(1, f"Error: {e}\n")
    elif args.download_all:
        failures = download_all_corpus(force=args.force)
        if failures:
            parser.exit(1, f"Falló la descarga de {len(failures)} corpus.\n")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
