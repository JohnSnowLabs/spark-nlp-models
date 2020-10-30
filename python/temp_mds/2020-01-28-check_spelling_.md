---
layout: model
title: Check Spelling
author: John Snow Labs
name: check_spelling
class: 
language: 
repository: public/models
date: 28/01/2020
tags: [pipeline]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/check_spelling_en_2.0.2_2.4_1580246859135.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = Pipeline.pretrained("check_spelling","","public/models")\
	.setInputCols("")\
	.setOutputCol("")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|----------------|
| Model Name              | check_spelling |
| Model Class             | Pipeline       |
| Spark Compatibility     | 2.0.2          |
| Spark NLP Compatibility | 2.4            |
| License                 | open source    |
| Edition                 | public         |




{:.h2_title}
## Data Source


