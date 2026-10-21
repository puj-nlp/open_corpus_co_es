---
layout: page
title: Auditoría
permalink: /auditoria/
nav_order: 3
---

# Auditoría de la versión 0.1.1a4

Fecha: **21 de octubre de 2026**. Consulta también el
[inventario completo]({{ '/corpus/' | relative_url }}) y la [evidencia estructurada]({{ '/auditoria_corpus.json' | relative_url }}).

## Alcance y resultados

| Comprobación | Resultado |
|---|---:|
| Entradas del inventario | 66 |
| Nombres únicos y esquemas registrados | 66 |
| Lecturas completas con cantidad de registros coincidente | 66 |
| Entradas habilitadas | 65 |
| Descargas públicas sin cookies verificadas | 65 |
| Descargas cuyo tamaño y SHA-256 coinciden con el archivo local | 65 |
| Entradas deshabilitadas conservadas | 1 |

Se inspeccionaron archivos tabulares de las carpetas `corpora` y `resource` de
la unidad compartida Corpus. Para cada entrada del inventario se verificaron
existencia, tamaño, SHA-256, esquema y lectura de registros. En Parquet se recorrieron
todos los lotes y se validaron sus estructuras. La auditoría de carga utilizó el
cargador del paquete con la configuración de cada colección. Las descargas públicas
se comprobaron de forma independiente, sin cookies de autenticación.

La entrada deshabilitada `consolidated_anew_xanew_ncr_inquirer_sel_spanish` tiene
28.491 filas y fue leída localmente. Su descarga pública no se ejecutó y su estado
heredado no se cambió automáticamente.

## Completitud del inventario

El catálogo anterior tenía 59 filas, pero dos nombres duplicados ocultaban las
variantes Excel de educación primaria y textos humanos/LLM. Se asignaron nombres
explícitos `educacion_primaria_excel` y `llm_humano_excel`; los nombres anteriores
continúan seleccionando Parquet. El cargador del catálogo rechaza futuras colisiones.

Se incorporaron las siete colecciones del Global Populism Database que ya estaban
en Drive: dos de discursos, una de rúbricas y cuatro de indicadores. Los nombres
de archivo originales se conservan aunque algunos contengan `gdp` en lugar de `gpd`.

La familia de educación, salud y seguridad contiene las 18 combinaciones esperadas
de tres temas, tres países (Argentina, Colombia y México) y dos versiones.
La cobertura histórica declarada de cada colección no implica actualización a 2026;
2026-10-21 es la fecha de esta verificación técnica.

## Calidad del texto y preservación de registros

Los registros con texto vacío se conservan con `text=""` y sus metadatos disponibles.
No se convierten sus metadatos en un texto ficticio ni se eliminan filas silenciosamente.
Los valores nulos de otros campos se omiten; los campos anidados se conservan.

| Colección | Filas sin texto en la columna seleccionada |
|---|---:|
| `perfiles_periodistas_2020` | 5.843 |
| `entrevistas_victimas_publicas_v2` | 2 |
| `edades_entrenamiento` | 104 |
| `educacion_primaria` | 1 |
| `educacion_primaria_excel` | 1 |
| `news_2020_colombia_v2` | 1 |
| `consolidated_anew_xanew_ncr_inquirer_sel_spanish` (deshabilitado) | 1.763 |

Los perfiles sin descripción conservan sus datos de cuenta. Las versiones de una
misma colección no deben sumarse como documentos independientes. La cantidad de
filas del archivo es distinta de la cantidad de textos no vacíos o textos únicos.

En las exportaciones de publicaciones, `Opening Text` estaba vacío y el texto real
estaba en `Hit Sentence`; ahora se selecciona explícitamente este último. Se reconocen
también `description`, `lyrics`, `Res` y las columnas de términos léxicos. La columna
`text` tiene prioridad sobre nombres como `text_sha256`.

CREA sin encabezado tiene 737.799 filas: la primera palabra ya no se interpreta
como encabezado. En los CSV léxicos se preservan términos literales como `nan` y
`null`, sin interpretarlos como valores ausentes.

## Archivos idénticos

Estas relaciones fueron comprobadas por SHA-256; se mantienen los identificadores
existentes para preservar compatibilidad:

- `salud_mexico_2024_v1` y `salud_mexico_2024_v2` tienen contenido binario idéntico.
- `discurso_odio` y `es_hs_project_raw_extended` tienen contenido binario idéntico.

Dragons contiene 169.248 documentos con identificadores únicos y 154.477 textos
únicos. Las 14.771 filas con texto repetido se conservan y están declaradas en el
manifiesto de procedencia.

## Presidentes y límites históricos

Se verificaron 22 registros, incluido Abelardo de la Espriella con periodo etiquetado
2026–2030 y texto no vacío. El catálogo anterior lo describía como un corpus de 2023;
se corrigió a una actualización de 2026. El final del periodo no significa que
se hayan recopilado discursos futuros hasta 2030. La fecha de modificación del
archivo en Drive es 2026-08-12 y la fecha de verificación es 2026-10-21.

La [Presidencia de la República](https://www.presidencia.gov.co/contenidoVinculado/perfiles/presidente.html)
identifica a Abelardo de la Espriella para el periodo 2026–2030.

La fila `1942_1946_jorge_eliecer_gaitan.txt` tiene una atribución de mandato
inconsistente. El [Banco de la República](https://enciclopedia.banrepcultural.org/index.php/Alfonso_L%C3%B3pez_Pumarejo)
sitúa a Alfonso López Pumarejo en la presidencia durante 1942–1945. Se conserva el
registro original con una advertencia en el catálogo. Este corpus es una selección
de discursos políticos, no una lista exhaustiva o históricamente normalizada de mandatos.

## Archivos fuera del catálogo y límites de la auditoría

El archivo auxiliar `corpora/general/age_tweets_all.csv`, que no forma parte del
inventario publicado, falló la lectura por comillas o delimitadores inconsistentes.
No se añadió al catálogo. Las versiones de archivo antiguas, los ZIP históricos,
los archivos temporales de Office y los recursos PDF/RDF no se habilitaron como
colecciones tabulares nuevas.

Los años y países de las colecciones heredadas se documentan como declarados,
porque los archivos no siempre contienen evidencia suficiente para verificarlos
documento por documento. Tampoco se certifican autoría, exactitud de afirmaciones,
representatividad, licencias de las fuentes o ausencia de información personal.
La licencia MIT cubre el código del paquete.

## Cambios funcionales verificados

- Descargas contrastadas con tamaño y SHA-256 antes de reemplazar el archivo local.
- Una descarga fallida con `force=True` conserva la versión anterior.
- Se detectan copias locales antiguas y se indica cómo actualizarlas con `force=True`.
- Las descargas de este inventario público no dependen de cookies locales de Google.
- Las opciones CLI `--force` y `--download_all` funcionan y comunican fallos con un código de salida distinto de cero.
- No se descargan modelos de NLTK al importar el paquete.
- JSON y JSONL se leen según su estructura y los errores de `Raw_data` no se descartan silenciosamente.
- Excel declara la dependencia `openpyxl`; `requests` también es una dependencia directa.
- La versión tiene una sola definición en `pyproject.toml` y requiere Python 3.9 o posterior.

## Publicación verificada

La versión **[0.1.1a4](https://pypi.org/project/open-corpus-co-es/0.1.1a4/)** se publicó
en PyPI el **21 de octubre de 2026**. Se comprobaron los dos artefactos publicados
contra sus huellas locales y se instaló el wheel directamente desde PyPI en una
carpeta aislada. La instalación devolvió 65 entradas habilitadas y cargó los
22 registros de `presidentes`, incluido Abelardo con `fecha_inicio=2026`.

La suite completa terminó con **17 pruebas aprobadas** y ambos artefactos superaron
`twine check --strict`. Consulta las [notas de versión]({{ '/versiones/' | relative_url }})
para las huellas de los archivos publicados.
