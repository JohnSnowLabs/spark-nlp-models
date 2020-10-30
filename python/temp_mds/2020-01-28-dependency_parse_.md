---
layout: model
title: Dependency Parse
author: John Snow Labs
name: dependency_parse
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
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/dependency_parse_en_2.0.2_2.4_1580255669655.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = Pipeline.pretrained("dependency_parse","","public/models")\
	.setInputCols("")\
	.setOutputCol("")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|------------------|
| Model Name              | dependency_parse |
| Model Class             | Pipeline         |
| Spark Compatibility     | 2.0.2            |
| Spark NLP Compatibility | 2.4              |
| License                 | open source      |
| Edition                 | public           |




{:.h2_title}
## Data Source


