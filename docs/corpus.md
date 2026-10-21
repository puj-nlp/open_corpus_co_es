---
layout: page
title: Corpus
description: Referencia completa del catálogo auditado de Open Corpus CO-ES
permalink: /corpus/
nav_order: 2
---

# Inventario completo

Actualización: **2026-10-21**. Versión **[0.1.1a3 publicada en PyPI](https://pypi.org/project/open-corpus-co-es/0.1.1a3/)**. **66 entradas: 65 habilitadas y una deshabilitada**.

El nombre de la primera columna es el identificador para `download_corpus()` y `load_corpus()`. Los archivos tabulares se cargan como listas de diccionarios; la columna textual configurada se expone como `text`. Si no hay columna textual, se representan los campos de la fila como texto. Las etiquetas de país y año son metadatos heredados de la colección, salvo las actualizaciones documentadas; no son una validación geográfica o temporal de cada documento.

Los tamaños, huellas, esquemas y cantidades de filas corresponden a archivos inspeccionados. Se verificó la descarga anónima de las **65 entradas habilitadas** y su coincidencia SHA-256 con Drive.

## Resumen

| Nombre | Estado | Formato | Filas | Columnas | País declarado | Año/edición | Tema |
|---|---|---|---:|---:|---|---:|---|
| `dragons_rag_2026_10_19` | Habilitado | parquet | 169248 | 33 | Multipaís | 2026 | Noticias y redes sociales para RAG |
| `dataset_bancos_2022` | Habilitado | parquet | 38952 | 3 | Colombia | 2022 | Financiero |
| `perfiles_periodistas_2020` | Habilitado | parquet | 14030 | 8 | Colombia | 2020 | Perfiles |
| `tweets_miscelaneos_2020` | Habilitado | parquet | 95678 | 6 | Colombia | 2020 | Tweets |
| `educacion_argentina_2024_v2` | Habilitado | parquet | 20000 | 51 | Argentina | 2024 | Educación |
| `educacion_argentina_2024_v1` | Habilitado | parquet | 20000 | 51 | Argentina | 2024 | Educación |
| `educacion_colombia_2024_v2` | Habilitado | parquet | 20000 | 51 | Colombia | 2024 | Educación |
| `educacion_colombia_2024_v1` | Habilitado | parquet | 20000 | 51 | Colombia | 2024 | Educación |
| `educacion_mexico_2024_v2` | Habilitado | parquet | 20000 | 51 | México | 2024 | Educación |
| `educacion_mexico_2024_v1` | Habilitado | parquet | 20000 | 51 | México | 2024 | Educación |
| `salud_argentina_2024_v2` | Habilitado | parquet | 20000 | 51 | Argentina | 2024 | Salud |
| `salud_argentina_2024_v1` | Habilitado | parquet | 20000 | 51 | Argentina | 2024 | Salud |
| `salud_colombia_2024_v1` | Habilitado | parquet | 20000 | 51 | Colombia | 2024 | Salud |
| `salud_colombia_2024_v2` | Habilitado | parquet | 20000 | 51 | Colombia | 2024 | Salud |
| `salud_mexico_2024_v1` | Habilitado | parquet | 20000 | 51 | México | 2024 | Salud |
| `salud_mexico_2024_v2` | Habilitado | parquet | 20000 | 51 | México | 2024 | Salud |
| `seguridad_argentina_2024_v2` | Habilitado | parquet | 20000 | 51 | Argentina | 2024 | Seguridad |
| `seguridad_argentina_2024_v1` | Habilitado | parquet | 20000 | 51 | Argentina | 2024 | Seguridad |
| `seguridad_colombia_2024_v2` | Habilitado | parquet | 20000 | 51 | Colombia | 2024 | Seguridad |
| `seguridad_colombia_2024_v1` | Habilitado | parquet | 20000 | 51 | Colombia | 2024 | Seguridad |
| `seguridad_mexico_2024_v2` | Habilitado | parquet | 20000 | 51 | México | 2024 | Seguridad |
| `seguridad_mexico_2024_v1` | Habilitado | parquet | 20000 | 51 | México | 2024 | Seguridad |
| `entrevistas_victimas_publicas_v2` | Habilitado | parquet | 2486 | 3 | Colombia | 2020 | Entrevistas |
| `rag_processed_data` | Habilitado | parquet | 73560 | 7 | Colombia | 2020 | Entrevistas |
| `presidentes` | Habilitado | parquet | 22 | 5 | Colombia | 2026 | Presidentes |
| `edades_entrenamiento` | Habilitado | parquet | 169336 | 2 | Colombia | 2016 | Edades |
| `musica_metrica` | Habilitado | parquet | 17996 | 17 | Colombia | 2020 | Música |
| `musica_letra` | Habilitado | parquet | 3759 | 7 | Colombia | 2020 | Música |
| `educacion_primaria_excel` | Habilitado | xlsx | 342 | 5 | Colombia | 2024 | Educación |
| `llm_humano_excel` | Habilitado | xlsx | 1844 | 3 | Colombia | 2023 | LLM |
| `es_hs_project_raw_extended` | Habilitado | parquet | 915939 | 8 | Colombia | 2023 | Discurso de odio |
| `es_hs_project_raw_extended_v2` | Habilitado | parquet | 4950 | 5 | Colombia | 2023 | Discurso de odio |
| `educacion_primaria` | Habilitado | parquet | 342 | 5 | Colombia | 2024 | Educación |
| `llm_humano` | Habilitado | parquet | 1844 | 3 | Colombia | 2023 | LLM |
| `discurso_odio` | Habilitado | parquet | 915939 | 8 | Colombia | 2023 | Discurso de odio |
| `ods` | Habilitado | parquet | 17 | 2 | Colombia | 2020 | ODS |
| `laudato_si` | Habilitado | parquet | 14 | 3 | Colombia | 2020 | Religión |
| `news_2020_peru_v2` | Habilitado | parquet | 26711 | 3 | Perú | 2020 | Noticias |
| `news_2020_colombia_v2` | Habilitado | parquet | 17513 | 3 | Colombia | 2020 | Noticias |
| `news_2020_ecuador_v2` | Habilitado | parquet | 20032 | 3 | Ecuador | 2020 | Noticias |
| `consolidated_anew_xanew_ncr_inquirer_sel_spanish` | Deshabilitado | xlsx | 28491 | 25 | Colombia | 2020 | NCR y otros léxicos afectivos |
| `lexicon_tic` | Habilitado | xlsx | 457 | 3 | Colombia | 2020 | TIC |
| `lexicon_actors_roles` | Habilitado | csv | 7983 | 3 | Colombia | 2020 | Roles |
| `lexicon_actors_roles_excel_v2` | Habilitado | xlsx | 7983 | 3 | Colombia | 2020 | Roles |
| `lexicon_afectivo_categorias` | Habilitado | csv | 6625 | 3 | Colombia | 2020 | Afectivo |
| `lexicon_afectivo_categorias_v2` | Habilitado | xlsx | 6625 | 3 | Colombia | 2020 | Afectivo |
| `lexicon_duelo_completa` | Habilitado | xlsx | 376 | 8 | Colombia | 2020 | Duelo |
| `lexicon_ejecuciones_extrajudiciales` | Habilitado | xlsx | 338 | 6 | Colombia | 2020 | Guerra |
| `lexicon_estigmatizacion` | Habilitado | xlsx | 111 | 5 | Colombia | 2020 | Guerra |
| `lexicon_ministers` | Habilitado | csv | 2408 | 3 | Colombia | 2020 | Gobierno |
| `lexicon_ministers_v2` | Habilitado | xlsx | 2408 | 3 | Colombia | 2020 | Gobierno |
| `lexicon_referencia_crea` | Habilitado | csv | 737799 | 3 | Colombia | 2020 | RAE |
| `lexicon_referencia_creav_2` | Habilitado | csv | 737799 | 3 | Colombia | 2020 | RAE |
| `lexicon_relations_verbs` | Habilitado | csv | 308 | 2 | Colombia | 2020 | Verbos |
| `lexicon_relations_verbs_v2` | Habilitado | xlsx | 308 | 2 | Colombia | 2020 | Verbos |
| `lexicon_sevicia` | Habilitado | csv | 190 | 2 | Colombia | 2020 | Sevicia |
| `lexicon_verbos_sentencias_tierras` | Habilitado | csv | 236 | 2 | Colombia | 2020 | Guerra |
| `lexicon_verbos_sentencias_tierras_v2` | Habilitado | xlsx | 236 | 2 | Colombia | 2020 | Guerra |
| `tesauro_cev_v2` | Habilitado | xlsx | 12341 | 8 | Colombia | 2020 | CEV |
| `gpd_20190625` | Habilitado | parquet | 4464 | 18 | Multipaís | 2019 | Indicadores de populismo |
| `gpd_v2_1_20251120` | Habilitado | parquet | 5552 | 19 | Multipaís | 2025 | Indicadores de populismo |
| `gpd_v2_1_20251120_wide` | Habilitado | parquet | 361 | 37 | Multipaís | 2025 | Indicadores de populismo |
| `gpd_v2_20220427` | Habilitado | parquet | 4960 | 19 | Multipaís | 2022 | Indicadores de populismo |
| `gpd_rubrics_20251120` | Habilitado | parquet | 156 | 7 | Multipaís | 2025 | Rúbricas de populismo |
| `gpd_speeches_20220427` | Habilitado | parquet | 1161 | 7 | Multipaís | 2022 | Discursos políticos internacionales |
| `gpd_speeches_20251120` | Habilitado | parquet | 1310 | 7 | Multipaís | 2025 | Discursos políticos internacionales |

## Uso

```bash
python -m open_corpus_co_es --download presidentes
python -m open_corpus_co_es --download presidentes --force
```

```python
from open_corpus_co_es import download_corpus, load_corpus

download_corpus("presidentes")
documentos = load_corpus("presidentes")
print(documentos[-1]["nombre"])
```

## Presidentes: actualización de 2026

El parquet contiene **22 registros y cinco campos**: `fecha_inicio`, `fecha_fin`, `nombre`, `archivo` y `text`. Incluye el texto de Abelardo de la Espriella con periodo etiquetado **2026–2030**. El archivo de Drive fue modificado el 12 de agosto de 2026; se verificó su contenido y descarga el 21 de octubre de 2026. Esto no implica que el corpus incluya todos los discursos hasta octubre ni textos futuros de 2030.

La [Presidencia de la República](https://www.presidencia.gov.co/contenidoVinculado/perfiles/presidente.html) identifica a Abelardo de la Espriella para el periodo 2026–2030.

**Limitación histórica:** la fila `1942_1946_jorge_eliecer_gaitan.txt` contiene un discurso de Gaitán y no representa un mandato presidencial suyo. Las fuentes del [Banco de la República](https://enciclopedia.banrepcultural.org/index.php/Alfonso_L%C3%B3pez_Pumarejo) identifican a Alfonso López Pumarejo como presidente en 1942–1945. Se conserva el texto y la etiqueta original para no alterar silenciosamente los datos. El conjunto es una selección de discursos políticos, no una nómina histórica exhaustiva.

## Dragons RAG

Versión de origen **2026-10-19**, generada el 21 de octubre de 2026: **169.248 documentos**, **154.477 textos únicos** y **33 columnas**. Fuentes: Bluesky (64.670), Media Cloud (103.380) y GDELT (1.198). Conserva texto original y metadatos, sin fragmentación ni embeddings. Se conservan 14.771 filas con texto repetido. El manifiesto de procedencia está junto al parquet en Drive; no forma parte de la lista de documentos cargados.

## Relaciones entre colecciones

- `educacion_primaria` y `educacion_primaria_excel` ofrecen formatos Parquet y Excel de una colección de 342 filas.
- `llm_humano` y `llm_humano_excel` ofrecen formatos Parquet y Excel de una colección de 1.844 filas.
- `salud_mexico_2024_v1` y `salud_mexico_2024_v2` tienen la misma huella SHA-256.
- `discurso_odio` y `es_hs_project_raw_extended` también tienen la misma huella SHA-256.
- CREA sin encabezado y CREA v2 con encabezado tienen 737.799 registros cada uno. La carga de la primera versión configura explícitamente los nombres de columna y conserva su primera fila.
- Los indicadores GPD en formato largo y ancho tienen granularidades diferentes: sus cantidades de filas no son directamente comparables con los discursos.
- `consolidated_anew_xanew_ncr_inquirer_sel_spanish` continúa deshabilitado por la configuración heredada. La lectura local fue comprobada; no se incluye entre las 65 descargas verificadas ni en `list_corpus()`.

## Fichas de todas las entradas

Los registros con texto vacío se conservan con sus metadatos. Los conteos de filas sin texto, los problemas de origen y la política de lectura de términos literales como `nan` y `null` se detallan en la [auditoría]({{ '/auditoria/' | relative_url }}). Una fila no equivale necesariamente a un texto no vacío o único.

### `dragons_rag_2026_10_19`

Dragons - Corpus documental para RAG de Bluesky, Media Cloud y GDELT, versión del 2026-10-19. Conserva el texto original y sus metadatos, sin fragmentación ni embeddings.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `dragons`.
- Formato: `parquet`. Filas: **169248**. Columnas: **33**. Tamaño: **256941261 bytes**.
- País declarado: Multipaís. Año/edición declarada: 2026.
- Texto: columna `text`.
- Archivo: [dragons_rag_2026_10_19.parquet](https://drive.google.com/file/d/1JN8PhSXiUoeE45bBDOpfNyvNicLO2GQn/view?usp=drivesdk). Ruta de Drive: `corpora/dragons/dragons_rag_2026_10_19.parquet`.
- SHA-256: `f4a669f17eaedd357f72b70c2192e685b6d534a94f6ffaeadbced7290b181728`.

Campos originales: `document_id`, `text`, `collection_name`, `title`, `url`, `source`, `source_type`, `language`, `country_key`, `created_at`, `synced_at`, `mongo_id`, `strategy`, `url_domain`, `final_url`, `language_base`, `publisher`, `author_id`, `author_name`, `author_handle`, `uri`, `section`, `event_id`, `event_context`, `keyword_family`, `collection_keyword`, `collection_keyword_label`, `collection_query`, `keyword_matches`, `top_terms`, `word_count`, `char_count`, `text_sha256`.

### `dataset_bancos_2022`

Financiero - Conjunto de datos de origen 'Tweets' generado en Colombia durante el año 2022.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **38952**. Columnas: **3**. Tamaño: **23507060 bytes**.
- País declarado: Colombia. Año/edición declarada: 2022.
- Texto: objetos de `Raw_data`.
- Archivo: [dataset_bancos_2022.parquet](https://drive.google.com/file/d/1jbgbBti6X8l1bqsQTx3gT7vvQ0Qx-pN1/view?usp=sharing). Ruta de Drive: `corpora/tweets/dataset_bancos_2022.parquet`.
- SHA-256: `343e272ad2e97ba756b9772ef26a5e3f2735bf456f6f6c31b8a8e42f848f94a6`.

Campos originales: `Id`, `Raw_data`, `URLs_img`.

### `perfiles_periodistas_2020`

Perfiles - Conjunto de datos de origen 'Tweets' generado en Colombia durante el año 2020.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **14030**. Columnas: **8**. Tamaño: **1137076 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `description`.
- Archivo: [perfiles_periodistas_2020.parquet](https://drive.google.com/file/d/1i9BGSDHudVJzTehLPHF-WTyVZ7lwRr39/view?usp=sharing). Ruta de Drive: `corpora/tweets/perfiles_periodistas_2020.parquet`.
- SHA-256: `65041c76d9b470bd6398adc05c3f112e77ccb2374d2302e91a8f763be8697637`.

Campos originales: `_id`, `description`, `favourites_count`, `followers_count`, `following`, `id`, `profile_image_url`, `screen_name`.

### `tweets_miscelaneos_2020`

Tweets - Conjunto de datos de origen 'Tweets' generado en Colombia durante el año 2020.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **95678**. Columnas: **6**. Tamaño: **8282159 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `text`.
- Archivo: [tweets_miscelaneos_2020.parquet](https://drive.google.com/file/d/1f9nosxazk_fIoxRGwj8pgPKPyi2De7na/view?usp=sharing). Ruta de Drive: `corpora/tweets/tweets_miscelaneos_2020.parquet`.
- SHA-256: `db6738d9e3ad8d6dffba547131b739a5b4ae1183fdb53b9c247063c49e8cad24`.

Campos originales: `_id`, `user.id`, `id`, `user.name`, `text`, `user.screen_name`.

### `educacion_argentina_2024_v2`

Publicaciones sobre educación de Argentina, colección v2 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **8598117 bytes**.
- País declarado: Argentina. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [educacion_argentina_2024_v2.parquet](https://drive.google.com/file/d/1YBHahypClBqXLy2oy7H_2-Kr-ovPh8fR/view?usp=sharing). Ruta de Drive: `corpora/tweets/educacion_argentina_2024_v2.parquet`.
- SHA-256: `4e1410756079e53addb3118ebc05457cefce140a9080de2c2c85ec52b7f93e04`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `educacion_argentina_2024_v1`

Publicaciones sobre educación de Argentina, colección v1 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **8010142 bytes**.
- País declarado: Argentina. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [educacion_argentina_2024_v1.parquet](https://drive.google.com/file/d/1QmEd42nujxCgXBedXqH7y5frelG3syfv/view?usp=sharing). Ruta de Drive: `corpora/tweets/educacion_argentina_2024_v1.parquet`.
- SHA-256: `7312670cd5b07ffec995bcfd11ee2476267a13e6313cdef603b1e287edc39a3d`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `educacion_colombia_2024_v2`

Publicaciones sobre educación de Colombia, colección v2 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **7993194 bytes**.
- País declarado: Colombia. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [educacion_colombia_2024_v2.parquet](https://drive.google.com/file/d/1U_fDLS-LArqyMMavvXhj1d2pEID-7yf3/view?usp=sharing). Ruta de Drive: `corpora/tweets/educacion_colombia_2024_v2.parquet`.
- SHA-256: `5db75f8fec2c4da818a93be404881b89c2e6773a89963ea2dd88d31e9bce9a7b`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `educacion_colombia_2024_v1`

Publicaciones sobre educación de Colombia, colección v1 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **8862425 bytes**.
- País declarado: Colombia. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [educacion_colombia_2024_v1.parquet](https://drive.google.com/file/d/1dSD9pxU0o_uW6y_3Puhl3leO08DjPS7m/view?usp=sharing). Ruta de Drive: `corpora/tweets/educacion_colombia_2024_v1.parquet`.
- SHA-256: `eeba8524301ae39d17a93a01b02b5cd8128b1f6bb945e84ffbd22535cf53bb61`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `educacion_mexico_2024_v2`

Publicaciones sobre educación de México, colección v2 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **8932946 bytes**.
- País declarado: México. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [educacion_mexico_2024_v2.parquet](https://drive.google.com/file/d/1NqTdWC-jRjTnFJ0nG7rld-D88nHOXMag/view?usp=sharing). Ruta de Drive: `corpora/tweets/educacion_mexico_2024_v2.parquet`.
- SHA-256: `8b1e2021867d0953f2c2d49e7be00a76315554a3dc36d35343357db03f6cf957`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `educacion_mexico_2024_v1`

Publicaciones sobre educación de México, colección v1 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **8084169 bytes**.
- País declarado: México. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [educacion_mexico_2024_v1.parquet](https://drive.google.com/file/d/1AYMzykPKo_0D7feL6z-sS_8axwvLftjB/view?usp=sharing). Ruta de Drive: `corpora/tweets/educacion_mexico_2024_v1.parquet`.
- SHA-256: `7482308a806a9faf4cfd83e95f26789fef6a749eb21d7ebbe69c0089a4ad6865`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `salud_argentina_2024_v2`

Publicaciones sobre salud de Argentina, colección v2 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **8073488 bytes**.
- País declarado: Argentina. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [salud_argentina_2024_v2.parquet](https://drive.google.com/file/d/1lqmUyj_80bVJDYSB8a4mO1dVHGv_5Ms2/view?usp=sharing). Ruta de Drive: `corpora/tweets/salud_argentina_2024_v2.parquet`.
- SHA-256: `2525c1b0fea12e146eed1d359d94aa4b0a372b637d5f4ed5e89186bb76c2c7aa`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `salud_argentina_2024_v1`

Publicaciones sobre salud de Argentina, colección v1 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **8569165 bytes**.
- País declarado: Argentina. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [salud_argentina_2024_v1.parquet](https://drive.google.com/file/d/16mnSTooxOJFShxNBNRb9McB3UwZyNQ-S/view?usp=sharing). Ruta de Drive: `corpora/tweets/salud_argentina_2024_v1.parquet`.
- SHA-256: `9e2dc890d84d91d96aedb32905f21d05bbdfbf8af532dabdfb6bb8f4d09dd55f`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `salud_colombia_2024_v1`

Publicaciones sobre salud de Colombia, colección v1 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **7250146 bytes**.
- País declarado: Colombia. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [salud_colombia_2024_v1.parquet](https://drive.google.com/file/d/1zTeFuZQDeU95UYpchqwuWP_XrWNL6333/view?usp=sharing). Ruta de Drive: `corpora/tweets/salud_colombia_2024_v1.parquet`.
- SHA-256: `1dbf016f647cdde4d2c0b9110dc538799d2d0fd8ab0534fa6c29965956087b14`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `salud_colombia_2024_v2`

Publicaciones sobre salud de Colombia, colección v2 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **8614658 bytes**.
- País declarado: Colombia. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [salud_colombia_2024_v2.parquet](https://drive.google.com/file/d/19g_sjz8dYPjdX9eiae_y9zJ5-LcBGCPY/view?usp=sharing). Ruta de Drive: `corpora/tweets/salud_colombia_2024_v2.parquet`.
- SHA-256: `3a09c9832817de94b06b6e3b8228fc605909542591e700dc5a4c52752112a25e`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `salud_mexico_2024_v1`

Publicaciones sobre salud de México, colección v1 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **8847155 bytes**.
- País declarado: México. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [salud_mexico_2024_v1.parquet](https://drive.google.com/file/d/181apcxcMP3QEjeZwgZKfGoj1F7DxAvge/view?usp=sharing). Ruta de Drive: `corpora/tweets/salud_mexico_2024_v1.parquet`.
- SHA-256: `6bd8fb71e46ad9c706434d813dd35e871a177a2e68ea6894e3c28cf38bfaaa3f`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

**Observación:** Las versiones v1 y v2 tienen contenido binario idéntico en esta auditoría.

### `salud_mexico_2024_v2`

Publicaciones sobre salud de México, colección v2 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **8847155 bytes**.
- País declarado: México. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [salud_mexico_2024_v2.parquet](https://drive.google.com/file/d/1JhABswU1YuXK-HGghBOYn7orEXpxR0TZ/view?usp=sharing). Ruta de Drive: `corpora/tweets/salud_mexico_2024_v2.parquet`.
- SHA-256: `6bd8fb71e46ad9c706434d813dd35e871a177a2e68ea6894e3c28cf38bfaaa3f`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

**Observación:** Las versiones v1 y v2 tienen contenido binario idéntico en esta auditoría.

### `seguridad_argentina_2024_v2`

Publicaciones sobre seguridad de Argentina, colección v2 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **8993076 bytes**.
- País declarado: Argentina. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [seguridad_argentina_2024_v2.parquet](https://drive.google.com/file/d/1xvdb5hFvHiwPhyrtMacrv_s3F5vrWAIh/view?usp=sharing). Ruta de Drive: `corpora/tweets/seguridad_argentina_2024_v2.parquet`.
- SHA-256: `6d302fabeb8f5a03381a9b3d3f275302b90190019cd33d0894f4a82fbf4c663b`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `seguridad_argentina_2024_v1`

Publicaciones sobre seguridad de Argentina, colección v1 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **7837451 bytes**.
- País declarado: Argentina. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [seguridad_argentina_2024_v1.parquet](https://drive.google.com/file/d/1-_zhV_uBo64Plomg06aVDmmHzgxTnYsg/view?usp=sharing). Ruta de Drive: `corpora/tweets/seguridad_argentina_2024_v1.parquet`.
- SHA-256: `1e7011770e69832f308ab23671e10ff978f32be421cb78e28baf6f75de0233a0`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `seguridad_colombia_2024_v2`

Publicaciones sobre seguridad de Colombia, colección v2 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **7774342 bytes**.
- País declarado: Colombia. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [seguridad_colombia_2024_v2.parquet](https://drive.google.com/file/d/1EroZiA6zUdOZhi1TKO5QNilxC-uMhooD/view?usp=sharing). Ruta de Drive: `corpora/tweets/seguridad_colombia_2024_v2.parquet`.
- SHA-256: `fe907321759e77a9cdd0a04b12924945949ad97f30d06a288e456ad617d6acc8`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `seguridad_colombia_2024_v1`

Publicaciones sobre seguridad de Colombia, colección v1 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **9138489 bytes**.
- País declarado: Colombia. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [seguridad_colombia_2024_v1.parquet](https://drive.google.com/file/d/13mIKM-5QVQgnhAxP8fgSabr5UT9Mol1W/view?usp=sharing). Ruta de Drive: `corpora/tweets/seguridad_colombia_2024_v1.parquet`.
- SHA-256: `88525c4045c197c498ad93ab6bafbcbd136ef83e97b176cce4bc3b0834bbda98`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `seguridad_mexico_2024_v2`

Publicaciones sobre seguridad de México, colección v2 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **8956926 bytes**.
- País declarado: México. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [seguridad_mexico_2024_v2.parquet](https://drive.google.com/file/d/1NYQj-cp1suS7niea08oMreff2brN9vBQ/view?usp=sharing). Ruta de Drive: `corpora/tweets/seguridad_mexico_2024_v2.parquet`.
- SHA-256: `4fe201c9c3c48c84f9e1b4a9465d112f0df86bbb9698e2d85999e0af81cf7301`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `seguridad_mexico_2024_v1`

Publicaciones sobre seguridad de México, colección v1 declarada de 2024; texto en Hit Sentence y metadatos de la exportación.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `tweets`.
- Formato: `parquet`. Filas: **20000**. Columnas: **51**. Tamaño: **7815913 bytes**.
- País declarado: México. Año/edición declarada: 2024.
- Texto: columna `Hit Sentence`.
- Archivo: [seguridad_mexico_2024_v1.parquet](https://drive.google.com/file/d/1b1JzBYXqGijIfcZUKzUiZDuzQIKlJJsV/view?usp=sharing). Ruta de Drive: `corpora/tweets/seguridad_mexico_2024_v1.parquet`.
- SHA-256: `82d05b96727d8c1687e50a901a3a4d058b3caf464078215cf6bc8a041c12a347`.

Campos originales: `Date`, `Headline`, `URL`, `Opening Text`, `Hit Sentence`, `Source`, `Influencer`, `Country`, `Subregion`, `Language`, `Reach`, `Desktop Reach`, `Mobile Reach`, `Twitter Social Echo`, `Facebook Social Echo`, `Reddit Social Echo`, `National Viewership`, `Engagement`, `AVE`, `Sentiment`, `Key Phrases`, `Input Name`, `Keywords`, `Twitter Authority`, `Tweet Id`, `Twitter Id`, `Twitter Client`, `Twitter Screen Name`, `User Profile Url`, `Twitter Bio`, `Twitter Followers`, `Twitter Following`, `Alternate Date Format`, `Time`, `State`, `City`, `Social Echo Total`, `Editorial Echo`, `Views`, `Estimated Views`, `Likes`, `Replies`, `Retweets`, `Comments`, `Shares`, `Reactions`, `Threads`, `Is Verified`, `Parent URL`, `Document Tags`, `Document ID`.

### `entrevistas_victimas_publicas_v2`

Entrevistas - Conjunto de datos de origen 'Cev' generado en Colombia durante el año 2020.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `cev`.
- Formato: `parquet`. Filas: **2486**. Columnas: **3**. Tamaño: **114364610 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `text`.
- Archivo: [entrevistas_victimas_publicas_v2.parquet](https://drive.google.com/file/d/1zBtJ6fM6ypjhWd64OWH5lThhk-aMQjl3/view?usp=sharing). Ruta de Drive: `corpora/cev/entrevistas_victimas_publicas_v2.parquet`.
- SHA-256: `38218574c96a18126c453f7a098c24a03d75ad4428861b5a7509ca56d7bfcc51`.

Campos originales: `id_doc`, `pages`, `text`.

### `rag_processed_data`

Entrevistas - Conjunto de datos de origen 'Cev' generado en Colombia durante el año 2020.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `cev`.
- Formato: `parquet`. Filas: **73560**. Columnas: **7**. Tamaño: **107551016 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Text`.
- Archivo: [rag_processed_data.parquet](https://drive.google.com/file/d/1d1KVuHx3LhKwYPaJpMAXR2S36_NSl-Rg/view?usp=sharing). Ruta de Drive: `corpora/cev/rag_processed_data.parquet`.
- SHA-256: `704404c74e62af9661aa6677bcef6c9f81ac39d31c1b00a79225549bfec5b223`.

Campos originales: `ID`, `Title`, `Text`, `Page`, `Type`, `Original_Title`, `Link`.

### `presidentes`

Discursos políticos de Colombia: 22 registros, actualización de 2026 con Abelardo de la Espriella (2026–2030). Las etiquetas históricas originales incluyen una atribución inconsistente de Jorge Eliécer Gaitán al periodo 1942–1946.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `parquet`. Filas: **22**. Columnas: **5**. Tamaño: **401268 bytes**.
- País declarado: Colombia. Año/edición declarada: 2026.
- Texto: columna `text`.
- Archivo: [presidentes.parquet](https://drive.google.com/file/d/1pet4pUKKFoOtdunF2uaNxhwtYZIg-vg8/view?usp=sharing). Ruta de Drive: `corpora/general/presidentes.parquet`.
- SHA-256: `69e2e61340b65e698c0a571b3c6b3de2530ed7488548bfe001de34d2706084ab`.

Campos originales: `fecha_inicio`, `fecha_fin`, `nombre`, `archivo`, `text`.

**Observación:** La fila de Jorge Eliécer Gaitán no corresponde a un mandato presidencial de 1942–1946. Se conserva el dato de origen; este corpus no es un registro histórico exhaustivo de presidentes.

**Observación:** 2030 es el final del periodo etiquetado, no la fecha de actualización del corpus.

### `edades_entrenamiento`

Edades - Conjunto de datos de origen 'General' generado en Colombia durante el año 2016.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `parquet`. Filas: **169336**. Columnas: **2**. Tamaño: **13043498 bytes**.
- País declarado: Colombia. Año/edición declarada: 2016.
- Texto: columna `text`.
- Archivo: [edades_entrenamiento.parquet](https://drive.google.com/file/d/1fZ9DBXf2QAY0VrmtvtVnsdNCFxQAQbuD/view?usp=sharing). Ruta de Drive: `corpora/general/edades_entrenamiento.parquet`.
- SHA-256: `0208cc6f68cac3951d05a30678f097b69c0944ce6a8f3084fb20914a9a5596d2`.

Campos originales: `text`, `age_range`.

### `musica_metrica`

Musica - Conjunto de datos de origen 'General' generado en Colombia durante el año 2020.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `parquet`. Filas: **17996**. Columnas: **17**. Tamaño: **1047081 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: representación de los campos de cada fila.
- Archivo: [musica_metrica.parquet](https://drive.google.com/file/d/1bX32Q48lOBn9ixbWbEHrlf9Oj8tZv_JL/view?usp=sharing). Ruta de Drive: `corpora/general/musica_metrica.parquet`.
- SHA-256: `fbe23f81524da70c4da6a1dcec9e050970cd985eba67a193925908f7aba80975`.

Campos originales: `Artist Name`, `Track Name`, `Popularity`, `danceability`, `energy`, `key`, `loudness`, `mode`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo`, `duration_in min/ms`, `time_signature`, `Class`.

### `musica_letra`

Musica - Conjunto de datos de origen 'General' generado en Colombia durante el año 2020.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `parquet`. Filas: **3759**. Columnas: **7**. Tamaño: **2870680 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `lyrics`.
- Archivo: [musica_letra.parquet](https://drive.google.com/file/d/12DBuTWIzuvkOPsb-duOqQ7yPKv9svSEV/view?usp=sharing). Ruta de Drive: `corpora/general/musica_letra.parquet`.
- SHA-256: `f37a56130cb01d8ed97f79396af41a3a17b75370e0be3fb713fecb581886d368`.

Campos originales: `url`, `title`, `artists`, `language`, `lyrics`, `id`, `genre`.

### `educacion_primaria_excel`

Educacion - Conjunto de datos de origen 'General' generado en Colombia durante el año 2024.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `xlsx`. Filas: **342**. Columnas: **5**. Tamaño: **27357 bytes**.
- País declarado: Colombia. Año/edición declarada: 2024.
- Texto: columna `Res`.
- Archivo: [educacion_primaria.xlsx](https://docs.google.com/spreadsheets/d/1JQ_lrA0ZucADg2C3POPbRsGBje7Lyw9W/edit?usp=sharing&ouid=107072219928073180472&rtpof=true&sd=true). Ruta de Drive: `corpora/general/educacion_primaria.xlsx`.
- SHA-256: `5b635b8e4a2244955c469986a0ec06b9ac5626793ce36bba54d967f45db83668`.

Campos originales: `ID`, `CUESTIONARIO`, `NUM`, `Preg`, `Res`.

### `llm_humano_excel`

Llm - Conjunto de datos de origen 'General' generado en Colombia durante el año 2023.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `xlsx`. Filas: **1844**. Columnas: **3**. Tamaño: **1096041 bytes**.
- País declarado: Colombia. Año/edición declarada: 2023.
- Texto: columna `Texto`.
- Archivo: [llm_humano.xlsx](https://docs.google.com/spreadsheets/d/1Aiv3wjPvDqpSrkQrRuDrGpCLcvv8h_t7/edit?usp=sharing&ouid=107072219928073180472&rtpof=true&sd=true). Ruta de Drive: `corpora/general/llm_humano.xlsx`.
- SHA-256: `7674faf4410929ebcf017e3e1182e264d3e84dea610fbf6eb1ff0e0436cb116f`.

Campos originales: `Texto`, `Tipo de fuente`, `Clasificacion`.

### `es_hs_project_raw_extended`

Odio - Conjunto de datos de origen 'General' generado en Colombia durante el año 2023.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `parquet`. Filas: **915939**. Columnas: **8**. Tamaño: **56487561 bytes**.
- País declarado: Colombia. Año/edición declarada: 2023.
- Texto: columna `text`.
- Archivo: [es_hs_project_raw_extended.parquet](https://drive.google.com/file/d/1mbCovIeVJ4eXjL-aclzy3AXQwL2jmbYY/view?usp=sharing). Ruta de Drive: `corpora/general/es_hs_project_raw_extended.parquet`.
- SHA-256: `65df8c25517d30fe7a5695c2f83d4fa3881b3087f93591f149ee5be628476885`.

Campos originales: `index`, `id`, `text`, `truncated`, `place`, `HS`, `RS`, `MS`.

**Observación:** discurso_odio y es_hs_project_raw_extended contienen el mismo archivo binario.

### `es_hs_project_raw_extended_v2`

Odio - Conjunto de datos de origen 'General' generado en Colombia durante el año 2023.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `parquet`. Filas: **4950**. Columnas: **5**. Tamaño: **530882 bytes**.
- País declarado: Colombia. Año/edición declarada: 2023.
- Texto: columna `text`.
- Archivo: [es_hs_project_raw_extended_v2.parquet](https://drive.google.com/file/d/1ram9BXdd5CJmBAKTQPzx9e2Tt8PuXtNi/view?usp=sharing). Ruta de Drive: `corpora/general/es_hs_project_raw_extended_v2.parquet`.
- SHA-256: `d35c1f21480266943aa647c575c9c172a59ef3b44b28aba2a9703062b96a1a2f`.

Campos originales: `id`, `text`, `HS`, `TR`, `AG`.

### `educacion_primaria`

Educacion - Conjunto de datos de origen 'General' generado en Colombia durante el año 2024.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `parquet`. Filas: **342**. Columnas: **5**. Tamaño: **24852 bytes**.
- País declarado: Colombia. Año/edición declarada: 2024.
- Texto: columna `Res`.
- Archivo: [educacion_primaria.parquet](https://drive.google.com/file/d/1y0nlumu_3S_3D_IFWnLw-aa15RVlbqmd/view?usp=sharing). Ruta de Drive: `corpora/general/educacion_primaria.parquet`.
- SHA-256: `dda726cad89065b823a21b3feed1db24ef7c01ab35c34014b1c151fdebcb1a81`.

Campos originales: `ID`, `CUESTIONARIO`, `NUM`, `Preg`, `Res`.

### `llm_humano`

Llm - Conjunto de datos de origen 'General' generado en Colombia durante el año 2023.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `parquet`. Filas: **1844**. Columnas: **3**. Tamaño: **1533864 bytes**.
- País declarado: Colombia. Año/edición declarada: 2023.
- Texto: columna `Texto`.
- Archivo: [llm_humano.parquet](https://drive.google.com/file/d/1GbNj3PoFY0Hs7cQD7AkJUejCDxdXo3bQ/view?usp=sharing). Ruta de Drive: `corpora/general/llm_humano.parquet`.
- SHA-256: `bea48ba52148e284965ec39934749b220d0622fc35d799006dd377c37e4ec7ab`.

Campos originales: `Texto`, `Tipo de fuente`, `Clasificacion`.

### `discurso_odio`

Discurso_odio - Conjunto de datos de origen 'General' generado en Colombia durante el año 2023.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `parquet`. Filas: **915939**. Columnas: **8**. Tamaño: **56487561 bytes**.
- País declarado: Colombia. Año/edición declarada: 2023.
- Texto: columna `text`.
- Archivo: [discurso_odio.parquet](https://drive.google.com/file/d/1lqf0KXUjfMbR2tMJdV4d41dbAFmoVUsz/view?usp=sharing). Ruta de Drive: `corpora/general/discurso_odio.parquet`.
- SHA-256: `65df8c25517d30fe7a5695c2f83d4fa3881b3087f93591f149ee5be628476885`.

Campos originales: `index`, `id`, `text`, `truncated`, `place`, `HS`, `RS`, `MS`.

**Observación:** discurso_odio y es_hs_project_raw_extended contienen el mismo archivo binario.

### `ods`

Ods - Conjunto de datos de origen 'General' generado en Colombia durante el año 2020.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `parquet`. Filas: **17**. Columnas: **2**. Tamaño: **33408 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Descripcion`.
- Archivo: [ods.parquet](https://drive.google.com/file/d/1mPESzZjoXZksBGyAHG4578guEAt32HW7/view?usp=sharing). Ruta de Drive: `corpora/general/ods.parquet`.
- SHA-256: `2949fde46ede1cbcb0b77db9a7034505236bd9759345834fe1233167c86eafe1`.

Campos originales: `Objetivo`, `Descripcion`.

### `laudato_si`

Religion - Conjunto de datos de origen 'General' generado en Colombia durante el año 2020.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `general`.
- Formato: `parquet`. Filas: **14**. Columnas: **3**. Tamaño: **573598 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `text`.
- Archivo: [laudato_si.parquet](https://drive.google.com/file/d/1E2k-n2CuTCuFNmt6UoPMupxHbBbhgJBj/view?usp=sharing). Ruta de Drive: `corpora/general/laudato_si.parquet`.
- SHA-256: `932f1ff8cda0e8ab367f81e055eb4ad88043e60caa67069ff5946bc40d03ecff`.

Campos originales: `file`, `text`, `lang`.

### `news_2020_peru_v2`

News - Conjunto de datos de origen 'News' generado en Peru durante el año 2020.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `news`.
- Formato: `parquet`. Filas: **26711**. Columnas: **3**. Tamaño: **50083422 bytes**.
- País declarado: Perú. Año/edición declarada: 2020.
- Texto: columna `text`.
- Archivo: [news_2020_peru_v2.parquet](https://drive.google.com/file/d/1iOHkRQz2v2t52_msh9pPpW9jxUS7w09L/view?usp=sharing). Ruta de Drive: `corpora/news/news_2020_peru_v2.parquet`.
- SHA-256: `3f24b8775e5945010f8650222b5ee960e03f0f67cb4f54345419dc9f6d0a4300`.

Campos originales: `_id`, `topic`, `text`.

### `news_2020_colombia_v2`

News - Conjunto de datos de origen 'News' generado en Colombia durante el año 2020.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `news`.
- Formato: `parquet`. Filas: **17513**. Columnas: **3**. Tamaño: **40556063 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `text`.
- Archivo: [news_2020_colombia_v2.parquet](https://drive.google.com/file/d/1bPHYfrP_a-6XLto0i2o4kq5mmP1UDEs6/view?usp=sharing). Ruta de Drive: `corpora/news/news_2020_colombia_v2.parquet`.
- SHA-256: `1a57e670c1242122406e95fc21a03b454fb974a610a71ecd1bbcff2a90dcaa5e`.

Campos originales: `_id`, `topic`, `text`.

### `news_2020_ecuador_v2`

News - Conjunto de datos de origen 'News' generado en Ecuador durante el año 2020.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `news`.
- Formato: `parquet`. Filas: **20032**. Columnas: **3**. Tamaño: **41293904 bytes**.
- País declarado: Ecuador. Año/edición declarada: 2020.
- Texto: columna `text`.
- Archivo: [news_2020_ecuador_v2.parquet](https://drive.google.com/file/d/1W3flxoPyGfECuCAnNCx4paPc47j8q6Kp/view?usp=sharing). Ruta de Drive: `corpora/news/news_2020_ecuador_v2.parquet`.
- SHA-256: `4139205280e14856dfc938ad8e4c39cc02b77a57ef8e691672b4a86cbbb37dee`.

Campos originales: `_id`, `topic`, `text`.

### `consolidated_anew_xanew_ncr_inquirer_sel_spanish`

Recurso léxico de ncr y otros léxicos afectivos: 28.491 filas en formato XLSX. Se conservan las categorías y los campos originales.

- Estado: **deshabilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `xlsx`. Filas: **28491**. Columnas: **25**. Tamaño: **1906266 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `word`.
- Archivo: [consolidated_anew_xanew_ncr_inquirer_sel_spanish.xlsx](https://docs.google.com/spreadsheets/d/1rZqgNtREA_O9apFrUNfYaqJItRRLK-Ow/edit?usp=sharing&ouid=107072219928073180472&rtpof=true&sd=true). Ruta de Drive: `resource/lexicones/consolidated_anew_xanew_ncr_inquirer_sel_spanish.xlsx`.
- SHA-256: `403249f51e4a6261cb22dac2bf480ceee42f312910545f11207a0c7c57597d7c`.

Campos originales: `Unnamed: 0.1`, `Unnamed: 0`, `word`, `emotion_ncr`, `intensity_ncr`, `pos_inquirer`, `definition_inquirer`, `categories_inquirer`, `valence_mean_anew`, `valence_sd_anew`, `arousal_mean_anew`, `arousal_sd_anew`, `dominance_mean_anew`, `dominance_sd_anew`, `word_freq_anew`, `valence_mean_xanew`, `valence_sd_xanew`, `arousal_mean_xanew`, `arousal_sd_xanew`, `dominance_mean_xanew`, `dominance_sd_xanew`, `spanish_words`, `Palabra`, `PFA_SEL`, `category_SEL`.

### `lexicon_tic`

Recurso léxico de tic: 457 filas en formato XLSX. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `xlsx`. Filas: **457**. Columnas: **3**. Tamaño: **19704 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Word`.
- Archivo: [lexicon_tic.xlsx](https://docs.google.com/spreadsheets/d/1yKW-YbMrYozF9xWvsZ8sIhl9qdzYmQA9/edit?usp=sharing&ouid=107072219928073180472&rtpof=true&sd=true). Ruta de Drive: `resource/lexicones/lexicon_tic.xlsx`.
- SHA-256: `0fcbcdbac6c199cf5cd8f3b4c262a818951fc9380f80db8bdb0da4687c65bcb0`.

Campos originales: `Word`, `Type`, `Entity`.

### `lexicon_actors_roles`

Recurso léxico de roles: 7.983 filas en formato CSV. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `csv`. Filas: **7983**. Columnas: **3**. Tamaño: **617203 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Word`.
- Archivo: [lexicon_actors_roles.csv](https://drive.google.com/file/d/1TUCJRJhfHPOx7tGt2hq2_ljD0E2N9YWU/view?usp=sharing). Ruta de Drive: `resource/lexicones/lexicon_actors_roles.csv`.
- SHA-256: `c4168debd3c5e08f62a3d95c25f9c7915896e94f2049e482445fd7628e9701b3`.

Campos originales: `Word`, `Class1`, `Class2`.

### `lexicon_actors_roles_excel_v2`

Recurso léxico de roles: 7.983 filas en formato XLSX. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `xlsx`. Filas: **7983**. Columnas: **3**. Tamaño: **235896 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Word`.
- Archivo: [lexicon_actors_roles_excel_v2.xlsx](https://docs.google.com/spreadsheets/d/1wXy8a8hq0uclC3auP7ju-MFa_sfttJ16/edit?usp=sharing&ouid=107072219928073180472&rtpof=true&sd=true). Ruta de Drive: `resource/lexicones/lexicon_actors_roles_v2.xlsx`.
- SHA-256: `73d4ec4ae6602d6e8539977e58dd9d88f6c6ae110819cfe78d0d4ff6da20e153`.

Campos originales: `Word`, `Class1`, `Class2`.

### `lexicon_afectivo_categorias`

Recurso léxico de afectivo: 6.625 filas en formato CSV. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `csv`. Filas: **6625**. Columnas: **3**. Tamaño: **135098 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Palabra`.
- Archivo: [lexicon_afectivo_categorias.csv](https://drive.google.com/file/d/1Bbc5pE_4VEgVot4gU4BQb94FqECiVHsA/view?usp=sharing). Ruta de Drive: `resource/lexicones/lexicon_afectivo_categorias.csv`.
- SHA-256: `382ff1c9b3774b6e4d495e6380154c45024550823e41926e5b4c94817b97e8d7`.

Campos originales: `Palabra`, `category_SEL`, `category_Ncr`.

### `lexicon_afectivo_categorias_v2`

Recurso léxico de afectivo: 6.625 filas en formato XLSX. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `xlsx`. Filas: **6625**. Columnas: **3**. Tamaño: **126572 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Palabra`.
- Archivo: [lexicon_afectivo_categorias_v2.xlsx](https://docs.google.com/spreadsheets/d/1PfyW9Vj7qqO1a81IFvj7loSuTi1fCx81/edit?usp=sharing&ouid=107072219928073180472&rtpof=true&sd=true). Ruta de Drive: `resource/lexicones/lexicon_afectivo_categorias_v2.xlsx`.
- SHA-256: `4494827fcdcdfde8149d759b85905988fbda41a074b7e530274945b96f106bd4`.

Campos originales: `Palabra`, `category_SEL`, `category_Ncr`.

### `lexicon_duelo_completa`

Recurso léxico de duelo: 376 filas en formato XLSX. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `xlsx`. Filas: **376**. Columnas: **8**. Tamaño: **27658 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Word`.
- Archivo: [lexicon_duelo_completa.xlsx](https://docs.google.com/spreadsheets/d/1W68NqgEJnGZ8dT2P38GiffI1l5yLFylF/edit?usp=sharing&ouid=107072219928073180472&rtpof=true&sd=true). Ruta de Drive: `resource/lexicones/lexicon_duelo_completa.xlsx`.
- SHA-256: `d7af13341fa7756d4cc8b9523c4558a82c2e4bd788d390a1cfc4a1b53b76dee5`.

Campos originales: `tiempo`, `familiar`, `negar`, `Unnamed: 3`, `Word`, `Busqueda`, `Hallazgo`, `Tipo`.

### `lexicon_ejecuciones_extrajudiciales`

Recurso léxico de guerra: 338 filas en formato XLSX. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `xlsx`. Filas: **338**. Columnas: **6**. Tamaño: **22973 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Word`.
- Archivo: [lexicon_ejecuciones_extrajudiciales.xlsx](https://docs.google.com/spreadsheets/d/1pWAtwubIJyJbQduQnhBDHiW5ZnfnWivt/edit?usp=sharing&ouid=107072219928073180472&rtpof=true&sd=true). Ruta de Drive: `resource/lexicones/lexicon_ejecuciones_extrajudiciales.xlsx`.
- SHA-256: `9fff1a6a86806a4dd316661a6df1584c0dbcc82d4160d9c3a0cfde69a503daf8`.

Campos originales: `Word`, `Victima`, `Victimario`, `Testigo`, `Métodos`, `Type`.

### `lexicon_estigmatizacion`

Recurso léxico de guerra: 111 filas en formato XLSX. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `xlsx`. Filas: **111**. Columnas: **5**. Tamaño: **14654 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Word`.
- Archivo: [lexicon_estigmatizacion.xlsx](https://docs.google.com/spreadsheets/d/1kuZ6AGX8sYnEyaESGnuWgOwXBFWT4AxH/edit?usp=sharing&ouid=107072219928073180472&rtpof=true&sd=true). Ruta de Drive: `resource/lexicones/lexicon_estigmatizacion.xlsx`.
- SHA-256: `7e3c1775b85f5a3e1b38c79bbe91cb220599a283b1acbee2893bea23724775c6`.

Campos originales: `Word`, `Estigmatización Verbal`, `Estigmatización tribal`, `Estigmatización estructural`, `No directamente estigmatizadora`.

### `lexicon_ministers`

Recurso léxico de gobierno: 2.408 filas en formato CSV. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `csv`. Filas: **2408**. Columnas: **3**. Tamaño: **146599 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Word`.
- Archivo: [lexicon_ministers.csv](https://drive.google.com/file/d/1yASjcUEBMkXnOvBA_4R7QqQ56WjUbt45/view?usp=sharing). Ruta de Drive: `resource/lexicones/lexicon_ministers.csv`.
- SHA-256: `8a25e426316d5544860a22757301f77a38263081b3e4d8a18cc6f2f395f5faf3`.

Campos originales: `Word`, `Class1`, `Class2`.

### `lexicon_ministers_v2`

Recurso léxico de gobierno: 2.408 filas en formato XLSX. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `xlsx`. Filas: **2408**. Columnas: **3**. Tamaño: **75360 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Word`.
- Archivo: [lexicon_ministers_v2.xlsx](https://docs.google.com/spreadsheets/d/182qEedEEieR5cKnNOpLj8amQXXxDbsJI/edit?usp=sharing&ouid=107072219928073180472&rtpof=true&sd=true). Ruta de Drive: `resource/lexicones/lexicon_ministers_v2.xlsx`.
- SHA-256: `a2cfe1b01a3a9042e6430ee318c7115973bf0678404bc30e1697be49e9ebf169`.

Campos originales: `Word`, `Class1`, `Class2`.

### `lexicon_referencia_crea`

Recurso léxico de rae: 737.799 filas en formato CSV. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `csv`. Filas: **737799**. Columnas: **3**. Tamaño: **10838640 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `word`.
- Archivo: [lexicon_referencia_crea.csv](https://drive.google.com/file/d/1rzlO1DMMdVTOkZadOlcWLbJeyBc9A4Lh/view?usp=sharing). Ruta de Drive: `resource/lexicones/lexicon_referencia_crea.csv`.
- SHA-256: `17184f7e1af81470b6f4f7235e695a1b1fdecd192d46af72e71a57360c9fe97c`.

Campos originales: `word`, `freq`, `norm`.

### `lexicon_referencia_creav_2`

Recurso léxico de rae: 737.799 filas en formato CSV. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `csv`. Filas: **737799**. Columnas: **3**. Tamaño: **10838652 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `word`.
- Archivo: [lexicon_referencia_creav_2.csv](https://drive.google.com/file/d/17s76oUZQ6Xmb0cxgcpFmsUbft11Z98n1/view?usp=sharing). Ruta de Drive: `resource/lexicones/lexicon_referencia_creav_2.csv`.
- SHA-256: `52d1b22898f3a2cd1e44edfd5bf406507cc73f190364c860e883907256f038f5`.

Campos originales: `word`, `freq`, `norm`.

### `lexicon_relations_verbs`

Recurso léxico de verbos: 308 filas en formato CSV. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `csv`. Filas: **308**. Columnas: **2**. Tamaño: **6617 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Word`.
- Archivo: [lexicon_relations_verbs.csv](https://drive.google.com/file/d/1Hlj-1a2pZ68CgHAomnfUvl6foLdCVmnw/view?usp=sharing). Ruta de Drive: `resource/lexicones/lexicon_relations_verbs.csv`.
- SHA-256: `050b360845a6fc8ba23ddca6c5fdec67622baf73eb3e9a52e8ef5391c640755b`.

Campos originales: `Word`, `Class`.

### `lexicon_relations_verbs_v2`

Recurso léxico de verbos: 308 filas en formato XLSX. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `xlsx`. Filas: **308**. Columnas: **2**. Tamaño: **15344 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Word`.
- Archivo: [lexicon_relations_verbs_v2.xlsx](https://docs.google.com/spreadsheets/d/1Di6pYrl8FrCX8-t8W9T1U5XbnK48EprX/edit?usp=sharing&ouid=107072219928073180472&rtpof=true&sd=true). Ruta de Drive: `resource/lexicones/lexicon_relations_verbs_v2.xlsx`.
- SHA-256: `c39958d09ab1e357d2457bcc08addeec0426983a4265de4ab668b0eb39705d41`.

Campos originales: `Word`, `Class`.

### `lexicon_sevicia`

Recurso léxico de sevicia: 190 filas en formato CSV. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `csv`. Filas: **190**. Columnas: **2**. Tamaño: **2358 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `word`.
- Archivo: [lexicon_sevicia.csv](https://drive.google.com/file/d/1UyqSAL9SrpxV8qteRkg-ar0Rl0ZjAovd/view?usp=sharing). Ruta de Drive: `resource/lexicones/lexicon_sevicia.csv`.
- SHA-256: `c818f1d5319c762b167d400c3d9583d0d594a68d58a67cfd77fd9ae6a5843ead`.

Campos originales: `word`, `value`.

### `lexicon_verbos_sentencias_tierras`

Recurso léxico de guerra: 236 filas en formato CSV. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `csv`. Filas: **236**. Columnas: **2**. Tamaño: **4826 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Word`.
- Archivo: [lexicon_verbos_sentencias_tierras.csv](https://drive.google.com/file/d/1sV7axFFSFsjngjK8oTaa3OdsIq-gMD-9/view?usp=sharing). Ruta de Drive: `resource/lexicones/lexicon_verbos_sentencias_tierras.csv`.
- SHA-256: `835844c7104ebfcdfbbc76761cd640c69e55fd37b1668b031597a4d61921ad43`.

Campos originales: `Word`, `Class`.

### `lexicon_verbos_sentencias_tierras_v2`

Recurso léxico de guerra: 236 filas en formato XLSX. Se conservan las categorías y los campos originales.

- Estado: **habilitado**. Tipo: `resource`. Familia: `lexicones`.
- Formato: `xlsx`. Filas: **236**. Columnas: **2**. Tamaño: **14050 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: columna `Word`.
- Archivo: [lexicon_verbos_sentencias_tierras_v2.xlsx](https://docs.google.com/spreadsheets/d/1-vccMda46vtuj2cxbXEs825KNl5o2KLq/edit?usp=sharing&ouid=107072219928073180472&rtpof=true&sd=true). Ruta de Drive: `resource/lexicones/lexicon_verbos_sentencias_tierras_v2.xlsx`.
- SHA-256: `04b383b86005406c373e5ff8e4f34349f784a945acfaddcd0e4784ffee85a3b3`.

Campos originales: `Word`, `Class`.

### `tesauro_cev_v2`

Cev - Conjunto de datos de origen 'Tesauro' generado en Colombia durante el año 2020.

- Estado: **habilitado**. Tipo: `resource`. Familia: `tesauro`.
- Formato: `xlsx`. Filas: **12341**. Columnas: **8**. Tamaño: **2004645 bytes**.
- País declarado: Colombia. Año/edición declarada: 2020.
- Texto: representación de los campos de cada fila.
- Archivo: [tesauro_cev_v2.xlsx](https://docs.google.com/spreadsheets/d/14MuznbYb9k6FdLpMvn9Ww-oG4fpLpjDh). Ruta de Drive: `resource/lexicones/tesauro_cev_v2.xlsx`.
- SHA-256: `fbfff01c635ff3d8ab1f56db50323345bfdfd81ac8f7be002ea24e21f1c47e2a`.

Campos originales: `Grupo`, `Término`, `Unnamed: 2`, `Unnamed: 3`, `Unnamed: 4`, `Unnamed: 5`, `Unnamed: 6`, `Unnamed: 7`.

### `gpd_20190625`

Indicadores tabulares del Global Populism Database, edición 2019-06-25.

- Estado: **habilitado**. Tipo: `resource`. Familia: `global_populism_database`.
- Formato: `parquet`. Filas: **4464**. Columnas: **18**. Tamaño: **30825 bytes**.
- País declarado: Multipaís. Año/edición declarada: 2019.
- Texto: representación de los campos de cada fila.
- Archivo: [gdp_20190625.csv.parquet](https://drive.google.com/file/d/1U1_lfIsm2LR7muKQH7_yAE20poRSqBm5/view?usp=drivesdk). Ruta de Drive: `corpora/global_populism_database/gdp_20190625.csv.parquet`.
- SHA-256: `23273f3937f09e4656f1e7a7e464441a3dfff99f6184f54adb62da3701d7cc45`.

Campos originales: `country`, `leader`, `party`, `lr`, `president`, `term`, `startofterm`, `yearbegin`, `endofterm`, `yearend`, `speechtype`, `speechnum`, `codernum`, `rubricgrade`, `averagerubric`, `totalaverage`, `wb_region`, `region`.

### `gpd_v2_1_20251120`

Indicadores del Global Populism Database v2.1 en formato largo, edición 2025-11-20.

- Estado: **habilitado**. Tipo: `resource`. Familia: `global_populism_database`.
- Formato: `parquet`. Filas: **5552**. Columnas: **19**. Tamaño: **53716 bytes**.
- País declarado: Multipaís. Año/edición declarada: 2025.
- Texto: representación de los campos de cada fila.
- Archivo: [gdp_v2.1_20251120.csv.parquet](https://drive.google.com/file/d/1xhxCfyUt6i2T6wDZwioP5U2JVyZ_Mpeb/view?usp=drivesdk). Ruta de Drive: `corpora/global_populism_database/gdp_v2.1_20251120.csv.parquet`.
- SHA-256: `fc47850f06e074985c9c80d7e504f11397c1bc1d8b376df02b7c5bcf4bd3d968`.

Campos originales: `merging_variable`, `country`, `leader`, `party`, `lr`, `president`, `term`, `startofterm`, `yearbegin`, `endofterm`, `yearend`, `speechtype`, `speechnum`, `codernum`, `rubricgrade`, `averagerubric`, `totalaverage`, `wb_region`, `region`.

### `gpd_v2_1_20251120_wide`

Indicadores del Global Populism Database v2.1 en formato ancho, edición 2025-11-20.

- Estado: **habilitado**. Tipo: `resource`. Familia: `global_populism_database`.
- Formato: `parquet`. Filas: **361**. Columnas: **37**. Tamaño: **61577 bytes**.
- País declarado: Multipaís. Año/edición declarada: 2025.
- Texto: representación de los campos de cada fila.
- Archivo: [gdp_v2.1_20251120_Wide.csv.parquet](https://drive.google.com/file/d/18wEzV69epWzGzmUs6xtvfKYMzirpGS2g/view?usp=drivesdk). Ruta de Drive: `corpora/global_populism_database/gdp_v2.1_20251120_Wide.csv.parquet`.
- SHA-256: `2c189d6bbd37595415da31df27903634c581bd195c704980ffce352e9bd4f133`.

Campos originales: `country`, `leader`, `party`, `lr`, `president`, `term`, `startofterm`, `yearbegin`, `endofterm`, `yearend`, `wb_region`, `region`, `totalaverage`, `campaign_file`, `campaign_1`, `campaign_2`, `campaign_3`, `campaign_4`, `campaign_average`, `famous_file`, `famous_1`, `famous_2`, `famous_3`, `famous_4`, `famous_average`, `international_file`, `international_1`, `international_2`, `international_3`, `international_4`, `international_average`, `ribbon_file`, `ribbon_1`, `ribbon_2`, `ribbon_3`, `ribbon_4`, `ribbon_average`.

### `gpd_v2_20220427`

Indicadores tabulares del Global Populism Database v2, edición 2022-04-27.

- Estado: **habilitado**. Tipo: `resource`. Familia: `global_populism_database`.
- Formato: `parquet`. Filas: **4960**. Columnas: **19**. Tamaño: **49212 bytes**.
- País declarado: Multipaís. Año/edición declarada: 2022.
- Texto: representación de los campos de cada fila.
- Archivo: [gpd_v2_20220427.csv.parquet](https://drive.google.com/file/d/1jeJt8-k-NlnfJyaWfio1Qc6QPbnGFKJd/view?usp=drivesdk). Ruta de Drive: `corpora/global_populism_database/gpd_v2_20220427.csv.parquet`.
- SHA-256: `6ea03d52899de68e51af1df22cf8b7d5bfecb046257ff6211525e3fc720f2c4f`.

Campos originales: `merging_variable`, `country`, `leader`, `party`, `lr`, `president`, `term`, `startofterm`, `yearbegin`, `endofterm`, `yearend`, `speechtype`, `speechnum`, `codernum`, `rubricgrade`, `averagerubric`, `totalaverage`, `wb_region`, `region`.

### `gpd_rubrics_20251120`

Rúbricas del Global Populism Database, edición 2025-11-20.

- Estado: **habilitado**. Tipo: `resource`. Familia: `global_populism_database`.
- Formato: `parquet`. Filas: **156**. Columnas: **7**. Tamaño: **79464 bytes**.
- País declarado: Multipaís. Año/edición declarada: 2025.
- Texto: columna `text`.
- Archivo: [rubrics_20251120.parquet](https://drive.google.com/file/d/1Uw6k-dOvM8IpWwt9YlN1SqEjUvKvkiNn/view?usp=drivesdk). Ruta de Drive: `corpora/global_populism_database/rubrics_20251120.parquet`.
- SHA-256: `a7ebaa0e1d670a80c4fe73dea100179c1fce3f7135a47a525fdefdbbf27415aa`.

Campos originales: `country`, `time`, `version`, `president`, `lang`, `file`, `text`.

### `gpd_speeches_20220427`

Discursos del Global Populism Database, edición 2022-04-27.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `global_populism_database`.
- Formato: `parquet`. Filas: **1161**. Columnas: **7**. Tamaño: **11900239 bytes**.
- País declarado: Multipaís. Año/edición declarada: 2022.
- Texto: columna `text`.
- Archivo: [speeches_20220427.parquet](https://drive.google.com/file/d/1Mnu21gfYsU1Zj1IVFpFigjEH3Vab0BVp/view?usp=drivesdk). Ruta de Drive: `corpora/global_populism_database/speeches_20220427.parquet`.
- SHA-256: `ec9ae0228cd1c6653346111e35101b9344d41986452eabb2d88b1f68699ae2cf`.

Campos originales: `country`, `time`, `version`, `president`, `lang`, `file`, `text`.

### `gpd_speeches_20251120`

Discursos del Global Populism Database, edición 2025-11-20.

- Estado: **habilitado**. Tipo: `corpora`. Familia: `global_populism_database`.
- Formato: `parquet`. Filas: **1310**. Columnas: **7**. Tamaño: **13631904 bytes**.
- País declarado: Multipaís. Año/edición declarada: 2025.
- Texto: columna `text`.
- Archivo: [speeches_20251120.parquet](https://drive.google.com/file/d/1884vNancqcP1uLLJrSvZ1COub-mCZ3-K/view?usp=drivesdk). Ruta de Drive: `corpora/global_populism_database/speeches_20251120.parquet`.
- SHA-256: `c89a1fcd95fddce3e3ebb61162eeac52a477de3a8aaff1a2ee6f179e449bf284`.

Campos originales: `country`, `time`, `version`, `president`, `lang`, `file`, `text`.
