---
title: Universal Sentence Encoder Large
author: John Snow Labs
name: tfhub_use_lg
date: 2020-04-17
tags: [embeddings, en, use]
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description
The Universal Sentence Encoder encodes text into high-dimensional vectors that can be used for text classification, semantic similarity, clustering and other natural language tasks.

The model is trained and optimized for greater-than-word length text, such as sentences, phrases or short paragraphs. It is trained on a variety of data sources and a variety of tasks with the aim of dynamically accommodating a wide variety of natural language understanding tasks. The input is variable length English text and the output is a 512 dimensional vector. We apply this model to the STS benchmark for semantic similarity, and the results can be seen in the example notebook made available. The universal-sentence-encoder model is trained with a deep averaging network (DAN) encoder.

The details are described in the paper "[Universal Sentence Encoder](https://arxiv.org/abs/1803.11175)".

{:.btn-box}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/tfhub_use_lg_en_2.4.0_2.4_1587136993894.zip){:.button.button-orange.button-orange-trans.arr.button-icon}

## How to use

{% include programmingLanguageSelectScalaPython.html %}

```python

embeddings = UniversalSentenceEncoder.pretrained("tfhub_use_lg", "en") \
      .setInputCols("document") \
      .setOutputCol("sentence_embeddings")
```

```scala

val embeddings = UniversalSentenceEncoder.pretrained("tfhub_use_lg", "en")
      .setInputCols("document")
      .setOutputCol("sentence_embeddings")
```

{:.model-param}
## Model Parameters

{:.table-model}
|---|---|
|Model Name:|tfhub_use_lg|
|Type:|embeddings|
|Compatibility:|Spark NLP 2.4.0|
|Edition:|Official|
|Spark inputs:|[sentence, token]|
|Spark outputs:|[sentence_embeddings]|
|Language:|[en]|
|Dimension:|512|
|Case sensitive:|true|
|License:|Open Source|

{:.h2_title}
## Source
The model is imported from [https://tfhub.dev/google/universal-sentence-encoder-large/3](https://tfhub.dev/google/universal-sentence-encoder-large/3)
