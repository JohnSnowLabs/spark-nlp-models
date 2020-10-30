---
layout: model
title: 
author: John Snow Labs
name: bert_multi_cased
class: 
language: xx
repository: public/models
date: 25/08/2020
tags: [embeddings]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_multi_cased_xx_2.0.3_2.4_1598341875191.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = BertEmbeddings.pretrained("bert_multi_cased","xx","public/models")\
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
| Model Name              | bert_multi_cased          |
| Model Class             | BertEmbeddings            |
| Spark Compatibility     | 2.0.3                     |
| Spark NLP Compatibility | 2.4                       |
| License                 | open source               |
| Edition                 | public                    |
| Input Labels            | document, sentence, token |
| Output Labels           | word_embeddings           |
| Language                | xx                        |




{:.h2_title}
## Data Source


