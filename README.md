<a href="https://johnsnowlabs.com"><img src="https://www.johnsnowlabs.com/wp-content/uploads/2020/03/johnsnowlabs-square.png" width="125" height="125" align="right" /></a>

# Spark NLP Models

[![Build Status](https://travis-ci.org/JohnSnowLabs/spark-nlp.svg?branch=master)](https://travis-ci.org/JohnSnowLabs/spark-nlp) [![Maven Central](https://maven-badges.herokuapp.com/maven-central/com.johnsnowlabs.nlp/spark-nlp_2.11/badge.svg)](https://search.maven.org/artifact/com.johnsnowlabs.nlp/spark-nlp_2.11) [![PyPI version](https://badge.fury.io/py/spark-nlp.svg)](https://badge.fury.io/py/spark-nlp) [![Anaconda-Cloud](https://anaconda.org/johnsnowlabs/spark-nlp/badges/version.svg)](https://anaconda.org/JohnSnowLabs/spark-nlp) [![License](https://img.shields.io/badge/License-Apache%202.0-brightgreen.svg)](https://github.com/JohnSnowLabs/spark-nlp/blob/master/LICENSE)

We use this repository to maintain our releases of pre-trained pipelines and models for the Spark NLP library. For more info please take a look at our [releases](https://github.com/JohnSnowLabs/spark-nlp-models/releases).

## Project's website

Take a look at our official Spark NLP page: [http://nlp.johnsnowlabs.com/](http://nlp.johnsnowlabs.com/) for user documentation and examples

## Slack community channel

[Join Slack](https://join.slack.com/t/spark-nlp/shared_invite/enQtNjA4MTE2MDI1MDkxLTM4ZDliMjU5OWZmMDE1ZGVkMjg0MWFjMjU3NjY4YThlMTJkNmNjNjM3NTMwYzlhMWY4MGMzODI2NDBkOWU4ZDE)

## Table of contents

* [Pretrained Models](#pretrained-models)
  * [Public Models](#public-models)
    * [English](#english---models)
    * [French](#french---models)
    * [German](#german---models)
    * [Italian](#italian---models)
    * [Spanish](#spanish---models)
    * [Russian](#russian---models)
    * [Multi-language](#multi-language)

* [Pretrained Pipelines](#pretrained-pipelines)
  * [English](#english---pipelines)
  * [French](#french---pipelines)
  * [German](#german---pipelines)
  * [Italian](#italian---pipelines)
  * [Spanish](#spanish---pipelines)
  * [Russian](#russian---pipelines)

* [Licensed Enterprise](#licensed-enterprise)
  
# Pretrained Models

## Public Models

`pretrained(name, lang)` function to use

### English - Models

| Model                                    | Name                      | Build            | Description | Notes | Offline                                                                                                                            |
|:-----------------------------------------|:--------------------------|:-----------------|:------------|:------|:-----------------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer)             | `lemma_antbnc`            | 2.0.2 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_antbnc_en_2.0.2_2.4_1556480454569.zip) |
| PerceptronModel (POS)                    | `pos_anc`                 | 2.0.2 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_anc_en_2.0.2_2.4_1556659930154.zip) |
| PerceptronModel (POS UD)                    | `pos_ud_ewt`          | 2.2.2 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_ewt_en_2.2.2_2.4_1570464827452.zip) |
| NerCrfModel (NER with GloVe)             | `ner_crf`                 | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_crf_en_2.4.0_2.4_1580237286004.zip) |
| NerDLModel (NER with GloVe)              | `ner_dl`                  | 2.4.3 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_en_2.4.3_2.4_1584624950746.zip) |
| NerDLModel (NER with BERT)              | `ner_dl_bert`                  | 2.4.3 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_bert_en_2.4.3_2.4_1584624951079.zip) |
| NerDLModel (OntoNotes with GloVe 100d)   | `onto_100`                | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_100_en_2.4.0_2.4_1579729071672.zip) |
| NerDLModel (OntoNotes with GloVe 300d)   | `onto_300`                | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_300_en_2.4.0_2.4_1579729071854.zip) |
| WordEmbeddings (GloVe)                   | `glove_100d`              | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/glove_100d_en_2.4.0_2.4_1579690104032.zip) |
| BertEmbeddings (base_uncased)            | `bert_base_uncased`       | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_base_uncased_en_2.4.0_2.4_1580579889322.zip) |
| BertEmbeddings (base_cased)              | `bert_base_cased`         | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_base_cased_en_2.4.0_2.4_1580579557778.zip) |
| BertEmbeddings (large_uncased)           | `bert_large_uncased`      | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_large_uncased_en_2.4.0_2.4_1580581306683.zip) |
| BertEmbeddings (large_cased)             | `bert_large_cased`        | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_large_cased_en_2.4.0_2.4_1580580251298.zip) |
| ElmoEmbeddings                           | `elmo`                    | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/elmo_en_2.4.0_2.4_1580488815299.zip)
| UniversalSentenceEncoder                 | `tfhub_use`              | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/tfhub_use_en_2.4.0_2.4_1587136330099.zip)
| UniversalSentenceEncoder                 | `tfhub_use_lg`           | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/tfhub_use_lg_en_2.4.0_2.4_1587136993894.zip)
| NerDLModel                               | `ner_dl_sentence`         | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_sentence_en_2.4.0_2.4_1580252313303.zip)|
| SymmetricDeleteModel (Spell Checker)     | `spellcheck_sd`           | 2.0.2 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/spellcheck_sd_en_2.0.2_2.4_1556604489934.zip)|
| NorvigSweetingModel (Spell Checker)      | `spellcheck_norvig`       | 2.0.2 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/spellcheck_norvig_en_2.0.2_2.4_1556605026653.zip)|
| ViveknSentimentModel (Sentiment)         | `sentiment_vivekn`        | 2.0.2 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentiment_vivekn_en_2.0.2_2.4_1556663184035.zip)|
| DependencyParser (Dependency)            | `dependency_conllu`       | 2.0.8 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_conllu_en_2.0.8_2.4_1561435004077.zip)|
| TypedDependencyParser (Dependency)       | `dependency_typed_conllu` | 2.0.8 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_typed_conllu_en_2.0.8_2.4_1561473259215.zip) |

### French - Models

| Model                        | Name               | Build | Notes | Description | Offline                                                                                                                                                                                                |
|:-----------------------------|:-------------------|:------|:------|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer) | `lemma`            |   2.0.2    |       |  | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_fr_2.0.2_2.4_1556531462843.zip)                                                                                       |
| PerceptronModel (POS UD)     | `pos_ud_gsd`       |   2.0.2    |       |  | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_gsd_fr_2.0.2_2.4_1556531457346.zip)                                                                                  |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` |   2.0.2    |       |  | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_fr_2.4.0_2.4_1579699913554.zip)                                                                            |

| Feature   | Description                                                                                                                                                                                            |    |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---|
| **Lemma** | Trained by **Lemmatizer** annotator on **lemmatization-lists** by `Michal Měchura`                                                                                                                     |    |
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/fr_gsd/index.html)                                                             |    |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |    |

### German - Models

| Model                        | Name               | Build            | Notes | Description | Offline                                                                                                                                                                                                |
|:-----------------------------|:-------------------|:-----------------|:------|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.0.8 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_de_2.0.8_2.4_1561248996126.zip)                                                                                             |
| PerceptronModel (POS UD)     | `pos_ud_hdt`       | 2.0.8 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_hdt_de_2.0.8_2.4_1561232528570.zip)                                                                                        |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` | 2.4.0 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_de_2.4.0_2.4_1579699913555.zip)|

| Feature   | Description                                                                                                                                                                                            |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lemma** | Trained by **Lemmatizer** annotator on **lemmatization-lists** by `Michal Měchura`                                                                                                                     |
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/de_hdt/index.html)                                                             |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |

### Italian - Models

| Model                         | Name               | Build            | Notes | Description | Offline                                                                                                                     |
|:------------------------------|:-------------------|:-----------------|:------|:------------|:----------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer)  | `lemma_dxc`        | 2.0.2 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_dxc_it_2.0.2_2.4_1556531469058.zip)        |
| ViveknSentimentAnalysis (Sentiment) | `sentiment_dxc`    | 2.0.2 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentiment_dxc_it_2.0.2_2.4_1556531477694.zip)    |
| PerceptronModel (POS UD)      | `pos_ud_isdt`      | 2.0.8 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_isdt_it_2.0.8_2.4_1560168427464.zip)      |
| NerDLModel (glove_840B_300)   | `wikiner_840B_300` | 2.4.0 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_it_2.4.0_2.4_1579699913554.zip) |

| Feature   | Description                                                                                                                                                                                            |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lemma** | Trained by **Lemmatizer** annotator on **DXC Technology** dataset                                                                                                                                      |
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/it_isdt/index.html)                                                            |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |

### Spanish - Models

| Model                        | Name               | Build            | Notes | Description | Offline                                                                                                                                                                                                |
|:-----------------------------|:-------------------|:-----------------|:------|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.4.0 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_es_2.4.0_2.4_1581890818386.zip) |
| PerceptronModel (POS UD)     | `pos_ud_gsd`       | 2.4.0 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_gsd_es_2.4.0_2.4_1581891015986.zip) |
| NerDLModel (glove_100d)  | `wikiner_6B_100` | 2.4.0 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_100_es_2.4.0_2.4_1581971941700.zip) |
| NerDLModel (glove_6B_300)  | `wikiner_6B_300` | 2.4.0 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_300_es_2.4.0_2.4_1581971942090.zip) |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` | 2.4.0 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_es_2.4.0_2.4_1581971942091.zip;) |

| Feature   | Description                                                                                                                                                                                            |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lemma** | Trained by **Lemmatizer** annotator on **lemmatization-lists** by `Michal Měchura`                                                                                                                     |
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/es_gsd/index.html)                                                             |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |

### Russian - Models

| Model                        | Name               | Build            | Notes | Description | Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.4.4 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_ru_2.4.4_2.4_1584013425855.zip) |
| PerceptronModel (POS UD)     | `pos_ud_gsd`       | 2.4.4 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_gsd_ru_2.4.4_2.4_1584013495069.zip) |
| NerDLModel (glove_100d)  | `wikiner_6B_100` | 2.4.4 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_100_ru_2.4.4_2.4_1584014001452.zip) |
| NerDLModel (glove_6B_300)  | `wikiner_6B_300` | 2.4.4 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_300_ru_2.4.4_2.4_1584014001694.zip) |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` | 2.4.4 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_ru_2.4.4_2.4_1584014001695.zip) |

| Feature   | Description                                                                                                                                                                                            |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lemma** | Trained by **Lemmatizer** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/ru_gsd/index.html)|
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/ru_gsd/index.html)                                                             |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |

### Multi-language

| Model                        | Name               | Build            | Notes | Description                                                                                                                 | Offline |
|:-----------------------------|:-------------------|:-----------------|:------|:----------------------------------------------------------------------------------------------------------------------------|:--------|
| WordEmbeddings (GloVe)       | `glove_840B_300`   | 2.4.0 |     |  | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/glove_840B_300_xx_2.4.0_2.4_1579698926752.zip)   |         |
| WordEmbeddings (GloVe)       | `glove_6B_300`     | 2.4.0 |      | | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/glove_6B_300_xx_2.4.0_2.4_1579698630432.zip)     |         |
| BertEmbeddings (multi_cased) | `bert_multi_cased` | 2.4.0 |      | | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_multi_cased_xx_2.4.0_2.4_1580582335793.zip) |         |

## Pretrained Pipelines

### English - Pipelines

| Pipeline                     | Name                                  | Build            | lang | Description | Offline                                                                                                                                        |
|:-----------------------------|:--------------------------------------|:-----------------|:------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| Explain Document ML          | `explain_document_ml`                 | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_ml_en_2.4.0_2.4_1580252705962.zip) |
| Explain Document DL          | `explain_document_dl`                 | 2.4.3 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_dl_en_2.4.3_2.4_1584626657780.zip) |
| Recognize Entities DL        | `recognize_entities_dl`               | 2.4.3 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/recognize_entities_dl_en_2.4.3_2.4_1584626752821.zip) |
| Recognize Entities DL        | `recognize_entities_bert`             | 2.4.3 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/recognize_entities_bert_en_2.4.3_2.4_1584626853422.zip) |
| OntoNotes Entities Small     | `onto_recognize_entities_sm`          | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_recognize_entities_sm_en_2.4.0_2.4_1579730599257.zip) |
| OntoNotes Entities Large     | `onto_recognize_entities_lg`          | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_recognize_entities_lg_en_2.4.0_2.4_1579729320751.zip) |
| Match Datetime               | `match_datetime`                      | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_datetime_en_2.4.0_2.4_1580246861565.zip) |
| Match Pattern                | `match_pattern`                       | 2.4.0 |   `en`    |      | [Download]() |
| Match Chunk                  | `match_chunks`                        | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_chunks_en_2.4.0_2.4_1580246868138.zip) |
| Match Phrases                | `match_phrases`                       | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_phrases_en_2.4.0_2.4_1580255815623.zip)|
| Clean Stop                   | `clean_stop`                          | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clean_stop_en_2.4.0_2.4_1580255705789.zip)|
| Clean Pattern                | `clean_pattern`                       | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clean_pattern_en_2.4.0_2.4_1580246862642.zip)|
| Clean Slang                  | `clean_slang`                         | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clean_slang_en_2.4.0_2.4_1580255816146.zip)|
| Check Spelling               | `check_spelling`                      | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/check_spelling_en_2.4.0_2.4_1580246859135.zip)|
| Analyze Sentiment            | `analyze_sentiment`                   | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/analyze_sentiment_en_2.4.0_2.4_1580483464667.zip)|
| Dependency Parse             | `dependency_parse`                    | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_parse_en_2.4.0_2.4_1580255669655.zip)|

### French - Pipelines

| Pipeline                 | Name                   | Build            | lang | Description                                                                                                                     | Offline |
|:-------------------------|:-----------------------|:-----------------|:------|:--------------------------------------------------------------------------------------------------------------------------------|:--------|
| Explain Document Large   | `explain_document_lg`  | 2.4.0 |   `fr`| |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_fr_2.4.0_2.4_1579709189947.zip)  |         |
| Explain Document Medium  | `explain_document_md`  | 2.4.0 |   `fr`| |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_fr_2.4.0_2.4_1579722754344.zip)  |         |
| Entity Recognizer Large  | `entity_recognizer_lg` | 2.4.0 |   `fr`| |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_fr_2.4.0_2.4_1579710310593.zip) |         |
| Entity Recognizer Medium | `entity_recognizer_md` | 2.4.0 |   `fr`| |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_fr_2.4.0_2.4_1579722764594.zip) |         |

### German - Pipelines

| Pipeline                 | Name                   | Build         | lang | Description | Offline                                                                                                                         |
|:-------------------------|:-----------------------|:--------------|:------|:------------|:--------------------------------------------------------------------------------------------------------------------------------|
| Explain Document Large   | `explain_document_lg`  | 2.4.0 |  `de` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_de_2.4.0_2.4_1579722852211.zip)  |
| Explain Document Medium  | `explain_document_md`  | 2.4.0 |  `de` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_de_2.4.0_2.4_1579722872528.zip)  |
| Entity Recognizer Large  | `entity_recognizer_lg` | 2.4.0 |  `de` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_de_2.4.0_2.4_1579722883057.zip) |
| Entity Recognizer Medium | `entity_recognizer_md` | 2.4.0 |  `de` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_de_2.4.0_2.4_1579722895254.zip) |

### Italian - Pipelines

| Pipeline                 | Name                   | Build          | lang | Description | Offline                                                                                                                         |
|:-------------------------|:-----------------------|:------|:-------|:------------|:--------------------------------------------------------------------------------------------------------------------------------|
| Explain Document Large   | `explain_document_lg`  | 2.4.0 |   `it` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_it_2.4.0_2.4_1579722789680.zip)  |
| Explain Document Medium  | `explain_document_md`  | 2.4.0 |   `it` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_it_2.4.0_2.4_1579722813892.zip)  |
| Entity Recognizer Large  | `entity_recognizer_lg` | 2.4.0 |   `it` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_it_2.4.0_2.4_1579722823718.zip) |
| Entity Recognizer Medium | `entity_recognizer_md` | 2.4.0 |   `it` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_it_2.4.0_2.4_1579722834033.zip) |

### Spanish - Pipelines

| Pipeline                 | Name                   | Build  | lang | Description | Offline   |
|:-------------------------|:-----------------------|:-------|:-------|:----------|:----------|
| Explain Document Small    | `explain_document_sm`  | 2.4.0 |   `es` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_sm_es_2.4.0_2.4_1581977077084.zip)  |
| Explain Document Medium   | `explain_document_md`  | 2.4.0 |   `es` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_es_2.4.0_2.4_1581976836224.zip)  |
| Explain Document Large    | `explain_document_lg`  | 2.4.0 |   `es` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_es_2.4.0_2.4_1581975536033.zip)  |
| Entity Recognizer Small   | `entity_recognizer_sm`  | 2.4.0 |   `es` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_sm_es_2.4.0_2.4_1581978479912.zip)  |
| Entity Recognizer Medium  | `entity_recognizer_md`  | 2.4.0 |   `es` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_es_2.4.0_2.4_1581978260094.zip)  |
| Entity Recognizer Large   | `entity_recognizer_lg`  | 2.4.0 |   `es` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_es_2.4.0_2.4_1581977172660.zip)  |
  
### Russian - Pipelines

| Pipeline                 | Name                   | Build  | lang | Description | Offline   |
|:-------------------------|:-----------------------|:-------|:-------|:----------|:----------|
| Explain Document Small    | `explain_document_sm`  | 2.4.4 |   `ru` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_sm_ru_2.4.4_2.4_1584017142719.zip)  |
| Explain Document Medium   | `explain_document_md`  | 2.4.4 |   `ru` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_ru_2.4.4_2.4_1584016917220.zip)  |
| Explain Document Large    | `explain_document_lg`  | 2.4.4 |   `ru` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_ru_2.4.4_2.4_1584015824836.zip)  |
| Entity Recognizer Small   | `entity_recognizer_sm`  | 2.4.4 |   `ru` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_sm_ru_2.4.4_2.4_1584018543619.zip)  |
| Entity Recognizer Medium  | `entity_recognizer_md`  | 2.4.4 |   `ru` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_ru_2.4.4_2.4_1584018332357.zip)  |
| Entity Recognizer Large   | `entity_recognizer_lg`  | 2.4.4 |   `ru` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_ru_2.4.4_2.4_1584017227871.zip)  |  

# Licensed Enterprise

It is required to specify 3rd argument to `pretrained(name, lang, location)` function to add the location of these

## Pretrained Models - Spark NLP For Healthcare

### English Language, Clinical/Models Location   

`{Model}.pretrained({Name}, 'en', 'clinical/models')`

"Name","Model","TrainedOn","Extracts","DatasetLink"
"assertion_dl","AssertionDLModel","Trained on i2b2",,
"assertion_ml","AssertionLogRegModel","Trained on i2b2",,
"biobert_clinical_cased","BertEmbeddings","Pretrained from TFHub",,
"biobert_discharge_cased","BertEmbeddings","Pretrained from TFHub",,
"biobert_pmc_cased","BertEmbeddings","Pretrained from TFHub",,
"biobert_pubmed_cased","BertEmbeddings","Pretrained from TFHub",,
"biobert_pubmed_pmc_cased","BertEmbeddings","Pretrained from TFHub",,
"chunkresolve_cpt_clinical","ChunkEntityResolverModel","Trained on Current Procedural Terminology dataset",,
"chunkresolve_icd10cm_clinical","ChunkEntityResolverModel","Trained on ICD10 Clinical Modification dataset",,
"chunkresolve_icd10pcs_clinical","ChunkEntityResolverModel","Trained on ICD10 Procedure Coding System dataset",,
"chunkresolve_icdo_clinical","ChunkEntityResolverModel","Trained on ICD-O Histology Behaviour dataset",,
"context_spell_med","ContextSpellCheckerModel",,,
"deidentify_dl","NerDLModel","Trained on n2c2 Demographic dataset",,
"deidentify_rb","DeIdentificationModel","Rule based DeIdentifier based on `deidentify_dl`",,
"embeddings_clinical","WordEmbeddingsModel","Trained on PubMed corpora",,
"embeddings_healthcare","WordEmbeddingsModel","Trained on PubMed + ICD10 + UMLS + MIMIC III corpora",,
"ensembleresolve_snomed_clinical","EnsembleEntityResolverModel","Trained on SNOMED ontology graph with `embeddings_clinical`",,
"ensembleresolve_snomed_healthcare","EnsembleEntityResolverModel","Trained on SNOMED ontology graph with `embeddings_healthcare`",,
"ensembleresolve_rxnorm_clinical","EnsembleEntityResolverModel","Trained on RxNorm ontology graph with `embeddings_clinical`",,
"ensembleresolve_rxnorm_healthcare","EnsembleEntityResolverModel","Trained on RxNorm ontology graph with `embeddings_healthcare`",,
"ner_bionlp","NerDLModel","Trained on Cancer Genetics (CG) task of the BioNLP Shared Task 2013 with `embeddings_clinical`","Amino_acid, Anatomical_system, Cancer, Cell, Cellular_component, Developing_anatomical_Structure, Gene_or_gene_product, Immaterial_anatomical_entity, Multi-tissue_structure, Organ, Organism, Organism_subdivision, Simple_chemical, Tissue.","http://2013.bionlp-st.org/tasks/cancer-genetics"
"ner_clinical","NerDLModel","Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_clinical`.","Problem, Test, Treatment.","https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp"
"ner_diseases","NerDLModel","Trained on i2b2 with `embeddings_clinical.","Disease",
"ner_drugs","NerDLModel","Trained on i2b2_med7 + FDA with `embeddings_clinical`.","DrugChem (Drug and Chemicals)","https://www.i2b2.org/NLP/Medication"
"ner_healthcare","NerDLModel","Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_healthcare`.","Problem, Test, Treatment.","https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/"
"ner_posology","NerDLModel","Trained on the 2018 i2b2 dataset and FDA Drug datasets with `embeddings_clinical`.","Dosage, Drug, Duration, Form,  Frequency, Route, Strength.","https://open.fda.gov/"
"pos_clinical","PerceptronModel","Trained with MedPost dataset",,
"spellcheck_clinical","ContextSpellCheckerModel","",,
"spellcheck_dl","ContextSpellCheckerModel","",,
"textmatch_cpt_token","TextMatcherModel","Trai,ned on NER Synonym Augmented Procedural Terminology bigram tokens combined up to a window of one",,
"textmatch_icdo_ner","TextMatcherModel","Trained on NER Synonym Augmented ICD Histology Behaviour bigram tokens up to a window of four",,
"ner_cellular","NerDLModel","Trained on the JNLPBA corpus containing more than 2.404 publication abstracts with `embeddings_clinical`","DNA, Cell_type, Cell_line, RNA, Protein.","http://www.geniaproject.org/"
"ner_anatomy","NerDLModel","Trained on the Anatomical Entity Mention (AnEM) corpus with `embeddings_clinical`","Anatomical_system, Cell, Cellular_component, Developing_anatomical_structure, Immaterial_anatomical_entity, Multi-tissue_structure, Organ, Organism_subdivision, Organism_substance, Pathological_formation, Tissue.","http://www.nactem.ac.uk/anatomy/"
"ner_deid_enriched","NerDLModel","Trained on JSL enriched n2c2 2014: De-identification and Heart Disease Risk Factors Challenge datasets with `embeddings_clinical`","Age, City, Country, Date, Doctor, Hospital, Idnum, Medicalrecord, Organization, Patient, Phone, Profession, State, Street, Username, Zip.","https://portal.dbmi.hms.harvard.edu/projects/n2c2-2014/"
"ner_deid_large","NerDLModel","Trained on plain n2c2 2014: De-identification and Heart Disease Risk Factors Challenge datasets with `embeddings_clinical`","Age, City, Country, Date, Doctor, Hospital, Idnum, Medicalrecord, Organization, Patient, Phone, Profession, State, Street, Username, Zip.","https://portal.dbmi.hms.harvard.edu/projects/n2c2-2014/"
"ner_jsl","NerDLModel","",,
"ner_jsl_enriched","NerDLModel","",,
"ner_posology_large","NerDLModel","Trained on the 2018 i2b2 dataset and FDA Drug datasets with `embeddings_clinical`.","Dosage, Drug, Duration, Form,  Frequency, Route, Strength.","https://open.fda.gov/"
"ner_posology_small","NerDLModel","Trained on the 2018 i2b2 dataset (no FDA) with `embeddings_clinical`.","Dosage, Drug, Duration, Form,  Frequency, Route, Strength.","https://www.i2b2.org/NLP/Medication"
"ner_risk_factors","NerDLModel","Trained on plain n2c2 2014: De-identification and Heart Disease Risk Factors Challenge datasets with `embeddings_clinical`","Cad, Diabetes, Family_hist, Hyperlipidemia, Hypertension, Medication, Obese, Phi, Smoker.","https://portal.dbmi.hms.harvard.edu/projects/n2c2-2014/"

## Contact

nlp@johnsnowlabs.com

## John Snow Labs

[http://johnsnowlabs.com](http://johnsnowlabs.com)
