<a href="https://johnsnowlabs.com"><img src="https://www.johnsnowlabs.com/wp-content/uploads/2020/03/johnsnowlabs-square.png" width="125" height="125" align="right" /></a>

# Spark NLP Models

[![Build Status](https://travis-ci.org/JohnSnowLabs/spark-nlp.svg?branch=master)](https://travis-ci.org/JohnSnowLabs/spark-nlp) [![Maven Central](https://maven-badges.herokuapp.com/maven-central/com.johnsnowlabs.nlp/spark-nlp_2.11/badge.svg)](https://search.maven.org/artifact/com.johnsnowlabs.nlp/spark-nlp_2.11) [![PyPI version](https://badge.fury.io/py/spark-nlp.svg)](https://badge.fury.io/py/spark-nlp) [![Anaconda-Cloud](https://anaconda.org/johnsnowlabs/spark-nlp/badges/version.svg)](https://anaconda.org/JohnSnowLabs/spark-nlp) [![License](https://img.shields.io/badge/License-Apache%202.0-brightgreen.svg)](https://github.com/JohnSnowLabs/spark-nlp/blob/master/LICENSE)

We use this repository to maintain our releases of pre-trained pipelines and models for the Spark NLP library. For more info please take a look at our [releases](https://github.com/JohnSnowLabs/spark-nlp-models/releases).

## Project's website

Take a look at our official Spark NLP page: [http://nlp.johnsnowlabs.com/](http://nlp.johnsnowlabs.com/) for user documentation and examples

## Slack community channel

[Join Slack](https://join.slack.com/t/spark-nlp/shared_invite/enQtNjA4MTE2MDI1MDkxLTM4ZDliMjU5OWZmMDE1ZGVkMjg0MWFjMjU3NjY4YThlMTJkNmNjNjM3NTMwYzlhMWY4MGMzODI2NDBkOWU4ZDE)

## Table of contents

* [Pretrained Pipelines](#pretrained-pipelines)
  * [Public Pipelines](#public-pipelines)
    * [Dutch](#dutch---pipelines)
    * [English](#english---pipelines)
    * [French](#french---pipelines)
    * [German](#german---pipelines)
    * [Italian](#italian---pipelines)
    * [Norwegian](#norwegian---pipelines)
    * [Polish](#polish---pipelines)
    * [Portuguese](#portuguese---pipelines)
    * [Russian](#russian---pipelines)
    * [Spanish](#spanish---pipelines)

* [Pretrained Models](#pretrained-models)
  * [Public Models](#public-models)
    * [Dutch](#dutch---models)
    * [English](#english---models)
    * [French](#french---models)
    * [German](#german---models)
    * [Italian](#italian---models)
    * [Norwegian](#norwegian---models)
    * [Polish](#polish---models)
    * [Portuguese](#portuguese---models)
    * [Russian](#russian---models)
    * [Spanish](#spanish---models)
    * [Bulgarian](#bulgarian---models)
    * [Czech](#czech---models)
    * [Greek](#greek---models)
    * [Finnish](#finnish---models)
    * [Hungarian](#Hungarian---models)
    * [Romanian](#romanian---models)
    * [Slovak](#slovak---models)
    * [Swedish](#swedish---models)
    * [Turkish](#turkish---models)
    * [Ukrainian](#ukrainian---models)
    * [Multi-language](#multi-language)

* [Licensed Enterprise](#licensed-enterprise)
  
# Pretrained Pipelines

Example of how to use Spark NLP pretrained pipelines:

```python
# Import Spark NLP
from sparknlp.base import *
from sparknlp.annotator import *

from sparknlp.pretrained import PretrainedPipeline
import sparknlp

# Start Spark Session with Spark NLP
spark = sparknlp.start()

# Download a pre-trained pipeline
pipeline = PretrainedPipeline('explain_document_dl', lang='en')

# Your testing dataset
text = """
The Mona Lisa is a 16th century oil painting created by Leonardo. 
It's held at the Louvre in Paris.
"""

# Annotate your testing dataset
result = pipeline.annotate(text)

# What's in the pipeline
list(result.keys())
Output: ['entities', 'stem', 'checked', 'lemma', 'document',
'pos', 'token', 'ner', 'embeddings', 'sentence']

# Check the results
result['entities']
Output: ['Mona Lisa', 'Leonardo', 'Louvre', 'Paris']

```

## Public Pipelines

### Dutch - Pipelines

| Pipeline                 | Name                   | Build  | lang | Description | Offline   |
|:-------------------------|:-----------------------|:-------|:-------|:----------|:----------|
| Explain Document Small    | `explain_document_sm`  | 2.5.0 |   `nl` |           | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_sm_nl_2.5.0_2.4_1588546621618.zip)  |
| Explain Document Medium   | `explain_document_md`  | 2.5.0 |   `nl` |           | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_nl_2.5.0_2.4_1588546605329.zip)  |
| Explain Document Large    | `explain_document_lg`  | 2.5.0 |   `nl` |           | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_nl_2.5.0_2.4_1588612556770.zip)  |
| Entity Recognizer Small   | `entity_recognizer_sm`  | 2.5.0 |   `nl` |          | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_sm_nl_2.5.0_2.4_1588546655907.zip)  |
| Entity Recognizer Medium  | `entity_recognizer_md`  | 2.5.0 |   `nl` |          | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_nl_2.5.0_2.4_1588546645304.zip)  |
| Entity Recognizer Large   | `entity_recognizer_lg`  | 2.5.0 |   `nl` |          | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_nl_2.5.0_2.4_1588612569958.zip)  |  

### English - Pipelines

| Pipeline                     | Name                                  | Build            | lang | Description | Offline|
|:-------------------------|:-------------------|:------|:-------|:------------|:------------------|
| Explain Document ML          | `explain_document_ml`                 | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_ml_en_2.4.0_2.4_1580252705962.zip) |
| Explain Document DL          | `explain_document_dl`                 | 2.4.3 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_dl_en_2.4.3_2.4_1584626657780.zip) |
| Recognize Entities DL        | `recognize_entities_dl`               | 2.4.3 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/recognize_entities_dl_en_2.4.3_2.4_1584626752821.zip) |
| Recognize Entities DL        | `recognize_entities_bert`             | 2.4.3 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/recognize_entities_bert_en_2.4.3_2.4_1584626853422.zip) |
| OntoNotes Entities Small     | `onto_recognize_entities_sm`          | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_recognize_entities_sm_en_2.4.0_2.4_1579730599257.zip) |
| OntoNotes Entities Large     | `onto_recognize_entities_lg`          | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_recognize_entities_lg_en_2.4.0_2.4_1579729320751.zip) |
| Match Datetime               | `match_datetime`                      | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_datetime_en_2.4.0_2.4_1580246861565.zip) |
| Match Pattern                | `match_pattern`                       | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_pattern_en_2.4.0_2.4_1582247694074.zip) |
| Match Chunk                  | `match_chunks`                        | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_chunks_en_2.4.0_2.4_1580246868138.zip) |
| Match Phrases                | `match_phrases`                       | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/match_phrases_en_2.4.0_2.4_1580255815623.zip)|
| Clean Stop                   | `clean_stop`                          | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clean_stop_en_2.4.0_2.4_1580255705789.zip)|
| Clean Pattern                | `clean_pattern`                       | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clean_pattern_en_2.4.0_2.4_1580246862642.zip)|
| Clean Slang                  | `clean_slang`                         | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clean_slang_en_2.4.0_2.4_1580255816146.zip)|
| Check Spelling               | `check_spelling`                      | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/check_spelling_en_2.4.0_2.4_1580246859135.zip)|
| Check Spelling DL            | `check_spelling_dl`                   | 2.5.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/check_spelling_dl_en_2.5.0_2.4_1589015487144.zip)|
| Analyze Sentiment            | `analyze_sentiment`                   | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/analyze_sentiment_en_2.4.0_2.4_1580483464667.zip)|
| Analyze Sentiment DL         | `analyze_sentimentdl_use_imdb`        | 2.5.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/analyze_sentimentdl_use_imdb_en_2.5.0_2.4_1589108067729.zip)|
| Analyze Sentiment DL         | `analyze_sentimentdl_use_twitter`     | 2.5.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/analyze_sentimentdl_use_twitter_en_2.5.0_2.4_1589108892106.zip)|
| Dependency Parse             | `dependency_parse`                    | 2.4.0 |   `en`    |      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_parse_en_2.4.0_2.4_1580255669655.zip)|

### French - Pipelines

| Pipeline                 | Name                   | Build            | lang | Description | Offline |
|:-------------------------|:-------------------|:------|:-------|:------------|:------------------|
| Explain Document Large   | `explain_document_lg`  | 2.4.0 |   `fr`| |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_fr_2.4.0_2.4_1579709189947.zip)  |
| Explain Document Medium  | `explain_document_md`  | 2.4.0 |   `fr`| |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_fr_2.4.0_2.4_1579722754344.zip)  |
| Entity Recognizer Large  | `entity_recognizer_lg` | 2.4.0 |   `fr`| |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_fr_2.4.0_2.4_1579710310593.zip) |
| Entity Recognizer Medium | `entity_recognizer_md` | 2.4.0 |   `fr`| |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_fr_2.4.0_2.4_1579722764594.zip) |

### German - Pipelines

| Pipeline                 | Name                   | Build         | lang | Description | Offline|
|:-------------------------|:-------------------|:------|:-------|:------------|:------------------|
| Explain Document Large   | `explain_document_lg`  | 2.4.0 |  `de` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_de_2.4.0_2.4_1579722852211.zip)  |
| Explain Document Medium  | `explain_document_md`  | 2.4.0 |  `de` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_de_2.4.0_2.4_1579722872528.zip)  |
| Entity Recognizer Large  | `entity_recognizer_lg` | 2.4.0 |  `de` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_de_2.4.0_2.4_1579722883057.zip) |
| Entity Recognizer Medium | `entity_recognizer_md` | 2.4.0 |  `de` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_de_2.4.0_2.4_1579722895254.zip) |

### Italian - Pipelines

| Pipeline                 | Name                   | Build          | lang | Description | Offline|
|:-------------------------|:-------------------|:------|:-------|:------------|:------------------|
| Explain Document Large   | `explain_document_lg`  | 2.4.0 |   `it` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_it_2.4.0_2.4_1579722789680.zip)  |
| Explain Document Medium  | `explain_document_md`  | 2.4.0 |   `it` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_it_2.4.0_2.4_1579722813892.zip)  |
| Entity Recognizer Large  | `entity_recognizer_lg` | 2.4.0 |   `it` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_it_2.4.0_2.4_1579722823718.zip) |
| Entity Recognizer Medium | `entity_recognizer_md` | 2.4.0 |   `it` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_it_2.4.0_2.4_1579722834033.zip) |

### Norwegian - Pipelines

| Pipeline                 | Name                   | Build  | lang | Description | Offline   |
|:-------------------------|:-----------------------|:-------|:-------|:----------|:----------|
| Explain Document Small    | `explain_document_sm`  | 2.5.0 |   `no` |           | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_sm_no_2.5.0_2.4_1588784132955.zip)  |
| Explain Document Medium   | `explain_document_md`  | 2.5.0 |   `no` |           | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_no_2.5.0_2.4_1588783879809.zip)  |
| Explain Document Large    | `explain_document_lg`  | 2.5.0 |   `no` |           | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_no_2.5.0_2.4_1588782610672.zip)  |
| Entity Recognizer Small   | `entity_recognizer_sm`  | 2.5.0 |   `no` |          | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_sm_no_2.5.0_2.4_1588794567766.zip)  |
| Entity Recognizer Medium  | `entity_recognizer_md`  | 2.5.0 |   `no` |          | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_no_2.5.0_2.4_1588794357614.zip)  |
| Entity Recognizer Large   | `entity_recognizer_lg`  | 2.5.0 |   `no` |          | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_no_2.5.0_2.4_1588793261642.zip)  |  

### Polish - Pipelines

| Pipeline                 | Name                   | Build  | lang | Description | Offline   |
|:-------------------------|:-----------------------|:-------|:-------|:----------|:----------|
| Explain Document Small    | `explain_document_sm`  | 2.5.0 |   `pl` |           | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_sm_pl_2.5.0_2.4_1588531081173.zip)  |
| Explain Document Medium   | `explain_document_md`  | 2.5.0 |   `pl` |           | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_pl_2.5.0_2.4_1588530841737.zip)  |
| Explain Document Large    | `explain_document_lg`  | 2.5.0 |   `pl` |           | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_pl_2.5.0_2.4_1588529695577.zip)  |
| Entity Recognizer Small   | `entity_recognizer_sm`  | 2.5.0 |   `pl` |          | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_sm_pl_2.5.0_2.4_1588532616080.zip)  |
| Entity Recognizer Medium  | `entity_recognizer_md`  | 2.5.0 |   `pl` |          | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_pl_2.5.0_2.4_1588532376753.zip)  |
| Entity Recognizer Large   | `entity_recognizer_lg`  | 2.5.0 |   `pl` |          | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_pl_2.5.0_2.4_1588531171903.zip)  |  

### Portuguese - Pipelines

| Pipeline                 | Name                   | Build  | lang | Description | Offline   |
|:-------------------------|:-----------------------|:-------|:-------|:----------|:----------|
| Explain Document Small    | `explain_document_sm`  | 2.5.0 |   `pt` |           | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_sm_pt_2.5.0_2.4_1588501423743.zip)  |
| Explain Document Medium   | `explain_document_md`  | 2.5.0 |   `pt` |           | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_pt_2.5.0_2.4_1588501189804.zip)  |
| Explain Document Large    | `explain_document_lg`  | 2.5.0 |   `pt` |           | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_pt_2.5.0_2.4_1588500056427.zip)  |
| Entity Recognizer Small   | `entity_recognizer_sm`  | 2.5.0 |   `pt` |          | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_sm_pt_2.5.0_2.4_1588502815900.zip)  |
| Entity Recognizer Medium  | `entity_recognizer_md`  | 2.5.0 |   `pt` |          | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_pt_2.5.0_2.4_1588502606198.zip)  |
| Entity Recognizer Large   | `entity_recognizer_lg`  | 2.5.0 |   `pt` |          | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_pt_2.5.0_2.4_1588501526324.zip)  |  

### Russian - Pipelines

| Pipeline                 | Name                   | Build  | lang | Description | Offline   |
|:-------------------------|:-----------------------|:-------|:-------|:----------|:----------|
| Explain Document Small    | `explain_document_sm`  | 2.4.4 |   `ru` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_sm_ru_2.4.4_2.4_1584017142719.zip)  |
| Explain Document Medium   | `explain_document_md`  | 2.4.4 |   `ru` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_ru_2.4.4_2.4_1584016917220.zip)  |
| Explain Document Large    | `explain_document_lg`  | 2.4.4 |   `ru` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_ru_2.4.4_2.4_1584015824836.zip)  |
| Entity Recognizer Small   | `entity_recognizer_sm`  | 2.4.4 |   `ru` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_sm_ru_2.4.4_2.4_1584018543619.zip)  |
| Entity Recognizer Medium  | `entity_recognizer_md`  | 2.4.4 |   `ru` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_ru_2.4.4_2.4_1584018332357.zip)  |
| Entity Recognizer Large   | `entity_recognizer_lg`  | 2.4.4 |   `ru` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_ru_2.4.4_2.4_1584017227871.zip)  |  

### Spanish - Pipelines

| Pipeline                 | Name                   | Build  | lang | Description | Offline   |
|:-------------------------|:-----------------------|:-------|:-------|:----------|:----------|
| Explain Document Small    | `explain_document_sm`  | 2.4.0 |   `es` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_sm_es_2.4.0_2.4_1581977077084.zip)  |
| Explain Document Medium   | `explain_document_md`  | 2.4.0 |   `es` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_md_es_2.4.0_2.4_1581976836224.zip)  |
| Explain Document Large    | `explain_document_lg`  | 2.4.0 |   `es` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_lg_es_2.4.0_2.4_1581975536033.zip)  |
| Entity Recognizer Small   | `entity_recognizer_sm`  | 2.4.0 |   `es` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_sm_es_2.4.0_2.4_1581978479912.zip)  |
| Entity Recognizer Medium  | `entity_recognizer_md`  | 2.4.0 |   `es` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_md_es_2.4.0_2.4_1581978260094.zip)  |
| Entity Recognizer Large   | `entity_recognizer_lg`  | 2.4.0 |   `es` |             | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/entity_recognizer_lg_es_2.4.0_2.4_1581977172660.zip)  |

# Pretrained Models

## Public Models

If you wish to use a pre-trained model for a specific annotator in your pipeline, you need to use the annotator which is mentioned under `Model` following with `pretrained(name, lang)` function.

Example to load a pretraiand BERT model or NER model:

```python
bert = BertEmbeddings.pretrained(name='bert_base_cased', lang='en')

ner_onto = NerDLModel.pretrained(name='ner_dl_bert', lang='en')
```

**NOTE:** `build` means the model can be downloaded or loaded for that specific version or above. For instance, `2.4.0` can be used in all the releases after `2.4.x` but not before.

Pretrained models are great to creatae custom pipeline when the pretrained pipelines don't offer a feature or you need more flexibility:

```python

document = DocumentAssembler()\
    .setInputCol("description")\
    .setOutputCol("document")

use = UniversalSentenceEncoder.pretrained(name="tfhub_use", lang="en")\
 .setInputCols(["document"])\
 .setOutputCol("sentence_embeddings")

# the classes/labels/categories are in category column
sentimentdl = ClassifierDLModel.pretrained(name="sentimentdl_use_imdb", lang="en")\
  .setInputCols(["sentence_embeddings"])\
  .setOutputCol("sentiment")

pipeline = Pipeline(
    stages = [
        document,
        use,
        sentimentdl
    ])

```

### Dutch - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `nl`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_nl_2.5.0_2.4_1588532720582.zip) |
| PerceptronModel (POS UD)     | `pos_ud_alpino`       | 2.5.0 |   `nl`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_alpino_nl_2.5.0_2.4_1588545949009.zip) |
| NerDLModel (glove_100d)  | `wikiner_6B_100`       | 2.5.0 |   `nl`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_100_nl_2.5.0_2.4_1588546201140.zip) |
| NerDLModel (glove_6B_300)  | `wikiner_6B_300`     | 2.5.0 |   `nl`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_300_nl_2.5.0_2.4_1588546201483.zip) |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` | 2.5.0 |   `nl`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_nl_2.5.0_2.4_1588546201484.zip) |

### English - Models

| Model                                    | Name                      | Build            | Lang | Offline
|:-----------------------------------------|:--------------------------|:-----------------|:------------|:------|
| LemmatizerModel (Lemmatizer)             | `lemma_antbnc`            | 2.0.2 |      `en`         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_antbnc_en_2.0.2_2.4_1556480454569.zip) |
| PerceptronModel (POS)                    | `pos_anc`                 | 2.0.2 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_anc_en_2.0.2_2.4_1556659930154.zip) |
| PerceptronModel (POS UD)                    | `pos_ud_ewt`           | 2.2.2 |       `en`       | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_ewt_en_2.2.2_2.4_1570464827452.zip) |
| NerCrfModel (NER with GloVe)             | `ner_crf`                 | 2.4.0 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_crf_en_2.4.0_2.4_1580237286004.zip) |
| NerDLModel (NER with GloVe)              | `ner_dl`                  | 2.4.3 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_en_2.4.3_2.4_1584624950746.zip) |
| NerDLModel (NER with BERT)              | `ner_dl_bert`              | 2.4.3 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_bert_en_2.4.3_2.4_1584624951079.zip) |
| NerDLModel (OntoNotes with GloVe 100d)   | `onto_100`                | 2.4.0 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_100_en_2.4.0_2.4_1579729071672.zip) |
| NerDLModel (OntoNotes with GloVe 300d)   | `onto_300`                | 2.4.0 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/onto_300_en_2.4.0_2.4_1579729071854.zip) |
| DeepSentenceDetector                     | `ner_dl_sentence`         | 2.4.0 |      `en`         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_sentence_en_2.4.0_2.4_1580252313303.zip)|
| SymmetricDeleteModel (Spell Checker)     | `spellcheck_sd`           | 2.0.2 |      `en`         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/spellcheck_sd_en_2.0.2_2.4_1556604489934.zip)|
| NorvigSweetingModel (Spell Checker)      | `spellcheck_norvig`       | 2.0.2 |      `en`      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/spellcheck_norvig_en_2.0.2_2.4_1556605026653.zip)|
| ViveknSentimentModel (Sentiment)         | `sentiment_vivekn`        | 2.0.2 |      `en`      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentiment_vivekn_en_2.0.2_2.4_1556663184035.zip)|
| DependencyParser (Dependency)            | `dependency_conllu`       | 2.0.8 |      `en`      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_conllu_en_2.0.8_2.4_1561435004077.zip)|
| TypedDependencyParser (Dependency)       | `dependency_typed_conllu` | 2.0.8 |      `en`      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_typed_conllu_en_2.0.8_2.4_1561473259215.zip) |

#### Embeddings

| Model    | Name                      | Build            | Lang | Offline
|:--------------|:--------------------------|:-----------------|:------------|:------|
| WordEmbeddings (GloVe)            | `glove_100d`              | 2.4.0 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/glove_100d_en_2.4.0_2.4_1579690104032.zip) |
| BertEmbeddings                    | `bert_base_uncased`       | 2.4.0 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_base_uncased_en_2.4.0_2.4_1580579889322.zip) |
| BertEmbeddings                    | `bert_base_cased`         | 2.4.0 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_base_cased_en_2.4.0_2.4_1580579557778.zip) |
| BertEmbeddings                    | `bert_large_uncased`      | 2.4.0 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_large_uncased_en_2.4.0_2.4_1580581306683.zip) |
| BertEmbeddings                    | `bert_large_cased`        | 2.4.0 |      `en`         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_large_cased_en_2.4.0_2.4_1580580251298.zip) |
| ElmoEmbeddings                    | `elmo`                    | 2.4.0 |      `en`         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/elmo_en_2.4.0_2.4_1580488815299.zip)
| UniversalSentenceEncoder  (USE)   | `tfhub_use`              | 2.4.0 |       `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/tfhub_use_en_2.4.0_2.4_1587136330099.zip)
| UniversalSentenceEncoder  (USE)   | `tfhub_use_lg`           | 2.4.0 |       `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/tfhub_use_lg_en_2.4.0_2.4_1587136993894.zip)
| AlbertEmbeddings                  | `albert_base_uncased`    | 2.5.0 |      `en`         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/albert_base_uncased_en_2.5.0_2.4_1588073363475.zip)
| AlbertEmbeddings                  | `albert_large_uncased`    | 2.5.0 |      `en`         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/albert_large_uncased_en_2.5.0_2.4_1588073397355.zip)
| AlbertEmbeddings                  | `albert_xlarge_uncased`    | 2.5.0 |      `en`         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/albert_xlarge_uncased_en_2.5.0_2.4_1588073443653.zip)
| AlbertEmbeddings                  | `albert_xxlarge_uncased`    | 2.5.0 |      `en`         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/albert_xxlarge_uncased_en_2.5.0_2.4_1588073588232.zip)
| XlnetEmbeddings                  | `xlnet_base_cased`    | 2.5.0 |      `en`         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/xlnet_base_cased_en_2.5.0_2.4_1588074114942.zip)
| XlnetEmbeddings                  | `xlnet_large_cased`    | 2.5.0 |      `en`         | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/xlnet_large_cased_en_2.5.0_2.4_1588074397954.zip)

#### Classification

| Model    | Name                      | Build            | Lang | Offline
|:--------------|:--------------------------|:-----------------|:------------|:------|
| ClassifierDL (with tfhub_use)          | `classifierdl_use_trec6`        | 2.5.0 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/classifierdl_use_trec6_en_2.5.0_2.4_1588492648979.zip) |
| ClassifierDL (with tfhub_use)          | `classifierdl_use_trec50`       | 2.5.0 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/classifierdl_use_trec50_en_2.5.0_2.4_1588493558481.zip) |
| SentimentDL (with tfhub_use)           | `sentimentdl_use_imdb`          | 2.5.0 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentimentdl_use_imdb_en_2.5.0_2.4_1588679956272.zip) |
| SentimentDL (with tfhub_use)           | `sentimentdl_use_twitter`       | 2.5.0 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentimentdl_use_twitter_en_2.5.0_2.4_1589108892106.zip) |
| SentimentDL (with glove_100d)          | `sentimentdl_glove_imdb`         | 2.5.0 |      `en`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentimentdl_glove_imdb_en_2.5.0_2.4_1588682682507.zip) |

### French - Models

| Model                        | Name               | Build | Lang |  Offline|
|:-----------------------------|:-------------------|:------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            |   2.0.2    |   `fr`     | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_fr_2.0.2_2.4_1556531462843.zip)|
| PerceptronModel (POS UD)     | `pos_ud_gsd`       |   2.0.2    |    `fr`   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_gsd_fr_2.0.2_2.4_1556531457346.zip)|
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` |   2.0.2    |    `fr`   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_fr_2.4.0_2.4_1579699913554.zip)|

| Feature   | Description                                                                                                                                                                                            |    |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---|
| **Lemma** | Trained by **Lemmatizer** annotator on **lemmatization-lists** by `Michal Měchura`                                                                                                                     |    |
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/fr_gsd/index.html)                                                             |    |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |    |

### German - Models

| Model                        | Name               | Build            | Lang | Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.0.8 |       `de`      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_de_2.0.8_2.4_1561248996126.zip)|
| PerceptronModel (POS UD)     | `pos_ud_hdt`       | 2.0.8 |       `de`      | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_hdt_de_2.0.8_2.4_1561232528570.zip)|
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` | 2.4.0 |       `de`        | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_de_2.4.0_2.4_1579699913555.zip)|

| Feature   | Description                                                                                                                                                                                            |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lemma** | Trained by **Lemmatizer** annotator on **lemmatization-lists** by `Michal Měchura`                                                                                                                     |
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/de_hdt/index.html)                                                             |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |

### Italian - Models

| Model                         | Name               | Build            | Lang  | Offline|
|:------------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer)  | `lemma_dxc`        | 2.0.2 |    `it`   |  [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_dxc_it_2.0.2_2.4_1556531469058.zip)        |
| ViveknSentimentAnalysis (Sentiment) | `sentiment_dxc`    | 2.0.2 |    `it`   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentiment_dxc_it_2.0.2_2.4_1556531477694.zip)    |
| PerceptronModel (POS UD)      | `pos_ud_isdt`      | 2.0.8 |    `it`   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_isdt_it_2.0.8_2.4_1560168427464.zip)      |
| NerDLModel (glove_840B_300)   | `wikiner_840B_300` | 2.4.0 |   `it`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_it_2.4.0_2.4_1579699913554.zip) |

| Feature   | Description                                                                                                                                                                                            |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lemma** | Trained by **Lemmatizer** annotator on **DXC Technology** dataset                                                                                                                                      |
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/it_isdt/index.html)                                                            |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |

### Norwegian - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `nb`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_nb_2.5.0_2.4_1588693886432.zip) |
| PerceptronModel (POS UD)     | `pos_ud_nynorsk`       | 2.5.0 |   `nn`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_nynorsk_nn_2.5.0_2.4_1588693690964.zip) |
| PerceptronModel (POS UD)     | `pos_ud_bokmaal`       | 2.5.0 |   `nb`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_bokmaal_nb_2.5.0_2.4_1588693881973.zip) |
| NerDLModel (glove_100d)  | `norne_6B_100`       | 2.5.0 |   `no`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/norne_6B_100_no_2.5.0_2.4_1588781289907.zip) |
| NerDLModel (glove_6B_300)  | `norne_6B_300`     | 2.5.0 |   `no`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/norne_6B_300_no_2.5.0_2.4_1588781290264.zip) |
| NerDLModel (glove_840B_300)  | `norne_840B_300` | 2.5.0 |   `no`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/norne_840B_300_no_2.5.0_2.4_1588781290267.zip) |

### Polish - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `pl`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_pl_2.5.0_2.4_1588518491035.zip) |
| PerceptronModel (POS UD)     | `pos_ud_lfg`       | 2.5.0 |   `pl`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_lfg_pl_2.5.0_2.4_1588518541171.zip) |
| NerDLModel (glove_100d)  | `wikiner_6B_100`       | 2.5.0 |   `pl`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_100_pl_2.5.0_2.4_1588519719293.zip) |
| NerDLModel (glove_6B_300)  | `wikiner_6B_300`     | 2.5.0 |   `pl`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_300_pl_2.5.0_2.4_1588519719571.zip) |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` | 2.5.0 |   `pl`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_pl_2.5.0_2.4_1588519719572.zip) |

### Portuguese - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `pt`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_pt_2.5.0_2.4_1588499301752.zip) |
| PerceptronModel (POS UD)     | `pos_ud_bosque`       | 2.5.0 |   `pt`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_bosque_pt_2.5.0_2.4_1588499443093.zip) |
| NerDLModel (glove_100d)  | `wikiner_6B_100`       | 2.5.0 |   `pt`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_100_pt_2.5.0_2.4_1588495233192.zip) |
| NerDLModel (glove_6B_300)  | `wikiner_6B_300`     | 2.5.0 |   `pt`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_300_pt_2.5.0_2.4_1588495233641.zip) |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` | 2.5.0 |   `pt`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_pt_2.5.0_2.4_1588495233642.zip) |

### Russian - Models

| Model                        | Name               | Build            | Lang  | Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.4.4 |    `ru`   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_ru_2.4.4_2.4_1584013425855.zip) |
| PerceptronModel (POS UD)     | `pos_ud_gsd`       | 2.4.4 |    `ru`   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_gsd_ru_2.4.4_2.4_1584013495069.zip) |
| NerDLModel (glove_100d)  | `wikiner_6B_100` | 2.4.4 |    `ru`   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_100_ru_2.4.4_2.4_1584014001452.zip) |
| NerDLModel (glove_6B_300)  | `wikiner_6B_300` | 2.4.4 |  `ru`     | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_300_ru_2.4.4_2.4_1584014001694.zip) |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` | 2.4.4 |   `ru`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_ru_2.4.4_2.4_1584014001695.zip) |

| Feature   | Description                                                                                                                                                                                            |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lemma** | Trained by **Lemmatizer** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/ru_gsd/index.html)|
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/ru_gsd/index.html)                                                             |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |

### Spanish - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.4.0 |    `es`   |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_es_2.4.0_2.4_1581890818386.zip) |
| PerceptronModel (POS UD)     | `pos_ud_gsd`       | 2.4.0 |   `es`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_gsd_es_2.4.0_2.4_1581891015986.zip) |
| NerDLModel (glove_100d)  | `wikiner_6B_100` | 2.4.0 |    `es`   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_100_es_2.4.0_2.4_1581971941700.zip) |
| NerDLModel (glove_6B_300)  | `wikiner_6B_300` | 2.4.0 |  `es`     | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_6B_300_es_2.4.0_2.4_1581971942090.zip) |
| NerDLModel (glove_840B_300)  | `wikiner_840B_300` | 2.4.0 |   `es`    | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/wikiner_840B_300_es_2.4.0_2.4_1581971942091.zip;) |

| Feature   | Description                                                                                                                                                                                            |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lemma** | Trained by **Lemmatizer** annotator on **lemmatization-lists** by `Michal Měchura`                                                                                                                     |
| **POS**   | Trained by **PerceptronApproach** annotator on the [Universal Dependencies](https://universaldependencies.org/treebanks/es_gsd/index.html)                                                             |
| **NER**   | Trained by **NerDLApproach** annotator with **Char CNNs - BiLSTM - CRF** and **GloVe Embeddings** on the **WikiNER** corpus and supports the identification of `PER`, `LOC`, `ORG` and `MISC` entities |

### Bulgarian - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `bg`   |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_bg_2.5.0_2.4_1588666297763.zip) |
| PerceptronModel (POS UD)     | `pos_ud_btb`       | 2.5.0 |   `bg`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_btb_bg_2.5.0_2.4_1588621401140.zip) |

### Czech - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `cs`   |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_cs_2.5.0_2.4_1588666300042.zip) |
| PerceptronModel (POS UD)     | `pos_ud_pdt`       | 2.5.0 |   `cs`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_pdt_cs_2.5.0_2.4_1588622155494.zip) |

### Greek - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `el`   |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_el_2.5.0_2.4_1588686951720.zip) |
| PerceptronModel (POS UD)     | `pos_ud_gdt`       | 2.5.0 |   `el`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_gdt_el_2.5.0_2.4_1588686949851.zip) |

### Finnish - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `fi`   |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_fi_2.5.0_2.4_1588671290521.zip) |
| PerceptronModel (POS UD)     | `pos_ud_tdt`       | 2.5.0 |   `fi`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_tdt_fi_2.5.0_2.4_1588622348985.zip) |

### Hungarian - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `hu`   |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_hu_2.5.0_2.4_1588671968880.zip) |
| PerceptronModel (POS UD)     | `pos_ud_szeged`       | 2.5.0 |   `hu`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_szeged_hu_2.5.0_2.4_1588671966774.zip) |

### Romanian - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `ro`   |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_ro_2.5.0_2.4_1588666512149.zip) |
| PerceptronModel (POS UD)     | `pos_ud_rrt`       | 2.5.0 |   `ro`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_rrt_ro_2.5.0_2.4_1588622539956.zip) |

### Slovak - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `sk`   |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_sk_2.5.0_2.4_1588666524270.zip) |
| PerceptronModel (POS UD)     | `pos_ud_snk`       | 2.5.0 |   `sk`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_snk_sk_2.5.0_2.4_1588622627281.zip) |

### Swedish - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `sv`   |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_sv_2.5.0_2.4_1588666548498.zip) |
| PerceptronModel (POS UD)     | `pos_ud_tal`       | 2.5.0 |   `sv`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_tal_sv_2.5.0_2.4_1588622711284.zip) |

### Turkish - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `tr`   |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_tr_2.5.0_2.4_1587479962436.zip) |
| PerceptronModel (POS UD)     | `pos_ud_imst`       | 2.5.0 |   `tr`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_imst_tr_2.5.0_2.4_1587480006078.zip) |

### Ukrainian - Models

| Model                        | Name               | Build            | Lang |  Offline|
|:-----------------------------|:-------------------|:-----------------|:------|:------------|
| LemmatizerModel (Lemmatizer) | `lemma`            | 2.5.0 |   `uk`   |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_uk_2.5.0_2.4_1588671294202.zip) |
| PerceptronModel (POS UD)     | `pos_ud_iu`       | 2.5.0 |   `uk`    |[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_iu_uk_2.5.0_2.4_1588668890963.zip) |

### Multi-language

| Model                        | Name               | Build            | Lang | Offline |
|:-----------------------------|:-------------------|:-----------------|:------|:------|
| WordEmbeddings (GloVe)       | `glove_840B_300`   | 2.4.0 |  `xx`   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/glove_840B_300_xx_2.4.0_2.4_1579698926752.zip)   |
| WordEmbeddings (GloVe)       | `glove_6B_300`     | 2.4.0 |   `xx`   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/glove_6B_300_xx_2.4.0_2.4_1579698630432.zip)     |
| BertEmbeddings (multi_cased) | `bert_multi_cased` | 2.4.0 |   `xx`   | [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_multi_cased_xx_2.4.0_2.4_1580582335793.zip) |

# Licensed Enterprise

It is required to specify 3rd argument to `pretrained(name, lang, location)` function to add the location of these

## Pretrained Models - Spark NLP For Healthcare

### English Language, Clinical/Models Location

`{Model}.pretrained({Name}, 'en', 'clinical/models')`

| Model                         | Name                                            | Build   |                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                            |                                                                                                                                                                                               |
|-------------------------------|-------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AssertionDLModel`            | `assertion_dl_large`                            | `2.4.2` | [:mag:](# 'Extracts: hypothetical, present, absent, possible, conditional, associated_with_someone_else')                                                                                                                                                            | [:clipboard:](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/ 'Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_clinical`')               | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/assertion_dl_large_en_2.4.2_2.4_1588811895962.zip 'Download')                            |
| `AssertionDLModel`            | `assertion_dl`                                  | `2.4.0` | [:mag:](# 'Extracts: hypothetical, present, absent, possible, conditional, associated_with_someone_else')                                                                                                                                                            | [:clipboard:](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/ 'Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_clinical`')               | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/assertion_dl_en_2.4.0_2.4_1580237286004.zip 'Download')                                  |
| `AssertionLogRegModel`        | `assertion_ml`                                  | `2.4.0` | [:mag:](# 'Extracts: hypothetical, present, absent, possible, conditional, associated_with_someone_else')                                                                                                                                                            | [:clipboard:](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/ 'Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_clinical`')               | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/assertion_ml_en_2.4.0_2.4_1580237286004.zip 'Download')                                  |
| `BertEmbeddings`              | `biobert_clinical_cased`                        | `2.3.1` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Pretrained from TFHub')                                                                                                                                                                   | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/biobert_clinical_cased_en_2.3.1_2.4_1574522054965.zip 'Download')                        |
| `BertEmbeddings`              | `biobert_discharge_cased`                       | `2.3.1` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Pretrained from TFHub')                                                                                                                                                                   | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/biobert_discharge_cased_en_2.3.1_2.4_1574522388638.zip 'Download')                       |
| `BertEmbeddings`              | `biobert_pmc_cased`                             | `2.3.1` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Pretrained from TFHub')                                                                                                                                                                   | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/biobert_pmc_cased_en_2.3.1_2.4_1574521384805.zip 'Download')                             |
| `BertEmbeddings`              | `biobert_pubmed_cased`                          | `2.3.1` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Pretrained from TFHub')                                                                                                                                                                   | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/biobert_pubmed_cased_en_2.3.1_2.4_1574521132506.zip 'Download')                          |
| `BertEmbeddings`              | `biobert_pubmed_pmc_cased`                      | `2.3.1` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Pretrained from TFHub')                                                                                                                                                                   | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/biobert_pubmed_pmc_cased_en_2.3.1_2.4_1574521728558.zip 'Download')                      |
| `ChunkEntityResolverModel`    | `chunkresolve_cpt_clinical`                     | `2.4.5` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Trained on Current Procedural Terminology dataset')                                                                                                                                       | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_cpt_clinical_en_2.4.5_2.4_1587491373378.zip 'Download')                     |
| `ChunkEntityResolverModel`    | `chunkresolve_icd10cm_clinical`                 | `2.4.5` | [:mag:](# 'Extracts: ICD10-CM Codes and their normalized definition')                                                                                                                                                                                                | [:clipboard:](https://www.icd10data.com/ICD10CM/Codes/ 'Trained on ICD10 Clinical Modification datasetwith tenths of variations per code')                                                                 | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10cm_clinical_en_2.4.5_2.4_1587491222166.zip 'Download')                 |
| `ChunkEntityResolverModel`    | `chunkresolve_icd10cm_diseases_clinical`        | `2.4.5` | [:mag:](# 'Extracts: ICD10-CM Codes and their normalized definition')                                                                                                                                                                                                | [:clipboard:](https://www.icd10data.com/ICD10CM/Codes/ 'Trained on ICD10CM Dataset Range: A000-N989 Except Neoplasms and Musculoskeletal')                                                                 | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10cm_diseases_clinical_en_2.4.5_2.4_1588105984876.zip 'Download')        |
| `ChunkEntityResolverModel`    | `chunkresolve_icd10cm_injuries_clinical`        | `2.4.5` | [:mag:](# 'Extracts: ICD10-CM Codes and their normalized definition')                                                                                                                                                                                                | [:clipboard:](https://www.icd10data.com/ICD10CM/Codes/S00-T88 'Trained on ICD10CM Dataset Range: S0000XA-S98929S ')                                                                                        | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10cm_injuries_clinical_en_2.4.5_2.4_1588103825347.zip 'Download')        |
| `ChunkEntityResolverModel`    | `chunkresolve_icd10cm_musculoskeletal_clinical` | `2.4.5` | [:mag:](# 'Extracts: ICD10-CM Codes and their normalized definition')                                                                                                                                                                                                | [:clipboard:](https://www.icd10data.com/ICD10CM/Codes/M00-M99 'Trained on ICD10CM Dataset Range: M0000-M9979XXS')                                                                                          | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10cm_musculoskeletal_clinical_en_2.4.5_2.4_1588103998999.zip 'Download') |
| `ChunkEntityResolverModel`    | `chunkresolve_icd10cm_neoplasms_clinical`       | `2.4.5` | [:mag:](# 'Extracts: ICD10-CM Codes and their normalized definition')                                                                                                                                                                                                | [:clipboard:](https://www.icd10data.com/ICD10CM/Codes/C00-D49 'Trained on ICD10CM Dataset Ranges: C000-D489, R590-R599')                                                                                   | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10cm_neoplasms_clinical_en_2.4.5_2.4_1588108205630.zip 'Download')       |
| `ChunkEntityResolverModel`    | `chunkresolve_icd10cm_puerile_clinical`         | `2.4.5` | [:mag:](# 'Extracts: ICD10-CM Codes and their normalized definition')                                                                                                                                                                                                | [:clipboard:](https://www.icd10data.com/ICD10CM/Codes/O00-O9A 'Trained on ICD10CM Dataset Range: O0000-O9989')                                                                                             | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10cm_puerile_clinical_en_2.4.5_2.4_1588103916781.zip 'Download')         |
| `ChunkEntityResolverModel`    | `chunkresolve_icd10pcs_clinical`                | `2.4.5` | [:mag:](# 'Extracts: ICD10-PCS Codes and their normalized definition')                                                                                                                                                                                               | [:clipboard:](https://www.icd10data.com/ICD10PCS/Codes 'Trained on ICD10 Procedure Coding System dataset')                                                                                                 | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10pcs_clinical_en_2.4.5_2.4_1587491320087.zip 'Download')                |
| `ChunkEntityResolverModel`    | `chunkresolve_icdo_clinical`                    | `2.4.5` | [:mag:](# 'Extracts: ICD-O Codes and their normalized definition')                                                                                                                                                                                                   | [:clipboard:](https://apps.who.int/iris/bitstream/handle/10665/96612/9789241548496_eng.pdf 'Trained on ICD-O Histology Behaviour dataset')                                                                 | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icdo_clinical_en_2.4.5_2.4_1587491354644.zip 'Download')                    |
| `ContextSpellCheckerModel`    | `spellcheck_clinical`                           | `2.4.2` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Trained with PubMed and i2b2 datasets')                                                                                                                                                   | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/spellcheck_clinical_en_2.4.2_2.4_1587146727460.zip 'Download')                           |
| `DeIdentificationModel`       | `deidentify_rb_no_regex`                        | `2.4.5` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Rule based DeIdentifier based on `ner_deid`')                                                                                                                                             | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/deidentify_rb_no_regex_en_2.4.5_2.4_1587996657263.zip 'Download')                        |
| `DeIdentificationModel`       | `deidentify_rb`                                 | `2.0.2` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Rule based DeIdentifier based on `ner_deid`')                                                                                                                                             | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/deidentify_rb_en_2.0.2_2.4_1559672122511.zip 'Download')                                 |
| `EnsembleEntityResolverModel` | `ensembleresolve_icd10cm_clinical`              | `2.4.7` | [:mag:](# 'Extracts: ICD10-CM Codes and their normalized definition')                                                                                                                                                                                                | [:clipboard:](https://www.icd10data.com/ICD10CM/Codes/ 'Trained on ICD10 Clinical Modification dataset with hundreds of variations per code')                                                              | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ensembleresolve_icd10cm_clinical_en_2.4.7_2.4_1587845517639.zip 'Download')              |
| `EnsembleEntityResolverModel` | `ensembleresolve_rxnorm_clinical`               | `2.4.5` | [:mag:](# 'Extracts: RxNorm Codes and their normalized definition')                                                                                                                                                                                                  | [:clipboard:](https://www.nlm.nih.gov/pubs/techbull/nd19/brief/nd19_rxnorm_december_2019_release.html 'Trained on December 2019 RxNorm ontology graph with `embeddings_clinical`')                         | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ensembleresolve_rxnorm_clinical_en_2.4.5_2.4_1587300549721.zip 'Download')               |
| `EnsembleEntityResolverModel` | `ensembleresolve_rxnorm_healthcare`             | `2.4.5` | [:mag:](# 'Extracts: RxNorm Codes and their normalized definition')                                                                                                                                                                                                  | [:clipboard:](https://www.nlm.nih.gov/pubs/techbull/nd19/brief/nd19_rxnorm_december_2019_release.html 'Trained on December 2019 RxNorm ontology graph with `embeddings_healthcare`')                       | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ensembleresolve_rxnorm_healthcare_en_2.4.5_2.4_1587302681254.zip 'Download')             |
| `EnsembleEntityResolverModel` | `ensembleresolve_snomed_clinical`               | `2.4.5` | [:mag:](# 'Extracts: SNOMED Codes and their normalized definition')                                                                                                                                                                                                  | [:clipboard:](https://www.nlm.nih.gov/pubs/techbull/so19/brief/so19_snomed_release.html 'Trained on September 2019 SNOMED CT ontology graph with `embeddings_clinical`')                                   | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ensembleresolve_snomed_clinical_en_2.4.5_2.4_1587296548545.zip 'Download')               |
| `EnsembleEntityResolverModel` | `ensembleresolve_snomed_healthcare`             | `2.4.5` | [:mag:](# 'Extracts: SNOMED Codes and their normalized definition')                                                                                                                                                                                                  | [:clipboard:](https://www.nlm.nih.gov/pubs/techbull/so19/brief/so19_snomed_release.html 'Trained on September 2019 SNOMED CT ontology graph with `embeddings_healthcare`')                                 | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ensembleresolve_snomed_healthcare_en_2.4.5_2.4_1587298549235.zip 'Download')             |
| `NerDLModel`                  | `ner_anatomy`                                   | `2.4.2` | [:mag:](# 'Extracts: Anatomical_system, Cell, Cellular_component, Developing_anatomical_structure, Immaterial_anatomical_entity, Multi-tissue_structure, Organ, Organism_subdivision, Organism_substance, Pathological_formation, Tissue.')                          | [:clipboard:](http://www.nactem.ac.uk/anatomy/ 'Trained on the Anatomical Entity Mention (AnEM) corpus with `embeddings_clinical`')                                                                        | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_anatomy_en_2.4.2_2.4_1587513307751.zip 'Download')                                   |
| `NerDLModel`                  | `ner_bionlp`                                    | `2.4.0` | [:mag:](# 'Extracts: Amino_acid, Anatomical_system, Cancer, Cell, Cellular_component, Developing_anatomical_Structure, Gene_or_gene_product, Immaterial_anatomical_entity, Multi-tissue_structure, Organ, Organism, Organism_subdivision, Simple_chemical, Tissue.') | [:clipboard:](http://2013.bionlp-st.org/tasks/cancer-genetics 'Trained on Cancer Genetics (CG) task of the BioNLP Shared Task 2013 with `embeddings_clinical`')                                            | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_bionlp_en_2.4.0_2.4_1580237286004.zip 'Download')                                    |
| `NerDLModel`                  | `ner_cellular`                                  | `2.4.2` | [:mag:](# 'Extracts: DNA, Cell_type, Cell_line, RNA, Protein.')                                                                                                                                                                                                      | [:clipboard:](http://www.geniaproject.org/ 'Trained on the JNLPBA corpus containing more than 2.404 publication abstracts with `embeddings_clinical`')                                                     | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_cellular_en_2.4.2_2.4_1587513308751.zip 'Download')                                  |
| `NerDLModel`                  | `ner_clinical`                                  | `2.4.0` | [:mag:](# 'Extracts: Problem, Test, Treatment.')                                                                                                                                                                                                                     | [:clipboard:](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp 'Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_clinical`.')               | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_en_2.4.0_2.4_1580237286004.zip 'Download')                                  |
| `NerDLModel`                  | `ner_deid_enriched`                             | `2.4.2` | [:mag:](# 'Extracts: Age, City, Country, Date, Doctor, Hospital, Idnum, Medicalrecord, Organization, Patient, Phone, Profession, State, Street, Username, Zip.')                                                                                                     | [:clipboard:](https://portal.dbmi.hms.harvard.edu/projects/n2c2-2014/ 'Trained on JSL enriched n2c2 2014: De-identification and Heart Disease Risk Factors Challenge datasets with `embeddings_clinical`') | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_deid_enriched_en_2.4.2_2.4_1587513306751.zip 'Download')                             |
| `NerDLModel`                  | `ner_deid_large`                                | `2.4.2` | [:mag:](# 'Extracts: Age, Contact, Date, Id, Location, Name, Profession.')                                                                                                                                                                                           | [:clipboard:](https://portal.dbmi.hms.harvard.edu/projects/n2c2-2014/ 'Trained on plain n2c2 2014: De-identification and Heart Disease Risk Factors Challenge datasets with `embeddings_clinical`')        | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_deid_large_en_2.4.2_2.4_1587513305751.zip 'Download')                                |
| `NerDLModel`                  | `ner_diseases`                                  | `2.4.4` | [:mag:](# 'Extracts: Disease')                                                                                                                                                                                                                                       | [:clipboard:](# 'Trained on i2b2 with `embeddings_clinical.')                                                                                                                                              | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_diseases_en_2.4.4_2.4_1584452534235.zip 'Download')                                  |
| `NerDLModel`                  | `ner_drugs`                                     | `2.4.4` | [:mag:](# 'Extracts: DrugChem (Drug and Chemicals)')                                                                                                                                                                                                                 | [:clipboard:](https://www.i2b2.org/NLP/Medication 'Trained on i2b2_med7 + FDA with `embeddings_clinical`.')                                                                                                | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_drugs_en_2.4.4_2.4_1584452534235.zip 'Download')                                     |
| `NerDLModel`                  | `ner_healthcare`                                | `2.4.4` | [:mag:](# 'Extracts: Problem, Test, Treatment.')                                                                                                                                                                                                                     | [:clipboard:](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/ 'Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_healthcare`.')            | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_healthcare_en_2.4.4_2.4_1585188313964.zip 'Download')                                |
| `NerDLModel`                  | `ner_jsl_enriched`                              | `2.4.2` | [:mag:](# 'Extracts: Age, Diagnosis, Dosage, Drug_name, Frequency, Gender, Lab_name, Lab_result, Modifier, Name, Negation, Symptom_name')                                                                                                                            | [:clipboard:](https://www.johnsnowlabs.com/data/ 'Trained on data gathered and manually annotated by John Snow Labs')                                                                                      | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_jsl_enriched_en_2.4.2_2.4_1587513303751.zip 'Download')                              |
| `NerDLModel`                  | `ner_jsl`                                       | `2.4.2` | [:mag:](# 'Extracts: Age, Diagnosis, Dosage, Drug_name, Frequency, Gender, Lab_name, Lab_result, Modifier, Name, Negation, Symptom_name')                                                                                                                            | [:clipboard:](https://www.johnsnowlabs.com/data/ 'Trained on data gathered and manually annotated by John Snow Labs')                                                                                      | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_jsl_en_2.4.2_2.4_1587513304751.zip 'Download')                                       |
| `NerDLModel`                  | `ner_posology_large`                            | `2.4.2` | [:mag:](# 'Extracts: Dosage, Drug, Duration, Form,  Frequency, Route, Strength.')                                                                                                                                                                                    | [:clipboard:](https://open.fda.gov/ 'Trained on the 2018 i2b2 dataset and FDA Drug datasets with `embeddings_clinical`.')                                                                                  | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_posology_large_en_2.4.2_2.4_1587513302751.zip 'Download')                            |
| `NerDLModel`                  | `ner_posology_small`                            | `2.4.2` | [:mag:](# 'Extracts: Dosage, Drug, Duration, Form,  Frequency, Route, Strength.')                                                                                                                                                                                    | [:clipboard:](https://www.i2b2.org/NLP/Medication 'Trained on the 2018 i2b2 dataset (no FDA) with `embeddings_clinical`.')                                                                                 | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_posology_small_en_2.4.2_2.4_1587513301751.zip 'Download')                            |
| `NerDLModel`                  | `ner_posology`                                  | `2.4.4` | [:mag:](# 'Extracts: Dosage, Drug, Duration, Form,  Frequency, Route, Strength.')                                                                                                                                                                                    | [:clipboard:](https://open.fda.gov/ 'Trained on the 2018 i2b2 dataset and FDA Drug datasets with `embeddings_clinical`.')                                                                                  | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_posology_en_2.4.4_2.4_1584452534235.zip 'Download')                                  |
| `NerDLModel`                  | `ner_risk_factors`                              | `2.4.2` | [:mag:](# 'Extracts: Cad, Diabetes, Family_hist, Hyperlipidemia, Hypertension, Medication, Obese, Phi, Smoker.')                                                                                                                                                     | [:clipboard:](https://portal.dbmi.hms.harvard.edu/projects/n2c2-2014/ 'Trained on plain n2c2 2014: De-identification and Heart Disease Risk Factors Challenge datasets with `embeddings_clinical`')        | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/ner_risk_factors_en_2.4.2_2.4_1587513300751.zip 'Download')                              |
| `PerceptronModel`             | `pos_clinical`                                  | `2.0.2` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Trained with MedPost dataset')                                                                                                                                                            | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/pos_clinical_en_2.0.2_2.4_1556660550177.zip 'Download')                                  |
| `TextMatcherModel`            | `textmatch_cpt_token`                           | `2.4.5` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Trai,ned on NER Synonym Augmented Procedural Terminology bigram tokens combined up to a window of one')                                                                                   | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/textmatch_cpt_token_en_2.4.5_2.4_1587495106014.zip 'Download')                           |
| `TextMatcherModel`            | `textmatch_icdo_ner`                            | `2.4.5` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Trained on NER Synonym Augmented ICD Histology Behaviour bigram tokens up to a window of four')                                                                                           | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/textmatch_icdo_ner_en_2.4.5_2.4_1587495006987.zip 'Download')                            |
| `WordEmbeddingsModel`         | `embeddings_clinical`                           | `2.4.0` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Trained on PubMed corpora')                                                                                                                                                               | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/embeddings_clinical_en_2.4.0_2.4_1580237286004.zip 'Download')                           |
| `WordEmbeddingsModel`         | `embeddings_healthcare`                         | `2.4.4` |                                                                                                                                                                                                                                                                      | [:clipboard:](# 'Trained on PubMed + ICD10 + UMLS + MIMIC III corpora')                                                                                                                                    | [:floppy_disk:](https://s3.console.aws.amazon.com/s3/object/auxdata.johnsnowlabs.com/clinical/models/embeddings_healthcare_en_2.4.4_2.4_1585188313964.zip 'Download')                         |

## Contact

nlp@johnsnowlabs.com

## John Snow Labs

[https://johnsnowlabs.com](http://johnsnowlabs.com)
