---
layout: model
title: Ner DL Model Risk Factors
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-04-21
tags: [clinical,ner,risk,factors,en]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Pretrained named entity recognition deep learning model for Heart Disease Risk Factors and Personal Health Information.

 {:.h2_title}
## Predicted Entities
CAD,DIABETES,FAMILY_HIST,HYPERLIPIDEMIA,HYPERTENSION,MEDICATION,OBESE,PHI,SMOKER 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_RISK_FACTORS/){:.button.button-orange}<br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_risk_factors_en_2.4.2_2.4_1587513300751.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
| Model Name              | ner_risk_factors                 |
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
Trained on plain n2c2 2014: De-identification and Heart Disease Risk Factors Challenge datasets with `embeddings_clinical`.

