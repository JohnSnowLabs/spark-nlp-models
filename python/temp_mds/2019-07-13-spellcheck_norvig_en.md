---
layout: model
title: 
author: John Snow Labs
name: spellcheck_norvig
class: 
language: en
repository: public/models
date: 13/07/2019
tags: []
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/spellcheck_norvig_en_2.0.2_2.4_1563017660080.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = NorvigSweetingModel.pretrained("spellcheck_norvig","en","public/models")\
	.setInputCols("token")\
	.setOutputCol("token")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|---------------------|
| Model Name              | spellcheck_norvig   |
| Model Class             | NorvigSweetingModel |
| Spark Compatibility     | 2.0.2               |
| Spark NLP Compatibility | 2.4                 |
| License                 | open source         |
| Edition                 | public              |
| Input Labels            | token               |
| Output Labels           | token               |
| Language                | en                  |
| Upstream Dependencies   | Spell Checker       |




{:.h2_title}
## Data Source


