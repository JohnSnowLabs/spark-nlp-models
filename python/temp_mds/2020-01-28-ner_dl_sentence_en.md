---
layout: model
title: 
author: John Snow Labs
name: ner_dl_sentence
class: 
language: en
repository: public/models
date: 28/01/2020
tags: [sentence_detector]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ner_dl_sentence_en_2.0.2_2.4_1580252313303.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = DeepSentenceDetector.pretrained("ner_dl_sentence","en","public/models")\
	.setInputCols("document")\
	.setOutputCol("sentence")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|----------------------|
| Model Name              | ner_dl_sentence      |
| Model Class             | DeepSentenceDetector |
| Spark Compatibility     | 2.0.2                |
| Spark NLP Compatibility | 2.4                  |
| License                 | open source          |
| Edition                 | public               |
| Input Labels            | document             |
| Output Labels           | sentence             |
| Language                | en                   |




{:.h2_title}
## Data Source


