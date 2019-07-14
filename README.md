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

### NerDLModel

#### French

Pre-trained `NerDLModel` was trained on `WikiNER` corpus. The evaluation is tag based and it was done over a random proportion of the `WikiNER` corpus.

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

## Contributing

We appreciate any sort of contributions:

* ideas
* feedback
* documentation
* bug reports
* nlp training and testing corpora
* development and testing

## Contact

nlp@johnsnowlabs.com

## John Snow Labs

[http://johnsnowlabs.com](http://johnsnowlabs.com)
