---
layout: model
title: Ner DL Model Diseases
author: John Snow Labs
name: ner_diseases
class: NerDLModel
language: en
repository: clinical/models
date: 17/03/2020
tags: [clinical,ner]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Pretrained named entity recognition deep learning model for diseases.

 {:.h2_title}
## Predicted Entities
Disease 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_DIAG_PROC/){:.button.button-orange}<br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_diseases_en_2.4.4_2.4_1584452534235.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|---------------------|
| Model Name              | ner_diseases        |
| Model Class             | NerDLModel          |
| Spark Compatibility     | 2.4.4               |
| Spark NLP Compatibility | 2.4                 |
| License                 | Licensed            |
| Edition                 | Healthcare          |
| Input Labels            |                     |
| Output Labels           | Disease             |
| Language                | en                  |
| Dimension               |                     |
| Case Sensitive          | 0.0                 |
| Upstream Dependencies   | embeddings_clinical |




{:.h2_title}
## Data Source

Trained on i2b2 with `embeddings_clinical`

