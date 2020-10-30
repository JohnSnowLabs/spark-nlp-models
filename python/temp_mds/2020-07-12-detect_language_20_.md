---
layout: model
title: LanguageDetectorDL
author: John Snow Labs
name: detect_language_20
class: 
language: 
repository: public/models
date: 12/07/2020
tags: [pipeline]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/detect_language_20_xx_2.5.0_2.4_1594580840930.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = Pipeline.pretrained("detect_language_20","","public/models")\
	.setInputCols("")\
	.setOutputCol("")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|--------------------|
| Model Name              | detect_language_20 |
| Model Class             | Pipeline           |
| Spark Compatibility     | 2.5.0              |
| Spark NLP Compatibility | 2.4                |
| License                 | open source        |
| Edition                 | public             |




{:.h2_title}
## Data Source


