---
layout: model
title: 
author: John Snow Labs
name: stopwords
class: 
language: el
repository: public/models
date: 14/07/2020
tags: [stopwords_cleaner]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/stopwords_el_2.5.4_2.4_1594742437880.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = StopWordsCleaner.pretrained("stopwords","el","public/models")\
	.setInputCols("token")\
	.setOutputCol("cleanTokens")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|------------------|
| Model Name              | stopwords        |
| Model Class             | StopWordsCleaner |
| Spark Compatibility     | 2.5.4            |
| Spark NLP Compatibility | 2.4              |
| License                 | open source      |
| Edition                 | public           |
| Input Labels            | token            |
| Output Labels           | cleanTokens      |
| Language                | el               |




{:.h2_title}
## Data Source


