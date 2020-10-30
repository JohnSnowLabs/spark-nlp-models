---
layout: model
title: 
author: John Snow Labs
name: sentiment_vivekn
class: 
language: en
repository: public/models
date: 30/04/2019
tags: [sentiment]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentiment_vivekn_en_2.0.2_2.4_1556663184035.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = ViveknSentimentModel.pretrained("sentiment_vivekn","en","public/models")\
	.setInputCols("sentence","sentiment_label","token")\
	.setOutputCol("sentiment")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|----------------------------------|
| Model Name              | sentiment_vivekn                 |
| Model Class             | ViveknSentimentModel             |
| Spark Compatibility     | 2.0.2                            |
| Spark NLP Compatibility | 2.4                              |
| License                 | open source                      |
| Edition                 | public                           |
| Input Labels            | sentence, sentiment_label, token |
| Output Labels           | sentiment                        |
| Language                | en                               |
| Upstream Dependencies   | Sentiment                        |




{:.h2_title}
## Data Source


