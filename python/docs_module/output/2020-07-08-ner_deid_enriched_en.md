---
layout: model
title: Deidentification NER (Enriched)
author: John Snow Labs
name: ner_deid_enriched
class: NerDLModel
language: en
repository: clinical/models
date: 08/07/2020
tags: [clinical,ner]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Deidentification NER (Enriched) is a Named Entity Recognition model that annotates text to find protected health information that may need to be deidentified. The entities it annotates are Age, City, Country, Date, Doctor, Hospital, Idnum, Medicalrecord, Organization, Patient, Phone, Profession, State, Street, Username, and Zip. Clinical NER is trained with the 'embeddings_clinical' word embeddings model, so be sure to use the same embeddings in the pipeline.

 {:.h2_title}
## Predicted Entities
Age, City, Country, Date, Doctor, Hospital, Idnum, Medicalrecord, Organization, Patient, Phone, Profession, State, Street, Username, Zip 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_DEMOGRAPHICS/){:.button.button-orange}<br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_DEMOGRAPHICS.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_enriched_en_2.5.3_2.4_1594170530497.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python

```

```scala

```
</div>

{:.h2_title}
## Results
```bash

```

{:.model-param}
## Model Information

{:.table-model}
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Model Name              | ner_deid_enriched                                                                                                                        |
| Model Class             | NerDLModel                                                                                                                               |
| Spark Compatibility     | 2.4.2                                                                                                                                    |
| Spark NLP Compatibility | 2.4                                                                                                                                      |
| License                 | Licensed                                                                                                                                 |
| Edition                 | Healthcare                                                                                                                               |
| Input Labels            |                                                                                                                                          |
| Output Labels           | Age, City, Country, Date, Doctor, Hospital, Idnum, Medicalrecord, Organization, Patient, Phone, Profession, State, Street, Username, Zip |
| Language                | en                                                                                                                                       |
| Dimension               |                                                                                                                                          |
| Case Sensitive          | 0.0                                                                                                                                      |
| Upstream Dependencies   | embeddings_clinical                                                                                                                      |




{:.h2_title}
## Data Source

Trained on JSL enriched n2c2 2014: De-identification and Heart Disease Risk Factors Challenge datasets with `embeddings_clinical`

