---
layout: model
title: Deidentify DL
author: John Snow Labs
name: deidentify_dl
class: NerDLModel
language: en
repository: clinical/models
date: 28/01/2020
tags: [clinical,ner]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
AGE,BIOID,CITY,COUNTRY,DATE,DOCTOR,EMAIL,FAX,HEALTHPLAN,HOSPITAL,IDNUM,MEDICALRECORD,ORGANIZATION,OTHER,PATIENT,PHONE,PROFESSION,STATE,STREET,USERNAME,X,ZIP 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/deidentify_dl_en_2.4.0_2.4_1580237286004.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model Name              | deidentify_dl                                                                                                                                                |
| Model Class             | NerDLModel                                                                                                                                                   |
| Spark Compatibility     | 2.4.0                                                                                                                                                        |
| Spark NLP Compatibility | 2.4                                                                                                                                                          |
| License                 | Licensed                                                                                                                                                     |
| Edition                 | Healthcare                                                                                                                                                   |
| Input Labels            |                                                                                                                                                              |
| Output Labels           | AGE,BIOID,CITY,COUNTRY,DATE,DOCTOR,EMAIL,FAX,HEALTHPLAN,HOSPITAL,IDNUM,MEDICALRECORD,ORGANIZATION,OTHER,PATIENT,PHONE,PROFESSION,STATE,STREET,USERNAME,X,ZIP |
| Language                | en                                                                                                                                                           |
| Dimension               |                                                                                                                                                              |
| Case Sensitive          |                                                                                                                                                              |
| Upstream Dependencies   | embeddings_clinical                                                                                                                                          |




{:.h2_title}
## Data Source
Rule based DeIdentifier based on `ner_deid`

