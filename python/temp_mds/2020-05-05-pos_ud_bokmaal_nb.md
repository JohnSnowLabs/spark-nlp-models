---
layout: model
title: Part of Speech for Norwegian
author: John Snow Labs
name: pos_ud_bokmaal
class: 
language: nb
repository: public/models
date: 05/05/2020
tags: [pos]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
This model annotates the part of speech of tokens in a text. The [parts of speech](https://universaldependencies.org/u/pos/) annotated include PRON (pronoun), CCONJ (coordinating conjunction), and 15 others. The part of speech model is useful for extracting the grammatical structure of a piece of text automatically.



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/>[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/2da56c087da53a2fac1d51774d49939e05418e57/tutorials/Certification_Trainings/Public/6.Playground_DataFrames.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/pos_ud_bokmaal_nb_2.5.0_2.4_1588693881973.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = PerceptronModel.pretrained("pos_ud_bokmaal","nb","public/models")\
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
| Model Name              | pos_ud_bokmaal  |
| Model Class             | PerceptronModel |
| Spark Compatibility     | 2.5.0           |
| Spark NLP Compatibility | 2.4             |
| License                 | open source     |
| Edition                 | public          |
| Input Labels            | token, sentence |
| Output Labels           | pos             |
| Language                | nb              |
| Case Sensitive          | 0.0             |
| Upstream Dependencies   | POS UD          |




{:.h2_title}
## Data Source
The model is imported from [https://universaldependencies.org](https://universaldependencies.org)

