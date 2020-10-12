---
layout: model
title: Ner DL Model Events `embeddings_clinical`
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-08-18
tags: [clinical,ner,events,en]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Pretrained named entity recognition deep learning model for clinical events.

 {:.h2_title}
## Predicted Entities
CLINICAL_DEPT,DATE,DURATION,EVIDENTIAL,FREQUENCY,OCCURRENCE,PROBLEM,TEST,TIME,TREATMENT 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_EVENTS_CLINICAL/){:.button.button-orange}<br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_events_clinical_en_2.5.5_2.4_1597775531760.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|----------------------------------|
| Model Name              | ner_events_clinical              |
| Model Class             | NerDLModel                       |
| Spark Compatibility     | 2.5.0                            |
| Spark NLP Compatibility | 2.4                              |
| License                 | Licensed                         |
| Edition                 | Official                         |
| Input Labels            | sentence, token, word_embeddings |
| Output Labels           | ner                              |
| Language                | en                               |
| Case Sensitive          | False                            |
| Upstream Dependencies   | embeddings_clinical              |





{:.h2_title}
## Data Source
Trained on i2b2 events data with `clinical_embeddings`.

