---
layout: model
title: 
author: John Snow Labs
name: pos_ud_ewt
class: 
language: en
repository: public/models
date: 07/10/2019
tags: [pos]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_ewt_en_2.2.2_2.4_1570464827452.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = PerceptronModel.pretrained("pos_ud_ewt","en","public/models")\
	.setInputCols("token","sentence")\
	.setOutputCol("pos")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|-----------------|
| Model Name              | pos_ud_ewt      |
| Model Class             | PerceptronModel |
| Spark Compatibility     | 2.2.2           |
| Spark NLP Compatibility | 2.4             |
| License                 | open source     |
| Edition                 | public          |
| Input Labels            | token, sentence |
| Output Labels           | pos             |
| Language                | en              |
| Upstream Dependencies   | POS UD          |




{:.h2_title}
## Data Source


