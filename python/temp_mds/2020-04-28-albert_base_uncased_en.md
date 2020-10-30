---
layout: model
title: ALBERT Base Uncase
author: John Snow Labs
name: albert_base_uncased
class: 
language: en
repository: public/models
date: 28/04/2020
tags: [embeddings]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
ALBERT is "A Lite" version of BERT, a popular unsupervised language representation learning algorithm. ALBERT uses parameter,reduction techniques that allow for large,scale configurations, overcome previous memory limitations, and achieve better behavior with respect to model degradation. The details are described in the paper "[ALBERT: A Lite BERT for Self,supervised Learning of Language Representations.](https://arxiv.org/abs/1909.11942)"



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/albert_base_uncased_en_2.5.0_2.4_1588073363475.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = AlbertEmbeddings.pretrained("albert_base_uncased","en","public/models")\
	.setInputCols("document","sentence","token")\
	.setOutputCol("word_embeddings")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|---------------------------|
| Model Name              | albert_base_uncased       |
| Model Class             | AlbertEmbeddings          |
| Spark Compatibility     | 2.5.0                     |
| Spark NLP Compatibility | 2.4                       |
| License                 | open source               |
| Edition                 | public                    |
| Input Labels            | document, sentence, token |
| Output Labels           | word_embeddings           |
| Language                | en                        |
| Dimension               | 768.0                     |
| Case Sensitive          | 0.0                       |




{:.h2_title}
## Data Source
The model is imported from [https://tfhub.dev/google/albert_base/3](https://tfhub.dev/google/albert_base/3)

