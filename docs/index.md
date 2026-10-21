---
layout: home
title: Open Corpus CO-ES
description: Descarga y carga de corpus y recursos tabulares para PLN
permalink: /
nav_order: 1
---

# Open Corpus CO-ES

Versión **[0.1.1a4 publicada en PyPI](https://pypi.org/project/open-corpus-co-es/0.1.1a4/)** el 21 de octubre de 2026.

**66 entradas auditadas · 65 habilitadas · 17 pruebas aprobadas**

Descarga y carga corpus documentales, publicaciones, noticias, discursos, entrevistas, recursos léxicos e indicadores para procesamiento de lenguaje natural, con énfasis en Colombia y América Latina.

## Instalar y actualizar

Requiere **Python 3.9 o posterior**. Esta es una versión preliminar; puedes instalarla explícitamente:

```bash
pip install --upgrade open_corpus_co_es==0.1.1a4
```

## Consultar y descargar corpus

```bash
python -m open_corpus_co_es --list
python -m open_corpus_co_es --download presidentes
```

```python
from open_corpus_co_es import download_corpus, load_corpus

nombre = "presidentes"
download_corpus(nombre)
documentos = load_corpus(nombre)
print(len(documentos))
```

El inventario incluye publicaciones, noticias, discursos, entrevistas, recursos léxicos e indicadores. El corpus `presidentes` contiene 22 registros y está actualizado a 2026, con el registro de Abelardo de la Espriella para 2026–2030.

## Novedades de esta versión

- **Nombre simple:** el corpus RAG se descarga como `dragons_rag`; su archivo es `dragons_rag.parquet`.
- **Ejemplo inicial:** la página usa `presidentes` para mostrar la descarga y carga de un corpus.
- **Dragons RAG:** 169.248 documentos, 33 columnas y 154.477 textos únicos, procedentes de Bluesky, Media Cloud y GDELT; versión de origen 2026-10-19.
- **Presidentes:** 22 registros, incluido Abelardo de la Espriella con periodo etiquetado 2026–2030. Consulta en la auditoría las limitaciones de las etiquetas históricas originales.
- **Global Populism Database:** siete colecciones de discursos, rúbricas e indicadores, con ediciones de 2019, 2022 y 2025.
- **Educación, salud y seguridad:** las 18 combinaciones de tres temas, tres países y dos versiones, con Argentina, Colombia y México.
- **Inventario sin nombres ocultos:** las variantes Excel se identifican como `educacion_primaria_excel` y `llm_humano_excel`.
- **Integridad y carga:** validación de tamaño y SHA-256, conservación de filas con texto vacío, lectura correcta del CSV CREA y opciones CLI `--force` y `--download_all`.

## Documentación y verificación

Consulta el [inventario completo]({{ '/corpus/' | relative_url }}), el [informe de auditoría]({{ '/auditoria/' | relative_url }}), las [notas de versión]({{ '/versiones/' | relative_url }}) y la [guía de publicación]({{ '/publicacion/' | relative_url }}). Las fichas detallan los campos originales, tamaños, huellas SHA-256 y limitaciones de cada colección.

Se comprobaron las **65 descargas públicas** y la lectura completa de las **66 entradas**. El wheel y la distribución fuente publicados en PyPI coinciden con las huellas verificadas; también se probó la instalación desde PyPI. La auditoría técnica no implica que todas las etiquetas de origen estén históricamente normalizadas.

Los archivos se descargan desde Google Drive a `~/.open_corpus_co_es/data/`. No se distribuyen dentro del wheel.

Para actualizar una copia local antigua:

```python
download_corpus("presidentes", force=True)
```

El [código de la distribución publicada](https://pypi.org/project/open-corpus-co-es/0.1.1a4/#files) y sus metadatos están disponibles en PyPI.

Proyecto desarrollado por Luis Gabriel Moreno Sandoval, Pontificia Universidad Javeriana.
