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

| Model                                    | Name                      | Build | Details | Offline                                                                                                                            |
|:-----------------------------------------|:--------------------------|:------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer)             | `lemma_antbnc`            |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_antbnc_en_2.0.2_2.4_1556480454569.zip)            |
| PerceptronModel (POS)                    | `pos_anc`                 |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_anc_en_2.0.2_2.4_1556659930154.zip)                 |
| NerCrfModel (NER with GloVe)             | `ner_crf`                 |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_crf_en_2.0.2_2.4_1556652790378.zip)                 |
| NerDLModel (NER with GloVe)              | `ner_dl`                  |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_en_2.0.2_2.4_1558802205173.zip)                  |
| NerDLModel (NER with GloVe)              | `ner_dl_contrib`          |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_contrib_en_2.0.2_2.4_1556501490317.zip)          |
| NerDLModel (NER with BERT)               | `ner_dl_bert_base_cased`  |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_bert_base_cased_en_2.2.0_2.4_1567854461249.zip)  |
| NerDLModel (OntoNotes with GloVe 100d)   | `onto_100`                |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_100_en_2.1.0_2.4_1564256329924.zip)                |
| NerDLModel (OntoNotes with GloVe 300d)   | `onto_300`                |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_300_en_2.1.0_2.4_1564256072129.zip)                |
| WordEmbeddings (GloVe)                   | `glove_100d`              |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/glove_100d_en_2.0.2_2.4_1556534397055.zip)              |
| BertEmbeddings (base_uncased)            | `bert_base_uncased`       |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_base_uncased_en_2.2.0_2.4_1566671691653.zip)       |
| BertEmbeddings (base_cased)              | `bert_base_cased`         |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_base_cased_en_2.2.0_2.4_1566671427398.zip)         |
| BertEmbeddings (large_uncased)           | `bert_large_uncased`      |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_large_uncased_en_2.2.0_2.4_1566673292025.zip)      |
| BertEmbeddings (large_cased)             | `bert_large_cased`        |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_large_cased_en_2.2.0_2.4_1566672045674.zip)        |
| DeepSentenceDetector                     | `ner_dl_sentence`         |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_sentence_en_2.0.2_2.4_1556666842347.zip)         |
| ContextSpellCheckerModel (Spell Checker) | `spellcheck_dl`           |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/spellcheck_dl_en_2.0.2_2.4_1556479898829.zip)           |
| SymmetricDeleteModel (Spell Checker)     | `spellcheck_sd`           |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/spellcheck_sd_en_2.0.2_2.4_1556604489934.zip)           |
| NorvigSweetingModel (Spell Checker)      | `spellcheck_norvig`       |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/spellcheck_norvig_en_2.0.2_2.4_1556605026653.zip)       |
| ViveknSentimentModel (Sentiment)         | `sentiment_vivekn`        |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentiment_vivekn_en_2.0.2_2.4_1556663184035.zip)        |
| DependencyParser (Dependency)            | `dependency_conllu`       |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_conllu_en_2.0.8_2.4_1561435004077.zip)       |
| TypedDependencyParser (Dependency)       | `dependency_typed_conllu` |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_typed_conllu_en_2.0.8_2.4_1561473259215.zip) |

### French - Models

| Model                        | Name               | Build | Details | Offline                                                                                                                     |
|:-----------------------------|:-------------------|:------|:--------|:----------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer) | `lemma`            |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_fr_2.0.2_2.4_1556531462843.zip)            |
| PerceptronModel (POS UD)     | `pos_ud_gsd`       |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_gsd_fr_2.0.2_2.4_1556531457346.zip)       |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_fr_2.1.0_2.4_1563035043013.zip) |

|Feature | Description|
|---|----|
|**Lemma**|Trained by **Lemmatizer** annotator on **lemmatization-lists** by `Michal Měchura`
|**POS**| Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/fr_gsd/index.html)
|**NER**|Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities

### German - Models

| Model                        | Name               | Build | Details | Offline                                                                                                               |
|:-----------------------------|:-------------------|:------|:--------|:----------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer) | `lemma`            |       |         | [de](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_de_2.0.8_2.4_1561248996126.zip)            |
| PerceptronModel (POS UD)     | `pos_ud_hdt`       |       |         | [de](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_hdt_de_2.0.8_2.4_1561232528570.zip)       |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` |       |         | [de](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_de_2.1.0_2.4_1563035544700.zip) |

|Feature | Description|
|---|----|
|**Lemma**|Trained by **Lemmatizer** annotator on **lemmatization-lists** by `Michal Měchura`
|**POS**| Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/de_hdt/index.html)
|**NER**|Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities

### Italian - Models

| Model                         | Name               | Build | Details | Offline                                                                                                                     |
|:------------------------------|:-------------------|:------|:--------|:----------------------------------------------------------------------------------------------------------------------------|
| LemmatizerModel (Lemmatizer)  | `lemma_dxc`        |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_dxc_it_2.0.2_2.4_1556531469058.zip)        |
| SentimentDetector (Sentiment) | `sentiment_dxc`    |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentiment_dxc_it_2.0.2_2.4_1556531477694.zip)    |
| PerceptronModel (POS UD)      | `pos_ud_isdt`      |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_isdt_it_2.0.8_2.4_1560168427464.zip)      |
| NerDLModel (glove_840B_300)   | `wikiner_840B_300` |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_it_2.1.0_2.4_1563095099139.zip) |

|Feature | Description|
|---|----|
|**Lemma**|Trained by **Lemmatizer** annotator on **DXC Technology** dataset
|**POS**| Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/it_isdt/index.html)
|**NER**|Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities

### Multi-language

| Model                        | Name               | Build | Details | Offline                                                                                                                     |
|:-----------------------------|:-------------------|:------|:--------|:----------------------------------------------------------------------------------------------------------------------------|
| WordEmbeddings (GloVe)       | `glove_840B_300`   |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/glove_840B_300_xx_2.0.2_2.4_1558645003344.zip)   |
| WordEmbeddings (GloVe)       | `glove_6B_300`     |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/glove_6B_300_xx_2.0.2_2.4_1559059806004.zip)     |
| BertEmbeddings (multi_cased) | `bert_multi_cased` |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_multi_cased_xx_2.2.0_2.4_1566674716493.zip) |

## Pretrained Pipelines
### English - Pipelines

**NOTE:**
`noncontrib` pipelines are compatible with `Windows` operating systems.

| Pipeline                     | Name                                  | Build | Details | Offline                                                                                                                                        |
|:-----------------------------|:--------------------------------------|:------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| Explain Document ML          | `explain_document_ml`                 |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_ml_en_2.1.0_2.4_1563203154682.zip)                 |
| Explain Document DL          | `explain_document_dl`                 |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_dl_en_2.1.0_2.4_1564764767733.zip)                 |
| Explain Document DL Win      | `explain_document_dl_noncontrib`      |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_dl_noncontrib_en_2.1.0_2.4_1564764344071.zip)      |
| Explain Document DL Fast     | `explain_document_dl_fast`            |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_dl_fast_en_2.1.0_2.4_1562946519404.zip)            |
| Explain Document DL Fast Win | `explain_document_dl_fast_noncontrib` |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_dl_fast_noncontrib_en_2.1.0_2.4_1562954323015.zip) |
| Recognize Entities DL        | `recognize_entities_dl`               |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/recognize_entities_dl_en_2.1.0_2.4_1562946909722.zip)               |
| Recognize Entities DL Win    | `recognize_entities_dl_noncontrib`    |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/recognize_entities_dl_noncontrib_en_2.1.0_2.4_1562954722690.zip)    |
| OntoNotes Entities Small     | `onto_recognize_entities_sm`          |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_recognize_entities_sm_en_2.1.0_2.4_1564330931782.zip)          |
| OntoNotes Entities Large     | `onto_recognize_entities_lg`          |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_recognize_entities_lg_en_2.1.0_2.4_1564339796549.zip)          |
| Match Datetime               | `match_datetime`                      |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_datetime_en_2.1.0_2.4_1562944300214.zip)                      |
| Match Pattern                | `match_pattern`                       |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_pattern_en_2.1.0_2.4_1562944301080.zip)                       |
| Match Chunk                  | `match_chunks`                        |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_chunks_en_2.2.0_2.4_1568121171238.zip)                        |
| Match Phrases                | `match_phrases`                       |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_phrases_en_2.1.0_2.4_1562944304428.zip)                       |
| Clean Stop                   | `clean_stop`                          |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clean_stop_en_2.1.0_2.4_1562944303490.zip)                          |
| Clean Pattern                | `clean_pattern`                       |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clean_pattern_en_2.1.0_2.4_1562944302303.zip)                       |
| Clean Slang                  | `clean_slang`                         |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clean_slang_en_2.1.0_2.4_1562944852594.zip)                         |
| Check Spelling               | `check_spelling`                      |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/check_spelling_en_2.1.0_2.4_1562944297070.zip)                      |
| Analyze Sentiment            | `analyze_sentiment`                   |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/analyze_sentiment_en_2.1.0_2.4_1563204637489.zip)                   |
| Dependency Parse             | `dependency_parse`                    |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_parse_en_2.1.0_2.4_1563224147733.zip)                    |

### French - Pipelines

| Pipeline                 | Name                       | Build | Details | Offline                                                                                                                         |
|:-------------------------|:---------------------------|:------|:--------|:--------------------------------------------------------------------------------------------------------------------------------|
| Explain Document Large   | `explain_document_lg`      |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_fr_2.1.0_2.4_1563178528241.zip)  |
| Explain Document Medium  | `explain_document_md`      |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_fr_2.1.0_2.4_1563180522434.zip)  |
| Entity Recognizer Large  | `entity_recognizer_lg`     |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_fr_2.1.0_2.4_1563180776696.zip) |
| Entity Recognizer Medium | `entity_recognizer_md`     |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_fr_2.1.0_2.4_1563182745366.zip) |

### Italian - Pipelines

| Pipeline                 | Name                        | Build | Details | Offline                                                                                                                         |
|:-------------------------|:----------------------------|:------|:--------|:--------------------------------------------------------------------------------------------------------------------------------|
| Explain Document Large   | `explain_document_lg`       |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_it_2.1.0_2.4_1563183013508.zip)  |
| Explain Document Medium  | `explain_document_md`       |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_it_2.1.0_2.4_1563184262421.zip)  |
| Entity Recognizer Large  | `entity_recognizer_lg`      |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_it_2.1.0_2.4_1563184543759.zip) |
| Entity Recognizer Medium | `entity_recognizer_md`      |       |         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_it_2.1.0_2.4_1563186026810.zip) |

# Licensed Enterprise

`pretrained(name, lang)` function to use

## Pretrained Models - Spark NLP For Healthcare
### English

It is required to specify 3rd argument to `pretrained(name, lang, loc)` function (location) to add the location of these

| Model                    | Name                       | Build | Details | Offline         |
|:-------------------------|:---------------------------|:------|:--------|:----------------|
| NerDLModel               | `ner_clinical`             |       | en      | clinical/models |
| AssertionLogRegModel     | `assertion_ml`             |       | en      | clinical/models |
| AssertionDLModel         | `assertion_dl`             |       | en      | clinical/models |
| NerDLModel               | `deidentify_dl`            |       | en      | clinical/models |
| DeIdentificationModel    | `deidentify_rb`            |       | en      | clinical/models |
| WordEmbeddingsModel      | `embeddings_clinical`      |       | en      | clinical/models |
| BertEmbeddingsModel      | `biobert_pubmed_cased`     |       | en      | clinical/models |
| BertEmbeddingsModel      | `biobert_pmc_cased`        |       | en      | clinical/models |
| BertEmbeddingsModel      | `biobert_pubmed_pmc_cased` |       | en      | clinical/models |
| BertEmbeddingsModel      | `biobert_clinical_cased`   |       | en      | clinical/models |
| BertEmbeddingsModel      | `biobert_discharge_cased`  |       | en      | clinical/models |
| PerceptronModel          | `pos_clinical`             |       | en      | clinical/models |
| EntityResolverModel      | `resolve_icd10`            |       | en      | clinical/models |
| EntityResolverModel      | `resolve_icd10cm_cl_em`    |       | en      | clinical/models |
| EntityResolverModel      | `resolve_icd10pcs_cl_em`   |       | en      | clinical/models |
| ContextSpellCheckerModel | `context_spell_med`        |       | en      | clinical/models |

## Contact

nlp@johnsnowlabs.com

## John Snow Labs

[http://johnsnowlabs.com](http://johnsnowlabs.com)
