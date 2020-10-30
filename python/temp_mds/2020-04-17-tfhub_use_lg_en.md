---
layout: model
title: Universal Sentence Encoder Large
author: John Snow Labs
name: tfhub_use_lg
class: 
language: en
repository: public/models
date: 17/04/2020
tags: []
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
The Universal Sentence Encoder encodes text into high,dimensional vectors that can be used for text classification, semantic similarity, clustering and other natural language tasks.,The model is trained and optimized for greater,than,word length text, such as sentences, phrases or short paragraphs. It is trained on a variety of data sources and a variety of tasks with the aim of dynamically accommodating a wide variety of natural language understanding tasks. The input is variable length English text and the output is a 512 dimensional vector. We apply this model to the STS benchmark for semantic similarity, and the results can be seen in the example notebook made available. The universal,sentence,encoder model is trained with a deep averaging network (DAN) encoder.,The details are described in the paper "[Universal Sentence Encoder](https://arxiv.org/abs/1803.11175)".



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/tfhub_use_lg_en_2.4.0_2.4_1587136993894.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = UniversalSentenceEncoder.pretrained("tfhub_use_lg","en","public/models")\
	.setInputCols("document","sentence")\
	.setOutputCol("sentence_embeddings")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|--------------------------|
| Model Name              | tfhub_use_lg             |
| Model Class             | UniversalSentenceEncoder |
| Spark Compatibility     | 2.4.0                    |
| Spark NLP Compatibility | 2.4                      |
| License                 | open source              |
| Edition                 | public                   |
| Input Labels            | document, sentence       |
| Output Labels           | sentence_embeddings      |
| Language                | en                       |
| Dimension               | 512.0                    |
| Case Sensitive          | 1.0                      |
| Upstream Dependencies   | USE                      |




{:.h2_title}
## Data Source
The model is imported from [https://tfhub.dev/google/universal-sentence-encoder-large/3](https://tfhub.dev/google/universal-sentence-encoder-large/3)

