---
layout: model
title: Deidentify Large
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-07-19
tags: [clinical,deidentify,en]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Deidentify (Large) is a deidentification model. It identifies instances of protected health information in text documents, and it can either obfuscate them (e.g., replacing names with different, fake names) or mask them (e.g., replacing "2020,06,04" with "<DATE>"). This model is useful for maintaining HIPAA compliance when dealing with text documents that contain protected health information.

 {:.h2_title}
## Predicted Entities
Contact, Location, Name, Profession 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT){:.button.button-orange}<br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.Clinical_DeIdentificiation.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/deidentify_large_en_2.5.1_2.4_1595199111307.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
| Model Name              | deidentify_large       |
| Model Class             | DeIdentificationModel  |
| Spark Compatibility     | 2.5.1                  |
| Spark NLP Compatibility | 2.4                    |
| License                 | Licensed               |
| Edition                 | Official               |
| Input Labels            | document, token, chunk |
| Output Labels           | document               |
| Language                | en                     |
| Upstream Dependencies   | ner_deid_large         |





{:.h2_title}
## Data Source
Trained on 10.000 Contact, Location, Name and Profession random replacements.

