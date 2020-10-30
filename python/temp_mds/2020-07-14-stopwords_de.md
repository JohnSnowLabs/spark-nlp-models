---
layout: model
title: Stop Words Cleaner for German
author: John Snow Labs
name: stopwords
class: 
language: de
repository: public/models
date: 14/07/2020
tags: [stopwords_cleaner]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
This model removes 'stop words' from text. Stop words are words so common that they can removed without significantly altering the meaning of a text. Removing stop words is useful when one wants to deal with only the most semantically important words in a text, and ignore words that are rarely semantically relevant, such as articles and prepositions.



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/>[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/b2eb08610dd49d5b15077cc499a94b4ec1e8b861/jupyter/annotation/english/stop-words/StopWordsCleaner.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/stopwords_de_2.5.4_2.4_1594742442247.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = StopWordsCleaner.pretrained("stopwords","de","public/models")\
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
| Language                | de               |
| Case Sensitive          | 0.0              |




{:.h2_title}
## Data Source
The model is imported from [https://github.com/WorldBrain/remove-stopwords](https://github.com/WorldBrain/remove-stopwords)

