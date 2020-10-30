---
layout: model
title: 
author: John Snow Labs
name: sentimentdl_glove_imdb
class: 
language: en
repository: public/models
date: 05/05/2020
tags: [sentiment]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentimentdl_glove_imdb_en_2.5.0_2.4_1588682682507.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = SentimentDLModel.pretrained("sentimentdl_glove_imdb","en","public/models")\
	.setInputCols("sentence","label","sentence_embeddings")\
	.setOutputCol("category")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|--------------------------------------|
| Model Name              | sentimentdl_glove_imdb               |
| Model Class             | SentimentDLModel                     |
| Spark Compatibility     | 2.5.0                                |
| Spark NLP Compatibility | 2.4                                  |
| License                 | open source                          |
| Edition                 | public                               |
| Input Labels            | sentence, label, sentence_embeddings |
| Output Labels           | category                             |
| Language                | en                                   |
| Upstream Dependencies   | with glove_100d                      |




{:.h2_title}
## Data Source


