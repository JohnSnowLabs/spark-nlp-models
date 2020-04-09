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
| UniversalSentenceEncoder                 | `tfhub_use`              | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/tfhub_use_en_2.4.0_2.4_1580582893733.zip)
| UniversalSentenceEncoder                 | `tfhub_use_lg`           | 2.4.0 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/tfhub_use_lg_en_2.4.0_2.4_1580583670712.zip)
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

It is required to specify 3rd argument to `pretrained(name, lang, loc)` function to add the location of these

## Pretrained Models - Spark NLP For Healthcare

### English
| Model                    | Name                           | Build   | Collection      | Explore                                                                                                                                                       | Notes                                             | Download                                                                                                                                     |
|--------------------------|--------------------------------|---------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| AssertionDLModel         | assertion_dl                   | 2.4.0   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/assertion_dl_en_2.4.0_2.4_1580237286004.zip)                   | Trained on i2b2                                   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/assertion_dl_en_2.4.0_2.4_1580237286004.zip)                   |
| AssertionLogRegModel     | assertion_ml                   | 2.4.0   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/assertion_ml_en_2.4.0_2.4_1580237286004.zip)                   | Trained on i2b2                                   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/assertion_ml_en_2.4.0_2.4_1580237286004.zip)                   |
| BertEmbeddings           | biobert_clinical_cased         | 2.3.1   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/biobert_clinical_cased_en_2.3.1_2.4_1574522054965.zip)         | Pretrained from TFHub                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/biobert_clinical_cased_en_2.3.1_2.4_1574522054965.zip)         |
| BertEmbeddings           | biobert_discharge_cased        | 2.3.1   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/biobert_discharge_cased_en_2.3.1_2.4_1574522388638.zip)        | Pretrained from TFHub                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/biobert_discharge_cased_en_2.3.1_2.4_1574522388638.zip)        |
| BertEmbeddings           | biobert_pmc_cased              | 2.3.1   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/biobert_pmc_cased_en_2.3.1_2.4_1574521384805.zip)              | Pretrained from TFHub                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/biobert_pmc_cased_en_2.3.1_2.4_1574521384805.zip)              |
| BertEmbeddings           | biobert_pubmed_cased           | 2.3.1   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/biobert_pubmed_cased_en_2.3.1_2.4_1574521132506.zip)           | Pretrained from TFHub                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/biobert_pubmed_cased_en_2.3.1_2.4_1574521132506.zip)           |
| BertEmbeddings           | biobert_pubmed_pmc_cased       | 2.3.1   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/biobert_pubmed_pmc_cased_en_2.3.1_2.4_1574521728558.zip)       | Pretrained from TFHub                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/biobert_pubmed_pmc_cased_en_2.3.1_2.4_1574521728558.zip)       |
| ChunkEntityResolverModel | chunkresolve_cpt_clinical      | 2.4.2   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_cpt_clinical_en_2.4.2_2.4_1583085325631.zip)      | Trained on Current Procedural Terminology dataset | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/chunkresolve_cpt_clinical_en_2.4.2_2.4_1583085325631.zip)      |
| ChunkEntityResolverModel | chunkresolve_icd10cm_clinical  | 2.4.2   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10cm_clinical_en_2.4.2_2.4_1583085234727.zip)  | Trained on ICD10 Clinical Modification dataset    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/chunkresolve_icd10cm_clinical_en_2.4.2_2.4_1583085234727.zip)  |
| ChunkEntityResolverModel | chunkresolve_icd10pcs_clinical | 2.4.2   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10pcs_clinical_en_2.4.2_2.4_1583085287797.zip) | Trained on ICD10 Procedure Coding System dataset  | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/chunkresolve_icd10pcs_clinical_en_2.4.2_2.4_1583085287797.zip) |
| ChunkEntityResolverModel | chunkresolve_icdo_clinical     | 2.4.2   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icdo_clinical_en_2.4.2_2.4_1583085316343.zip)     | nan                                               | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/chunkresolve_icdo_clinical_en_2.4.2_2.4_1583085316343.zip)     |
| PipelineModel            | clinical_analysis              | 2.4.0   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/clinical_analysis_en_2.4.0_2.4_1580600773378.zip)              | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/clinical_analysis_en_2.4.0_2.4_1580600773378.zip)              |
| PipelineModel            | clinical_deidentification      | 2.4.0   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_en_2.4.0_2.4_1580481115376.zip)      | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/clinical_deidentification_en_2.4.0_2.4_1580481115376.zip)      |
| PipelineModel            | clinical_ner_assertion         | 2.4.0   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/clinical_ner_assertion_en_2.4.0_2.4_1580481098096.zip)         | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/clinical_ner_assertion_en_2.4.0_2.4_1580481098096.zip)         |
| ContextSpellCheckerModel | context_spell_med              | 2.0.2   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/context_spell_med_en_2.0.2_2.4_1564584130634.zip)              | nan                                               | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/context_spell_med_en_2.0.2_2.4_1564584130634.zip)              |
| NerDLModel               | deidentify_dl                  | 2.4.0   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/deidentify_dl_en_2.4.0_2.4_1580237286004.zip)                  | Trained on n2c2 Demographic dataset               | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/deidentify_dl_en_2.4.0_2.4_1580237286004.zip)                  |
| DeIdentificationModel    | deidentify_rb                  | 2.0.2   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/deidentify_rb_en_2.0.2_2.4_1559672122511.zip)                  | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/deidentify_rb_en_2.0.2_2.4_1559672122511.zip)                  |
| WordEmbeddingsModel      | embeddings_clinical            | 2.4.0   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/embeddings_clinical_en_2.4.0_2.4_1580237286004.zip)            | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/embeddings_clinical_en_2.4.0_2.4_1580237286004.zip)            |
| WordEmbeddingsModel      | embeddings_healthcare          | 2.4.4   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/embeddings_healthcare_en_2.4.4_2.4_1585188313964.zip)          | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/embeddings_healthcare_en_2.4.4_2.4_1585188313964.zip)          |
| NerDLModel               | ner_bionlp                     | 2.4.0   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_bionlp_en_2.4.0_2.4_1580237286004.zip)                     | Trained on BioNLP Dataset                         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/ner_bionlp_en_2.4.0_2.4_1580237286004.zip)                     |
| NerDLModel               | ner_clinical                   | 2.4.0   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_en_2.4.0_2.4_1580237286004.zip)                   | Trained on i2b2                                   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/ner_clinical_en_2.4.0_2.4_1580237286004.zip)                   |
| NerCRFModel              | ner_crf                        | 2.4.0   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_crf_en_2.4.0_2.4_1580237286004.zip)                        | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/ner_crf_en_2.4.0_2.4_1580237286004.zip)                        |
| NerDLModel               | ner_diseases                   | 2.4.4   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_diseases_en_2.4.4_2.4_1584452534235.zip)                   | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/ner_diseases_en_2.4.4_2.4_1584452534235.zip)                   |
| NerDLModel               | ner_drugs                      | 2.4.4   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_drugs_en_2.4.4_2.4_1584452534235.zip)                      | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/ner_drugs_en_2.4.4_2.4_1584452534235.zip)                      |
| NerDLModel               | ner_healthcare                 | 2.4.4   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_healthcare_en_2.4.4_2.4_1585188313964.zip)                 | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/ner_healthcare_en_2.4.4_2.4_1585188313964.zip)                 |
| NerDLModel               | ner_posology                   | 2.4.4   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_posology_en_2.4.4_2.4_1584452534235.zip)                   | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/ner_posology_en_2.4.4_2.4_1584452534235.zip)                   |
| PerceptronModel          | pos_clinical                   | 2.0.2   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/pos_clinical_en_2.0.2_2.4_1556660550177.zip)                   | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/pos_clinical_en_2.0.2_2.4_1556660550177.zip)                   |
| ContextSpellCheckerModel | spellcheck_clinical            | 2.0.2   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/spellcheck_clinical_en_2.0.2_2.4_1558461056197.zip)            | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/spellcheck_clinical_en_2.0.2_2.4_1558461056197.zip)            |
| ContextSpellCheckerModel | spellcheck_dl                  | 2.2.2   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/spellcheck_dl_en_2.2.2_2.4_1573526353270.zip)                  | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/spellcheck_dl_en_2.2.2_2.4_1573526353270.zip)                  |
| TextMatcherModel         | textmatch_cpt_token            | 2.4.0   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/textmatch_cpt_token_en_2.4.0_2.4_1580319204346.zip)            | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/textmatch_cpt_token_en_2.4.0_2.4_1580319204346.zip)            |
| TextMatcherModel         | textmatch_cpt_token_n2c1       | 2.3.3   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/textmatch_cpt_token_n2c1_en_2.3.3_2.4_1574711212216.zip)       | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/textmatch_cpt_token_n2c1_en_2.3.3_2.4_1574711212216.zip)       |
| TextMatcherModel         | textmatch_icdo                 | 2.4.2   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/textmatch_icdo_en_2.4.2_2.4_1583201177949.zip)                 | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/textmatch_icdo_en_2.4.2_2.4_1583201177949.zip)                 |
| TextMatcherModel         | textmatch_icdo_ner             | 2.4.0   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/textmatch_icdo_ner_en_2.4.0_2.4_1580319074850.zip)             | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/textmatch_icdo_ner_en_2.4.0_2.4_1580319074850.zip)             |
| TextMatcherModel         | textmatch_icdo_ner_n2c4        | 2.3.3   | clinical/models | [Explore](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/textmatch_icdo_ner_n2c4_en_2.3.3_2.4_1574436247328.zip)        | NOTES                                             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com//clinical/models/textmatch_icdo_ner_n2c4_en_2.3.3_2.4_1574436247328.zip)        |

## Contact

nlp@johnsnowlabs.com

## John Snow Labs

[http://johnsnowlabs.com](http://johnsnowlabs.com)
