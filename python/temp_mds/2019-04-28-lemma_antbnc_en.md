---
layout: model
title: 
author: John Snow Labs
name: lemma_antbnc
class: 
language: en
repository: public/models
date: 28/04/2019
tags: [lemmatizer]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lemma_antbnc_en_2.0.2_2.4_1556480454569.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = LemmatizerModel.pretrained("lemma_antbnc","en","public/models")\
	.setInputCols("token")\
	.setOutputCol("lemma")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|-----------------|
| Model Name              | lemma_antbnc    |
| Model Class             | LemmatizerModel |
| Spark Compatibility     | 2.0.2           |
| Spark NLP Compatibility | 2.4             |
| License                 | open source     |
| Edition                 | public          |
| Input Labels            | token           |
| Output Labels           | lemma           |
| Language                | en              |
| Upstream Dependencies   | Lemmatizer      |




{:.h2_title}
## Data Source


