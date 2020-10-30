---
layout: model
title: Recognize Entities DL
author: John Snow Labs
name: recognize_entities_dl
class: 
language: 
repository: public/models
date: 19/03/2020
tags: [pipeline]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/recognize_entities_dl_en_2.1.0_2.4_1584626752821.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = Pipeline.pretrained("recognize_entities_dl","","public/models")\
	.setInputCols("")\
	.setOutputCol("")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|-----------------------|
| Model Name              | recognize_entities_dl |
| Model Class             | Pipeline              |
| Spark Compatibility     | 2.1.0                 |
| Spark NLP Compatibility | 2.4                   |
| License                 | open source           |
| Edition                 | public                |




{:.h2_title}
## Data Source


