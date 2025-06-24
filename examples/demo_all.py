from open_corpus_co_es.loader import list_corpus, load_corpus
from open_corpus_co_es.downloader import download_corpus
import pprint
import time


def probar_corpus(nombre):
    try:
        print("\n==============================")
        print(f"📥 Probando corpus: {nombre}")
        download_corpus(nombre)
        datos = load_corpus(nombre)

        if isinstance(datos, dict):
            print(f"✔️  Diccionario con {len(datos)} entradas")
            ejemplo = list(datos.items())[0]
            print(f"Ejemplo: {ejemplo[0]} → {str(ejemplo[1])[:100]}...")

        elif isinstance(datos, list):
            print(f"✔️  Lista con {len(datos)} documentos")
            pprint.pprint(datos[0], indent=2, width=100)

        elif hasattr(datos, 'serialize'):
            print(f"✔️  RDF con {len(datos)} triples")
            for s, p, o in list(datos)[:3]:
                print(f"  - {s} {p} {o}")

        else:
            print("✔️  Texto plano")
            print(str(datos)[:200])

    except Exception as e:
        print(f"❌ Error con corpus '{nombre}': {e}")


def main():
    print("🔍 Iniciando pruebas de todos los corpus disponibles...\n")
    print(list_corpus())
    print("-" * 100)
    corpus_disponibles = ["presidentes", "laudato_si", ""]# list_corpus()
    print(f"\n🔎 Probando todos los corpus habilitados ({len(corpus_disponibles)}):\n")
    time.sleep(1)

    for nombre in corpus_disponibles:
        probar_corpus(nombre)
        time.sleep(0.5)

    print("\n✅ Pruebas finalizadas.")


if __name__ == "__main__":
    main()