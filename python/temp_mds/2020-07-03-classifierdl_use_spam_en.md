---
layout: model
title: 
author: John Snow Labs
name: classifierdl_use_spam
class: 
language: en
repository: public/models
date: 03/07/2020
tags: [classifier]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/classifierdl_use_spam_en_2.5.3_2.4_1593783318934.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = ClassifierDLModel.pretrained("classifierdl_use_spam","en","public/models")\
	.setInputCols("sentence_embeddings","label")\
	.setOutputCol("category")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|----------------------------|
| Model Name              | classifierdl_use_spam      |
| Model Class             | ClassifierDLModel          |
| Spark Compatibility     | 2.5.3                      |
| Spark NLP Compatibility | 2.4                        |
| License                 | open source                |
| Edition                 | public                     |
| Input Labels            | sentence_embeddings, label |
| Output Labels           | category                   |
| Language                | en                         |
| Upstream Dependencies   | with tfhub_use             |




{:.h2_title}
## Data Source


