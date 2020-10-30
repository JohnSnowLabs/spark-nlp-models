---
layout: model
title: Ner DL Model Healthcare
author: John Snow Labs
name: ner_healthcare
class: NerDLModel
language: en
repository: clinical/models
date: 23/09/2020
tags: [clinical,ner]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Pretrained named entity recognition deep learning model for healthcare.

 {:.h2_title}
## Predicted Entities
PROBLEM,TEST,TREATMENT 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_healthcare_en_2.6.0_2.4_1600849764614.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python

```

```scala

```
</div>



{:.model-param}
## Model Information
{:.table-model}
|-------------------------|------------------------|
| Model Name              | ner_healthcare         |
| Model Class             | NerDLModel             |
| Spark Compatibility     | 2.4.4                  |
| Spark NLP Compatibility | 2.4                    |
| License                 | Licensed               |
| Edition                 | Healthcare             |
| Input Labels            |                        |
| Output Labels           | PROBLEM,TEST,TREATMENT |
| Language                | en                     |
| Dimension               |                        |
| Case Sensitive          | 0.0                    |
| Upstream Dependencies   | FILLUP                 |




{:.h2_title}
## Data Source
Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_healthcare_100d`

