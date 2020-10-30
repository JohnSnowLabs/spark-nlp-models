---
layout: model
title: POS Tagger Clinical
author: John Snow Labs
name: pos_clinical
class: 
language: en
repository: clinical/models
date: 30/04/2019
tags: [clinical,pos]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/pos_clinical_en_2.0.2_2.4_1556660550177.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = PerceptronModel.pretrained("pos_clinical","en","clinical/models")\
	.setInputCols("token","sentence")\
	.setOutputCol("pos")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|---------------------|
| Model Name              | pos_clinical        |
| Model Class             | PerceptronModel     |
| Spark Compatibility     | 2.0.2               |
| Spark NLP Compatibility | 2.4                 |
| License                 | Licensed            |
| Edition                 | Healthcare          |
| Input Labels            | token, sentence     |
| Output Labels           | pos                 |
| Language                | en                  |
| Upstream Dependencies   | embeddings_clinical |




{:.h2_title}
## Data Source
Trained with MedPost dataset

