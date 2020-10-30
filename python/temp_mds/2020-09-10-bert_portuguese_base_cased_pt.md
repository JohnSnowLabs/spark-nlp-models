---
layout: model
title: 
author: John Snow Labs
name: bert_portuguese_base_cased
class: 
language: pt
repository: public/models
date: 10/09/2020
tags: [embeddings]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_portuguese_base_cased_pt_2.6.0_2.4_1599740263165.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = BertEmbeddings.pretrained("bert_portuguese_base_cased","pt","public/models")\
	.setInputCols("document","sentence","token")\
	.setOutputCol("word_embeddings")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|----------------------------|
| Model Name              | bert_portuguese_base_cased |
| Model Class             | BertEmbeddings             |
| Spark Compatibility     | 2.6.0                      |
| Spark NLP Compatibility | 2.4                        |
| License                 | open source                |
| Edition                 | public                     |
| Input Labels            | document, sentence, token  |
| Output Labels           | word_embeddings            |
| Language                | pt                         |




{:.h2_title}
## Data Source


