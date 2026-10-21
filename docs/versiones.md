---
layout: page
title: Versiones
description: Novedades y verificación de las versiones publicadas
permalink: /versiones/
nav_order: 4
---

# Versiones publicadas

## 0.1.1a4 — 21 de octubre de 2026

**Estado: publicada y verificada en [PyPI](https://pypi.org/project/open-corpus-co-es/0.1.1a4/).**

```bash
pip install --upgrade open_corpus_co_es==0.1.1a4
```

- Identificador simplificado a `dragons_rag`; el archivo en Drive es `dragons_rag.parquet` dentro de `corpora/dragons_rag/`.
- El inventario, la documentación web, las pruebas y el catálogo usan el nombre nuevo. Los enlaces conservan los identificadores de Drive y la misma huella SHA-256.
- El ejemplo Python de la página principal usa `presidentes` como corpus inicial.
- Las 17 pruebas pasaron; `twine check --strict` aprobó los dos artefactos y se verificó la instalación directa desde PyPI.

| Artefacto publicado | SHA-256 |
|---|---|
| `open_corpus_co_es-0.1.1a4-py3-none-any.whl` | `d138581334bfe33bc84f9e2075ea08ea2706f4ec0bd547448d822b69986ddd95` |
| `open_corpus_co_es-0.1.1a4.tar.gz` | `678be2f41ba5bcbb0bf9380177d6be0f87a9fc18385dc81915776c1cebfd2971` |

## 0.1.1a3 — 21 de octubre de 2026

**Estado: publicada y verificada en [PyPI](https://pypi.org/project/open-corpus-co-es/0.1.1a3/).**
Es una versión preliminar y requiere **Python 3.9 o posterior**.

```bash
pip install --upgrade open_corpus_co_es==0.1.1a3
```

### Inventario actualizado

- 66 entradas identificables, 65 habilitadas y una deshabilitada conservada.
- Nuevo `dragons_rag_2026_10_19`: 169.248 documentos, 154.477 textos únicos y 33 columnas.
- En 0.1.1a4, el identificador se simplificó a `dragons_rag`; usa el nombre nuevo al actualizar.
- `presidentes`: actualización de 2026 con 22 registros, incluido Abelardo de la Espriella para el periodo etiquetado 2026–2030.
- Siete colecciones del Global Populism Database que ya estaban en Drive y no figuraban en el inventario.
- Variantes Excel accesibles como `educacion_primaria_excel` y `llm_humano_excel`, sin ocultar los Parquet.
- Fichas completas de formatos, campos, filas, tamaños, huellas, origen y limitaciones de todos los recursos.

### Descarga y carga

- Comprobación de tamaño y SHA-256 antes de sustituir un archivo local.
- Protección de la copia anterior cuando falla una descarga con `force=True`.
- Descargas públicas sin dependencia de cookies, con respaldo por URL directa si gdown no recupera el enlace.
- Opciones CLI `--force` y `--download_all`, con códigos de salida de error cuando corresponda.
- Selección del texto real en `Hit Sentence` y reconocimiento de otras columnas documentales y léxicas.
- Conservación de filas con texto vacío y de metadatos anidados.
- Lectura de CREA sin perder su primera fila y preservación de términos literales como `nan` y `null`.
- Lectura diferenciada de JSON y JSONL, sin omisión silenciosa de errores en `Raw_data`.
- Importación del paquete sin descargas automáticas de modelos NLTK; dependencias directas de Excel y HTTP declaradas.

### Verificación de la publicación

Se verificaron las 65 descargas públicas sin autenticación y la carga completa de
las 66 entradas. Pasaron las **17 pruebas** de la suite y `twine check --strict`.
Los dos artefactos de PyPI coinciden con los archivos auditados. Se probó una
instalación descargada directamente de PyPI, con 65 entradas habilitadas y los
22 registros de `presidentes`.

| Artefacto publicado | SHA-256 |
|---|---|
| `open_corpus_co_es-0.1.1a3-py3-none-any.whl` | `81057d6e03260b080cc2d6cd2757e053803b63e95b4188e50fc28c1d2570ef50` |
| `open_corpus_co_es-0.1.1a3.tar.gz` | `e0273ea4ba8f8831997ff95079c8babb1446c055e04d2084e04d3ad31573cdcb` |

Los corpus permanecen en Drive; no se incluyen en el wheel. La distribución fuente
publicada incluye el código, el catálogo, las pruebas, la documentación y los scripts
de auditoría correspondientes a esa publicación. Este sitio puede recibir mejoras
de documentación posteriores sin modificar los artefactos ya publicados.

### Limitaciones conocidas

Se conservan archivos idénticos publicados con distintos identificadores, filas
sin texto y etiquetas históricas de origen que necesitan revisión. La atribución
de Gaitán al periodo 1942–1946 está señalada explícitamente y no debe interpretarse
como un mandato presidencial. Los países y años heredados son etiquetas de colección,
no una certificación de cada documento. Consulta la [auditoría]({{ '/auditoria/' | relative_url }})
y el [inventario]({{ '/corpus/' | relative_url }}) antes de usar los datos.

## 0.1.1a2

Versión anterior disponible en [PyPI](https://pypi.org/project/open-corpus-co-es/0.1.1a2/).
Para obtener el inventario auditado y el nombre simplificado del corpus Dragons, actualiza a `0.1.1a4`.
