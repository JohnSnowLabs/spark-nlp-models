---
layout: model
title: Ner DL Model Posology Large
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-04-21
tags: [clinical,ner,drugs,fda,large,en]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Pretrained named entity recognition deep learning model for posology, this NER is trained with the 'embeddings_clinical' word embeddings model, so be sure to use the same embeddings in the pipeline

 {:.h2_title}
## Predicted Entities
DOSAGE,DRUG,DURATION,FORM,FREQUENCY,ROUTE,STRENGTH 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_posology_large_en_2.4.2_2.4_1587513302751.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
| Model Name              | ner_posology_large               |
| Model Class             | NerDLModel                       |
| Spark Compatibility     | 2.4.2                            |
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
Trained on the 2018 i2b2 dataset and FDA Drug datasets with `embeddings_clinical`..

