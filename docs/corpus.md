---
layout: page
title: Corpus Description 
description: Descripción de los corpus disponibles en la librería open_corpus_co_es
permalink: /corpus
nav_order: 2
---


# Open Corpus CO-ES

Este sitio documenta el uso de la librería `open_corpus_co_es`, que permite descargar y cargar corpus en español para tareas de procesamiento de lenguaje natural (PLN).

## 📚 Corpus disponibles

Los siguientes corpus están disponibles a través de la librería:

| Nombre                                | Año | País     | Tema          | Origen     |
|---------------------------------------|-----|----------|---------------|------------|
| `dataset_bancos_2022`                 | 2022 | Colombia | Financiero    | tweets     |
| `perfiles_periodistas_2020`           | 2020 | Colombia | Perfiles      | tweets     |
| `tweets_miscelaneos_2020`             | 2020 | Colombia | Tweets        | tweets     |
| `educacion_argentina_2024_v2`         | 2024 | Argentina| Educacion     | tweets     |
| `educacion_argentina_2024_v1`         | 2024 | Argentina| Educacion     | tweets     |
| `educacion_colombia_2024_v2`          | 2024 | Colombia | Educacion     | tweets     |
| `educacion_colombia_2024_v1`          | 2024 | Colombia | Educacion     | tweets     |
| `educacion_mexico_2024_v2`            | 2024 | Mexico   | Educacion     | tweets     |
| `educacion_mexico_2024_v1`            | 2024 | Mexico   | Educacion     | tweets     |
| `salud_argentina_2024_v2`             | 2024 | Argentina| Salud         | tweets     |
| `salud_argentina_2024_v1`             | 2024 | Argentina| Salud         | tweets     |
| `salud_colombia_2024_v1`              | 2024 | Colombia | Salud         | tweets     |
| `salud_colombia_2024_v2`              | 2024 | Colombia | Salud         | tweets     |
| `salud_mexico_2024_v1`                | 2024 | Mexico   | Salud         | tweets     |
| `salud_mexico_2024_v2`                | 2024 | Mexico   | Salud         | tweets     |
| `seguridad_argentina_2024_v2`         | 2024 | Argentina| Seguridad     | tweets     |
| `seguridad_argentina_2024_v1`         | 2024 | Argentina| Seguridad     | tweets     |
| `seguridad_colombia_2024_v2`          | 2024 | Colombia | Seguridad     | tweets     |
| `seguridad_colombia_2024_v1`          | 2024 | Colombia | Seguridad     | tweets     |
| `seguridad_mexico_2024_v2`            | 2024 | Mexico   | Seguridad     | tweets     |
| `seguridad_mexico_2024_v1`            | 2024 | Mexico   | Seguridad     | tweets     |
| `entrevistas_victimas_publicas_v2`    | 2020 | Colombia | Entrevistas   | cev        |
| `rag_processed_data`                  | 2020 | Colombia | Entrevistas   | cev        |
| `presidentes`                         | 2023 | Colombia | Presidentes   | general    |
| `edades_entrenamiento`                | 2016 | Colombia | Edades        | general    |
| `musica_metrica`                      | 2020 | Colombia | Musica        | general    |
| `musica_letra`                        | 2020 | Colombia | Musica        | general    |
| `educacion_primaria`                  | 2024 | Colombia | Educacion     | general    |
| `llm_humano`                          | 2023 | Colombia | LLM           | general    |
| `es_hs_project_raw_extended`          | 2023 | Colombia | Odio          | general    |
| `es_hs_project_raw_extended_v2`       | 2023 | Colombia | Odio          | general    |
| `discurso_odio`                       | 2023 | Colombia | Discurso_odio | general    |
| `ods`                                 | 2020 | Colombia | Ods           | general    |
| `laudato_si`                          | 2020 | Colombia | Religion      | general    |
| `news_2020_peru_v2`                   | 2020 | Peru     | News          | news       |
| `news_2020_colombia_v2`               | 2020 | Colombia | News          | news       |
| `news_2020_ecuador_v2`                | 2020 | Ecuador  | News          | news       |
| `consolidated_anew...`                | 2020 | Colombia | NCR           | lexicones  |
| `lexicon_tic`                         | 2020 | Colombia | TIC           | lexicones  |
| `lexicon_actors_roles`                | 2020 | Colombia | Roles         | lexicones  |
| `lexicon_actors_roles_excel_v2`       | 2020 | Colombia | Roles         | lexicones  |
| `lexicon_afectivo_categorias`         | 2020 | Colombia | Afectivo      | lexicones  |
| `lexicon_afectivo_categorias_v2`      | 2020 | Colombia | Afectivo      | lexicones  |
| `lexicon_duelo_completa`              | 2020 | Colombia | Duelo         | lexicones  |
| `lexicon_ejecuciones_extrajudiciales` | 2020 | Colombia | Guerra        | lexicones  |
| `lexicon_estigmatizacion`             | 2020 | Colombia | Guerra        | lexicones  |
| `lexicon_ministers`                   | 2020 | Colombia | Gobierno      | lexicones  |
| `lexicon_ministers_v2`                | 2020 | Colombia | Gobierno      | lexicones  |
| `lexicon_referencia_crea`             | 2020 | Colombia | RAE           | lexicones  |
| `lexicon_referencia_creav_2`          | 2020 | Colombia | RAE           | lexicones  |
| `lexicon_relations_verbs`             | 2020 | Colombia | Verbos        | lexicones  |
| `lexicon_relations_verbs_v2`          | 2020 | Colombia | Verbos        | lexicones  |
| `lexicon_sevicia`                     | 2020 | Colombia | Sevicia       | lexicones  |
| `lexicon_verbos_sentencias_tierras`   | 2020 | Colombia | Guerra        | lexicones  |
| `lexicon_verbos_sentencias_tierras_v2`| 2020 | Colombia | Guerra        | lexicones  |
| `tesauro_cev_v2`                      | 2020 | Colombia | CEV           | tesauro    |

## 📦 Cómo acceder

```bash
python -m open_corpus_co_es --list
python -m open_corpus_co_es --download <nombre_del_corpus>
```

También puedes utilizar `load_corpus` desde Python para cargarlos directamente en memoria.