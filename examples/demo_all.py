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
    corpus_disponibles = list_corpus()
    # Pruebas por grupos de corpus.
    # corpus_disponibles = ["presidentes"]
    # corpus_disponibles = ["lexicon_duelo_completa", "lexicon_ejecuciones_extrajudiciales", "lexicon_estigmatizacion"]
    # corpus_disponibles = ["lexicon_actors_roles", "lexicon_actors_roles_excel_v2", "lexicon_afectivo_categorias",
    #                       "lexicon_afectivo_categorias_v2"]
    # corpus_disponibles = ["es_hs_project_raw_extended", "es_hs_project_raw_extended_v2"]
    # corpus_disponibles = ["salud_argentina_2024_v2",  "salud_argentina_2024_v1", "salud_colombia_2024_v1",
    #                       "salud_mexico_2024_v1", "salud_mexico_2024_v2", "seguridad_argentina_2024_v2",
    #                       "seguridad_argentina_2024_v1","seguridad_colombia_2024_v1"]
    # corpus_disponibles = ["musica_metrica", "musica_letra"] # list_corpus()
    # corpus_disponibles = ["educacion_argentina_2024_v1", "salud_argentina_2024_v1", "seguridad_argentina_2024_v1",
    #                       "educacion_colombia_2024_v1", "salud_colombia_2024_v1", "seguridad_colombia_2024_v1",
    #                       "educacion_mexico_2024_v1", "salud_mexico_2024_v1", "seguridad_mexico_2024_v1"] # ["presidentes", "laudato_si", "ods"]# list_corpus()
    # corpus_disponibles = ["educacion_argentina_2024_v1", "educacion_argentina_2024_v2", "presidentes", "laudato_si", "ods"]
    print(f"\n🔎 Probando todos los corpus habilitados ({len(corpus_disponibles)}):\n")
    time.sleep(1)

    for nombre in corpus_disponibles:
        probar_corpus(nombre)
        time.sleep(0.5)

    print("\n✅ Pruebas finalizadas.")

if __name__ == "__main__":
    main()