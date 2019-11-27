<a href="https://johnsnowlabs.com"><img src="https://media.licdn.com/dms/image/C510BAQFT1HLZor5NGA/company-logo_400_400/0?e=1576713600&v=beta&t=LpJFzciaKlQfDAerduqyysJbsIrDaFV1E4Aunmne6E4" width="125" height="125" align="right" /></a>

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
    * [French](#French---models)
    * [German](#german---models)
    * [Italian](#italian---models)
    * [Multi-language](#multi-language)
    
* [Pretrained Pipelines](#pretrained-pipelines)
  * [English](#english---pipelines)
  * [French](#French---pipelines)
  * [Italian](#italian---pipelines)

* [Licensed Enterprise](#licensed-enterprise)
  
# Pretrained Models

## Public Models

`pretrained(name, lang)` function to use

### English - Models

| Model                                    | Name                      | Build            | Description | Notes | Offline                                                                                                                            |
|:-----------------------------------------|:--------------------------|:-----------------|:------------|:------|:-----------------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer)             | `lemma_antbnc`            | 2.0.2-2019.04.28 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_antbnc_en_2.0.2_2.4_1556480454569.zip)            |
| PerceptronModel (POS)                    | `pos_anc`                 | 2.0.2-2019.04.30 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_anc_en_2.0.2_2.4_1556659930154.zip)                 |
| NerCrfModel (NER with GloVe)             | `ner_crf`                 | 2.0.2-2019.04.30 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_crf_en_2.0.2_2.4_1556652790378.zip)                 |
| NerDLModel (NER with GloVe)              | `ner_dl`                  | 2.0.2-2019.05.25 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_en_2.0.2_2.4_1558802205173.zip)                  |
| NerDLModel (NER with GloVe)              | `ner_dl_contrib`          | 2.0.2-2019.04.29 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_contrib_en_2.0.2_2.4_1556501490317.zip)          |
| NerDLModel (NER with BERT)               | `ner_dl_bert_base_cased`  | 2.2.2-2019.09.07 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_bert_base_cased_en_2.2.0_2.4_1567854461249.zip)  |
| NerDLModel (OntoNotes with GloVe 100d)   | `onto_100`                | 2.1.0-2019.07.27 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_100_en_2.1.0_2.4_1564256329924.zip)                |
| NerDLModel (OntoNotes with GloVe 300d)   | `onto_300`                | 2.1.0-2019.07.27 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_300_en_2.1.0_2.4_1564256072129.zip)                |
| WordEmbeddings (GloVe)                   | `glove_100d`              | 2.0.2-2019.04.29 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/glove_100d_en_2.0.2_2.4_1556534397055.zip)              |
| BertEmbeddings (base_uncased)            | `bert_base_uncased`       | 2.2.0-2019.08.24 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_base_uncased_en_2.2.0_2.4_1566671691653.zip)       |
| BertEmbeddings (base_cased)              | `bert_base_cased`         | 2.2.0-2019.08.24 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_base_cased_en_2.2.0_2.4_1566671427398.zip)         |
| BertEmbeddings (large_uncased)           | `bert_large_uncased`      | 2.2.0-2019.08.24 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_large_uncased_en_2.2.0_2.4_1566673292025.zip)      |
| BertEmbeddings (large_cased)             | `bert_large_cased`        | 2.2.0-2019.08.24 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_large_cased_en_2.2.0_2.4_1566672045674.zip)        |
| DeepSentenceDetector                     | `ner_dl_sentence`         | 2.0.2-2019.04.30 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_sentence_en_2.0.2_2.4_1556666842347.zip)         |
| SymmetricDeleteModel (Spell Checker)     | `spellcheck_sd`           | 2.0.2-2019.04.30 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/spellcheck_sd_en_2.0.2_2.4_1556604489934.zip)           |
| NorvigSweetingModel (Spell Checker)      | `spellcheck_norvig`       | 2.0.2-2019.04.30 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/spellcheck_norvig_en_2.0.2_2.4_1556605026653.zip)       |
| ViveknSentimentModel (Sentiment)         | `sentiment_vivekn`        | 2.0.2-2019.04.30 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentiment_vivekn_en_2.0.2_2.4_1556663184035.zip)        |
| DependencyParser (Dependency)            | `dependency_conllu`       | 2.0.8-2019.06.25 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_conllu_en_2.0.8_2.4_1561435004077.zip)       |
| TypedDependencyParser (Dependency)       | `dependency_typed_conllu` | 2.0.8-2019.06.25 |             |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_typed_conllu_en_2.0.8_2.4_1561473259215.zip) |

### French - Models

| Model                        | Name               | Build | Notes | Description | Offline                                                                                                                                                                                                |
|:-----------------------------|:-------------------|:------|:------|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer) | `lemma`            |       |       | 2.0.2-2019.04.29 | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_fr_2.0.2_2.4_1556531462843.zip)                                                                                       |
| PerceptronModel (POS UD)     | `pos_ud_gsd`       |       |       | 2.0.2-2019.04.29 | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_gsd_fr_2.0.2_2.4_1556531457346.zip)                                                                                  |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` |       |       | 2.1.0-2019.07.13 | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_fr_2.1.0_2.4_1563035043013.zip)                                                                            |

| Feature   | Description                                                                                                                                                                                            |    |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---|
| **Lemma** | Trained by **Lemmatizer** annotator on **lemmatization-lists** by `Michal Měchura`                                                                                                                     |    |
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/fr_gsd/index.html)                                                             |    |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |    |

### German - Models

| Model                        | Name               | Build            | Notes | Description | Offline                                                                                                                                                                                                |
|:-----------------------------|:-------------------|:-----------------|:------|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.0.8-2019.06.23 |       |             | [de](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_de_2.0.8_2.4_1561248996126.zip)                                                                                             |
| PerceptronModel (POS UD)     | `pos_ud_hdt`       | 2.0.8-2019.06.22 |       |             | [de](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_hdt_de_2.0.8_2.4_1561232528570.zip)                                                                                        |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` | 2.1.0-2019.07.13 |       |             | [de](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_de_2.1.0_2.4_1563035544700.zip)                                                                                  |

| Feature   | Description                                                                                                                                                                                            |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lemma** | Trained by **Lemmatizer** annotator on **lemmatization-lists** by `Michal Měchura`                                                                                                                     |
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/de_hdt/index.html)                                                             |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |

### Italian - Models

| Model                         | Name               | Build            | Notes | Description | Offline                                                                                                                     |
|:------------------------------|:-------------------|:-----------------|:------|:------------|:----------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer)  | `lemma_dxc`        | 2.0.2-2019.04.29 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_dxc_it_2.0.2_2.4_1556531469058.zip)        |
| SentimentDetector (Sentiment) | `sentiment_dxc`    | 2.0.2-2019.04.29 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentiment_dxc_it_2.0.2_2.4_1556531477694.zip)    |
| PerceptronModel (POS UD)      | `pos_ud_isdt`      | 2.0.8-2019.06.10 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_isdt_it_2.0.8_2.4_1560168427464.zip)      |
| NerDLModel (glove_840B_300)   | `wikiner_840B_300` | 2.1.0-2019.07.14 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_it_2.1.0_2.4_1563095099139.zip) |

| Feature   | Description                                                                                                                                                                                            |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lemma** | Trained by **Lemmatizer** annotator on **DXC Technology** dataset                                                                                                                                      |
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/it_isdt/index.html)                                                            |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |

### Multi-language

| Model                        | Name               | Build            | Notes | Description                                                                                                                 | Offline |
|:-----------------------------|:-------------------|:-----------------|:------|:----------------------------------------------------------------------------------------------------------------------------|:--------|
| WordEmbeddings (GloVe)       | `glove_840B_300`   | 2.0.2-2019.05.23 |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/glove_840B_300_xx_2.0.2_2.4_1558645003344.zip)   |         |
| WordEmbeddings (GloVe)       | `glove_6B_300`     | 2.0.2-2019.05.28 |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/glove_6B_300_xx_2.0.2_2.4_1559059806004.zip)     |         |
| BertEmbeddings (multi_cased) | `bert_multi_cased` | 2.2.0-2019.08.24 |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_multi_cased_xx_2.2.0_2.4_1566674716493.zip) |         |

## Pretrained Pipelines
### English - Pipelines

**NOTE:**
`noncontrib` pipelines are compatible with `Windows` operating systems.

| Pipeline                     | Name                                  | Build            | Notes | Description | Offline                                                                                                                                        |
|:-----------------------------|:--------------------------------------|:-----------------|:------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| Explain Document ML          | `explain_document_ml`                 | 2.1.0-2019.07.15 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_ml_en_2.1.0_2.4_1563203154682.zip)                 |
| Explain Document DL          | `explain_document_dl`                 | 2.1.0-2019.08.02 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_dl_en_2.1.0_2.4_1564764767733.zip)                 |
| Explain Document DL Win      | `explain_document_dl_noncontrib`      | 2.1.0-2019.08.02 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_dl_noncontrib_en_2.1.0_2.4_1564764344071.zip)      |
| Explain Document DL Fast     | `explain_document_dl_fast`            | 2.1.0-2019.07.12 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_dl_fast_en_2.1.0_2.4_1562946519404.zip)            |
| Explain Document DL Fast Win | `explain_document_dl_fast_noncontrib` | 2.1.0-2019.07.12 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_dl_fast_noncontrib_en_2.1.0_2.4_1562954323015.zip) |
| Recognize Entities DL        | `recognize_entities_dl`               | 2.1.0-2019.07.12 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/recognize_entities_dl_en_2.1.0_2.4_1562946909722.zip)               |
| Recognize Entities DL Win    | `recognize_entities_dl_noncontrib`    | 2.1.0-2019.07.12 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/recognize_entities_dl_noncontrib_en_2.1.0_2.4_1562954722690.zip)    |
| OntoNotes Entities Small     | `onto_recognize_entities_sm`          | 2.1.0-2019.07.28 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_recognize_entities_sm_en_2.1.0_2.4_1564330931782.zip)          |
| OntoNotes Entities Large     | `onto_recognize_entities_lg`          | 2.1.0-2019.07.28 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_recognize_entities_lg_en_2.1.0_2.4_1564339796549.zip)          |
| Match Datetime               | `match_datetime`                      | 2.1.0-2019.07.12 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_datetime_en_2.1.0_2.4_1562944300214.zip)                      |
| Match Pattern                | `match_pattern`                       | 2.1.0-2019.07.12 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_pattern_en_2.1.0_2.4_1562944301080.zip)                       |
| Match Chunk                  | `match_chunks`                        | 2.2.0-2019.09.10 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_chunks_en_2.2.0_2.4_1568121171238.zip)                        |
| Match Phrases                | `match_phrases`                       | 2.1.0-2019.07.12 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_phrases_en_2.1.0_2.4_1562944304428.zip)                       |
| Clean Stop                   | `clean_stop`                          | 2.1.0-2019.07.12 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clean_stop_en_2.1.0_2.4_1562944303490.zip)                          |
| Clean Pattern                | `clean_pattern`                       | 2.1.0-2019.07.12 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clean_pattern_en_2.1.0_2.4_1562944302303.zip)                       |
| Clean Slang                  | `clean_slang`                         | 2.1.0-2019.07.12 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clean_slang_en_2.1.0_2.4_1562944852594.zip)                         |
| Check Spelling               | `check_spelling`                      | 2.1.0-2019.07.12 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/check_spelling_en_2.1.0_2.4_1562944297070.zip)                      |
| Analyze Sentiment            | `analyze_sentiment`                   | 2.1.0-2019.07.15 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/analyze_sentiment_en_2.1.0_2.4_1563204637489.zip)                   |
| Dependency Parse             | `dependency_parse`                    | 2.1.0-2019.07.15 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_parse_en_2.1.0_2.4_1563224147733.zip)                    |

### French - Pipelines

| Pipeline                 | Name                   | Build            | Notes | Description                                                                                                                     | Offline |
|:-------------------------|:-----------------------|:-----------------|:------|:--------------------------------------------------------------------------------------------------------------------------------|:--------|
| Explain Document Large   | `explain_document_lg`  | 2.1.0-2019.07.15 |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_fr_2.1.0_2.4_1563178528241.zip)  |         |
| Explain Document Medium  | `explain_document_md`  | 2.1.0-2019.07.15 |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_fr_2.1.0_2.4_1563180522434.zip)  |         |
| Entity Recognizer Large  | `entity_recognizer_lg` | 2.1.0-2019.07.15 |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_fr_2.1.0_2.4_1563180776696.zip) |         |
| Entity Recognizer Medium | `entity_recognizer_md` | 2.1.0-2019.07.15 |       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_fr_2.1.0_2.4_1563182745366.zip) |         |

### Italian - Pipelines

| Pipeline                 | Name                   | Build            | Notes | Description | Offline                                                                                                                         |
|:-------------------------|:-----------------------|:-----------------|:------|:------------|:--------------------------------------------------------------------------------------------------------------------------------|
| Explain Document Large   | `explain_document_lg`  | 2.1.0-2019.07.15 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_it_2.1.0_2.4_1563183013508.zip)  |
| Explain Document Medium  | `explain_document_md`  | 2.1.0-2019.07.15 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_it_2.1.0_2.4_1563184262421.zip)  |
| Entity Recognizer Large  | `entity_recognizer_lg` | 2.1.0-2019.07.15 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_it_2.1.0_2.4_1563184543759.zip) |
| Entity Recognizer Medium | `entity_recognizer_md` | 2.1.0-2019.07.15 |       |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_it_2.1.0_2.4_1563186026810.zip) |

# Licensed Enterprise

`pretrained(name, lang)` function to use

## Pretrained Models - Spark NLP For Healthcare
### English

It is required to specify 3rd argument to `pretrained(name, lang, loc)` function (location) to add the location of these

| Model                    | Name                       | Build            | Notes | Description | location        |
|:-------------------------|:---------------------------|:-----------------|:------|:------------|:----------------|
| NerDLModel               | `ner_clinical`             | 2.0.2-2019.04.30 |       |             | clinical/models |
| NerDLModel               | `ner_clinical_noncontrib`  | 2.3.0-2019.11.14 |       |             | clinical/models |
| NerDLModel               | `ner_bionlp`               | 2.3.4-2019.11.27 |       |             | clinical/models |
| NerDLModel               | `ner_bionlp_noncontrib`    | 2.3.4-2019.11.27 |       |             | clinical/models |
| NerDLModel               | `deidentify_dl`            | 2.0.2-2019.06.04 |       |             | clinical/models |
| AssertionDLModel         | `assertion_dl`             | 2.0.2-2019.04.30 |       |             | clinical/models |
| AssertionLogRegModel     | `assertion_ml`             | 2.0.2-2019.04.30 |       |             | clinical/models |
| DeIdentificationModel    | `deidentify_rb`            | 2.0.2-2019.06.04 |       |             | clinical/models |
| WordEmbeddingsModel      | `embeddings_clinical`      | 2.0.2-2019.05.21 |       |             | clinical/models |
| WordEmbeddingsModel      | `embeddings_icdoem`        | 2.3.2-2019.11.12 |       |             | clinical/models |
| BertEmbeddingsModel      | `biobert_pubmed_cased`     | 2.3.1-2019.11.23 |       |             | clinical/models |
| BertEmbeddingsModel      | `biobert_pmc_cased`        | 2.3.1-2019.11.23 |       |             | clinical/models |
| BertEmbeddingsModel      | `biobert_pubmed_pmc_cased` | 2.3.1-2019.11.23 |       |             | clinical/models |
| BertEmbeddingsModel      | `biobert_clinical_cased`   | 2.3.1-2019.11.23 |       |             | clinical/models |
| BertEmbeddingsModel      | `biobert_discharge_cased`  | 2.3.1-2019.11.23 |       |             | clinical/models |
| PerceptronModel          | `pos_clinical`             | 2.0.2-2019.04.30 |       |             | clinical/models |
| EntityResolverModel      | `resolve_icd10`            | 2.0.2-2019.06.05 |       |             | clinical/models |
| EntityResolverModel      | `resolve_icd10cm_cl_em`    | 2.0.8-2019.06.28 |       |             | clinical/models |
| EntityResolverModel      | `resolve_icd10cm_cl_em`    | 2.1.0-2019.07.15 |       |             | clinical/models |
| EntityResolverModel      | `resolve_icd10cm_icdoem`   | 2.3.2-2019.11.13 |       |             | clinical/models |
| EntityResolverModel      | `resolve_cpt_icdoem`       | 2.3.2-2019.11.13 |       |             | clinical/models |
| EntityResolverModel      | `resolve_icdo_icdoem`      | 2.3.2-2019.11.14 |       |             | clinical/models |
| ContextSpellCheckerModel | `spellcheck_dl`            | 2.2.2-2019.11.12 |       |             | clinical/models |
| TextMatcherModel         | `textmatch_icdo_ner_n2c4`  | 2.3.3-2019.11.22 |       |             | clinical/models |
| TextMatcherModel         | `textmatch_cpt_token_n2c1` | 2.3.3-2019.11.25 |       |             | clinical/models |
| Disambiguator            | `people_disambiguator`     | 2.3.4-2019.11.27 |       |             | clinical/models |
| ChunkEntityResolverModel | `chunkresolve_icdo_icdoem` | 2.3.3-2019.11.25 |       |             | clinical/models |
| ChunkEntityResolverModel | `chunkresolve_cpt_icdoem`  | 2.3.3-2019.11.25 |       |             | clinical/models |

## Contact

nlp@johnsnowlabs.com

## John Snow Labs

[http://johnsnowlabs.com](http://johnsnowlabs.com)
