# Open Corpus CO-ES

Biblioteca de descarga y carga de corpus y recursos tabulares para procesamiento de lenguaje natural, con énfasis en Colombia y América Latina.

Versión publicada: **0.1.1a4**. Inventario auditado el **21 de octubre de 2026**: **66 entradas**, **65 habilitadas** y una deshabilitada. Incluye corpus documentales, publicaciones, noticias, discursos, recursos léxicos e indicadores internacionales. Los archivos de datos se descargan desde Google Drive y no se incluyen dentro del paquete.

## Instalación

Requiere Python 3.9 o posterior. Para incluir versiones preliminares:

```bash
pip install --upgrade open_corpus_co_es==0.1.1a4
```

Para instalar esta revisión desde el repositorio:

```bash
pip install -e .
```

## Uso desde Python

```python
from open_corpus_co_es import download_corpus, list_corpus, load_corpus

inventario = list_corpus()
nombre = "presidentes"
download_corpus(nombre)
documentos = load_corpus(nombre)
print(len(documentos))
print(documentos[0]["text"][:200])

download_corpus(nombre, force=True)
```

`list_corpus()` devuelve un diccionario de entradas habilitadas con descripción, formato, filas, columnas, campos, tamaño y SHA-256. `download_corpus()` comprueba tamaño y SHA-256 antes de reemplazar un archivo. Una descarga fallida con `force=True` conserva el archivo anterior. Si cambia el archivo remoto, se necesita una nueva verificación del catálogo.

Los corpus tabulares del inventario se cargan como listas de diccionarios. Cuando hay una columna textual configurada, se expone como `text`; los demás campos disponibles se conservan. Los registros de `Raw_data` conservan su estructura original. Si el recurso contiene indicadores sin texto, `text` es una representación de sus campos, no un discurso ni un documento original. Las celdas nulas se omiten. No se eliminan duplicados.

Los registros con texto vacío se conservan como `text=""` con sus metadatos. Los archivos se guardan en `~/.open_corpus_co_es/data/<nombre>/`. La carga completa puede necesitar memoria considerable, especialmente para los corpus de 915.939 filas. Si una copia local antigua no coincide con el catálogo actualizado, usa `download_corpus(nombre, force=True)`.

## Línea de comandos

```bash
python -m open_corpus_co_es --list
python -m open_corpus_co_es --download presidentes
python -m open_corpus_co_es --download presidentes --force
python -m open_corpus_co_es --download dragons_rag
python -m open_corpus_co_es --download_all
```

`--download_all` omite entradas deshabilitadas y devuelve un código de error si alguna descarga falla.

## Inventario y cobertura

La [referencia completa de los 66 recursos](docs/corpus.md) incluye el estado de cada entrada, filas, columnas, formato, país y año declarados, campos, ubicación y huella de integridad.

- Educación, salud y seguridad: Argentina, Colombia y México; versiones v1 y v2.
- Noticias: Colombia, Ecuador y Perú.
- CEV: entrevistas y documentos procesados para RAG.
- Recursos generales: presidentes, edades, música, educación primaria, textos humanos/LLM, discurso de odio, ODS y Laudato si.
- Dragons RAG: 169.248 documentos de Bluesky, Media Cloud y GDELT.
- Global Populism Database: siete colecciones de discursos, rúbricas e indicadores.
- Recursos léxicos y tesauro CEV.

`presidentes` está actualizado a 2026 y contiene **22 registros**, incluido Abelardo de la Espriella, etiquetado 2026–2030. El final del periodo no es la fecha de actualización. Hay una etiqueta histórica inconsistente para Jorge Eliécer Gaitán en el archivo original; consulta las limitaciones en el inventario.

Las versiones Excel de educación primaria y textos humanos/LLM se llaman `educacion_primaria_excel` y `llm_humano_excel`; los nombres sin sufijo siguen cargando Parquet. Algunos nombres diferentes apuntan a contenido idéntico, documentado en la auditoría.

La [auditoría](docs/auditoria.md) distingue integridad técnica, completitud del inventario y limitaciones de procedencia. El país y año heredados son etiquetas de la colección; no acreditan por sí solos la fecha o el lugar de cada documento. La licencia MIT del código no sustituye las condiciones de uso de las fuentes de datos.

## Desarrollo y publicación

```bash
python -m pytest tests
python -m build
python -m twine check dist/open_corpus_co_es-0.1.1a4*
```

Consulta la [guía de publicación](docs/publicacion.md) para subir únicamente los artefactos de la versión verificada.

## Autor y licencia

Luis Gabriel Moreno Sandoval — Pontificia Universidad Javeriana — morenoluis@javeriana.edu.co.

Código bajo licencia MIT. Consulta `LICENSE`.
