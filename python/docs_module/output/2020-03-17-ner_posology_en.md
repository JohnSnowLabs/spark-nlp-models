---
layout: model
title: Ner DL Model Posology
author: John Snow Labs
name: ner_posology
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
Pretrained named entity recognition deep learning model for posology, this NER is trained with the 'embeddings_clinical' word embeddings model, so be sure to use the same embeddings in the pipeline

 {:.h2_title}
## Predicted Entities
DOSAGE,DRUG,DURATION,FORM,FREQUENCY,ROUTE,STRENGTH 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_POSOLOGY/){:.button.button-orange}<br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_posology_en_2.4.4_2.4_1584452534235.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|----------------------------------------------------|
| Model Name              | ner_posology                                       |
| Model Class             | NerDLModel                                         |
| Spark Compatibility     | 2.4.2                                              |
| Spark NLP Compatibility | 2.4                                                |
| License                 | Licensed                                           |
| Edition                 | Healthcare                                         |
| Input Labels            |                                                    |
| Output Labels           | DOSAGE,DRUG,DURATION,FORM,FREQUENCY,ROUTE,STRENGTH |
| Language                | en                                                 |
| Dimension               |                                                    |
| Case Sensitive          | 0.0                                                |
| Upstream Dependencies   | embeddings_clinical                                |




{:.h2_title}
## Data Source

Trained on the 2018 i2b2 dataset and FDA Drug datasets with `embeddings_clinical`.

