import argparse
from .downloader import download_corpus
from .loader import list_corpus


def main():
    parser = argparse.ArgumentParser(description="Gestión CLI para Open Corpus CO-ES")
    parser.add_argument("--list", action="store_true", help="Listar corpus disponibles")
    parser.add_argument("--download", help="Descargar un corpus específico por nombre")

    args = parser.parse_args()

    if args.list:
        print("\n📂 Corpus disponibles:")
        for nombre in list_corpus():
            print(f"- {nombre}")
    elif args.download:
        print(f"\n📥 Descargando corpus: {args.download}")
        try:
            download_corpus(args.download)
            print("✅ Descarga completada.")
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()