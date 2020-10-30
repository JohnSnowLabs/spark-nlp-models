---
layout: model
title: BERT Base Cased
author: John Snow Labs
name: bert_base_cased
class: 
language: en
repository: public/models
date: 25/08/2020
tags: [embeddings]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
This model contains a deep bidirectional transformer trained on Wikipedia and the BookCorpus. The details are described in the paper "[BERT: Pre,training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)".



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_base_cased_en_2.2.0_2.4_1598340336670.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = BertEmbeddings.pretrained("bert_base_cased","en","public/models")\
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
| Model Name              | bert_base_cased           |
| Model Class             | BertEmbeddings            |
| Spark Compatibility     | 2.2.0                     |
| Spark NLP Compatibility | 2.4                       |
| License                 | open source               |
| Edition                 | public                    |
| Input Labels            | document, sentence, token |
| Output Labels           | word_embeddings           |
| Language                | en                        |
| Dimension               | 768.0                     |
| Case Sensitive          | 1.0                       |




{:.h2_title}
## Data Source
The model is imported from [https://tfhub.dev/google/bert_cased_L-24_H-1024_A-16/1](https://tfhub.dev/google/bert_cased_L-24_H-1024_A-16/1)

