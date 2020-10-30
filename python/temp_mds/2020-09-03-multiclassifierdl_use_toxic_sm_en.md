---
layout: model
title: 
author: John Snow Labs
name: multiclassifierdl_use_toxic_sm
class: 
language: en
repository: public/models
date: 03/09/2020
tags: [classifier]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/multiclassifierdl_use_toxic_sm_en_2.6.0_2.4_1599144262902.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = MultiClassifierDLModel.pretrained("multiclassifierdl_use_toxic_sm","en","public/models")\
	.setInputCols("sentence_embeddings","label")\
	.setOutputCol("category")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|--------------------------------|
| Model Name              | multiclassifierdl_use_toxic_sm |
| Model Class             | MultiClassifierDLModel         |
| Spark Compatibility     | 2.6.0                          |
| Spark NLP Compatibility | 2.4                            |
| License                 | open source                    |
| Edition                 | public                         |
| Input Labels            | sentence_embeddings, label     |
| Output Labels           | category                       |
| Language                | en                             |
| Upstream Dependencies   | with tfhub_use                 |




{:.h2_title}
## Data Source


