<a href="https://johnsnowlabs.com"><img src="https://media.licdn.com/dms/image/C510BAQFT1HLZor5NGA/company-logo_400_400/0?e=1568246400&v=beta&t=zhiiJXBg8OqEUH1WhVK31UxJiN_O1g26G0DNjEcD0ZM" width="125" height="125" align="right" /></a>

# Spark NLP Models

[![Build Status](https://travis-ci.org/JohnSnowLabs/spark-nlp.svg?branch=master)](https://travis-ci.org/JohnSnowLabs/spark-nlp) [![Maven Central](https://maven-badges.herokuapp.com/maven-central/com.johnsnowlabs.nlp/spark-nlp_2.11/badge.svg)](https://search.maven.org/artifact/com.johnsnowlabs.nlp/spark-nlp_2.11) [![PyPI version](https://badge.fury.io/py/spark-nlp.svg)](https://badge.fury.io/py/spark-nlp) [![Anaconda-Cloud](https://anaconda.org/johnsnowlabs/spark-nlp/badges/version.svg)](https://anaconda.org/JohnSnowLabs/spark-nlp) [![License](https://img.shields.io/badge/License-Apache%202.0-brightgreen.svg)](https://github.com/JohnSnowLabs/spark-nlp/blob/master/LICENSE)

We use this repository to maintain our releases of pre-trained pipelines and models for the Spark NLP library. For more info please take a look at our [releases](https://github.com/JohnSnowLabs/spark-nlp-models/releases).

## Project's website

Take a look at our official Spark NLP page: [http://nlp.johnsnowlabs.com/](http://nlp.johnsnowlabs.com/) for user documentation and examples

## Slack community channel

[Join Slack](https://join.slack.com/t/spark-nlp/shared_invite/enQtNjA4MTE2MDI1MDkxLTM4ZDliMjU5OWZmMDE1ZGVkMjg0MWFjMjU3NjY4YThlMTJkNmNjNjM3NTMwYzlhMWY4MGMzODI2NDBkOWU4ZDE)

## Table of contents

* [Spark NLP Evaluation](#spark-nlp-evaluation)
  * [NerDLModel](#nerdlmodel)
    * [French](#french)
    * [German](#german)
    * [Italian](#italian)
* [Spark NLP Training](https://github.com/JohnSnowLabs/spark-nlp-models/tree/master/training)
  * [Lemmatizer Model](https://github.com/JohnSnowLabs/spark-nlp-models/tree/master/training/lemmatizer)
  * [POS Tagger Model](https://github.com/JohnSnowLabs/spark-nlp-models/tree/master/training/part_of_speech)

## Spark NLP Evaluation

How do we calcuate Precision, Recall, and F1-Score:

> **Precision** is "how useful the POS results are", and **Recall** is "how complete the results are". Precision can be seen as a measure of **exactness or quality**, whereas recall is a measure of **completeness or quantity**. [https://en.wikipedia.org/wiki/Precision_and_recall](https://en.wikipedia.org/wiki/Precision_and_recall)

> The **F1 score** is the harmonic average of the precision and recall, where an F1 score reaches its best value at 1 (perfect precision and recall) and worst at 0. [https://en.wikipedia.org/wiki/F1_score](https://en.wikipedia.org/wiki/F1_score)

![Precision](https://wikimedia.org/api/rest_v1/media/math/render/svg/26106935459abe7c266f7b1ebfa2a824b334c807)

![Recall](https://wikimedia.org/api/rest_v1/media/math/render/svg/4c233366865312bc99c832d1475e152c5074891b)

![F1 Score](https://wikimedia.org/api/rest_v1/media/math/render/svg/057ffc6b4fa80dc1c0e1f2f1f6b598c38cdd7c23)

### NerDLModel

The evaluation scores are tagged-based and it is done over a random proportion of `WikiNER` (for multi-lingual NerDLModel) or CoNLL 2003 `testa+testb` for English NerDLModel.

#### French

Pre-trained `NerDLModel` was trained on French `WikiNER` corpus and pre-trained WordEmbeddingd `glove_840B_300`.

#### French NER ACCURACY

|tag   |Precision|Recall|F1-Score|
|------|------|------|------|
|I-PER |0.969    |0.971 |0.97    |
|I-ORG |0.931    |0.926 |0.928   |
|I-LOC |0.919    |0.93  |0.924   |
|I-MISC|0.913    |0.919 |0.916   |
|B-MISC|0.909    |0.758 |0.827   |
|B-PER |0.904    |0.885 |0.894   |
|B-ORG |0.895    |0.944 |0.919   |
|B-LOC |0.793    |0.805 |0.799   |

|Precision         |Recall |F1-Score          |
|------------------|-------|------------------|
|0.90|0.89|0.90|

#### German

Pre-trained `NerDLModel` was trained on Dutch `WikiNER` corpus and pre-trained WordEmbeddingd `glove_840B_300`.

#### German NER ACCURACY

|tag   |Precision|Recall|F1-Score|
|------|------|------|------|
|I-PER |0.985    |0.984 |0.984   |
|I-LOC |0.951    |0.977 |0.964   |
|I-ORG |0.954    |0.934 |0.944   |
|I-MISC|0.949    |0.923 |0.936   |
|B-LOC |0.917    |0.906 |0.911   |
|B-ORG |0.93     |0.856 |0.891   |
|B-MISC|0.905    |0.788 |0.842   |
|B-PER |0.928    |0.72  |0.811   |

|Precision |Recall |F1-Score          |
|----------|-------|------------------|
|0.94|0.89|0.91|

#### Italian

Pre-trained `NerDLModel` was trained on Italian `WikiNER` corpus and pre-trained WordEmbeddingd `glove_840B_300`.

#### Italian NER ACCURACY

|tag   |Precision|Recall|F1-Score|
|------|------|------|------|
|I-PER |0.983    |0.987 |0.985   |
|I-ORG |0.966    |0.961 |0.963   |
|I-MISC|0.949    |0.948 |0.948   |
|B-PER |0.935    |0.896 |0.915   |
|I-LOC |0.933    |0.966 |0.949   |
|B-MISC|0.889    |0.865 |0.877   |
|B-LOC |0.864    |0.9   |0.882   |
|B-ORG |0.636    |0.933 |0.756   |

|Precision |Recall |F1-Score          |
|----------|-------|------------------|
|0.89|0.93|0.91|

## Contact

nlp@johnsnowlabs.com

## John Snow Labs

[http://johnsnowlabs.com](http://johnsnowlabs.com)
