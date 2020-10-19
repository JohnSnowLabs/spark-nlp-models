---
layout: model
title: Ner DL Model Risk Factors
author: John Snow Labs
name: ner_risk_factors
class: NerDLModel
language: en
repository: clinical/models
date: 21/04/2020
tags: [clinical,ner]
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

{:.h2_title}
## Results
```bash

```

{:.model-param}
## Model Information

{:.table-model}
|-------------------------|----------------------------------------------------------------------------------|
| Model Name              | ner_risk_factors                                                                 |
| Model Class             | NerDLModel                                                                       |
| Spark Compatibility     | 2.4.2                                                                            |
| Spark NLP Compatibility | 2.4                                                                              |
| License                 | Licensed                                                                         |
| Edition                 | Healthcare                                                                       |
| Input Labels            |                                                                                  |
| Output Labels           | CAD,DIABETES,FAMILY_HIST,HYPERLIPIDEMIA,HYPERTENSION,MEDICATION,OBESE,PHI,SMOKER |
| Language                | en                                                                               |
| Dimension               |                                                                                  |
| Case Sensitive          | 0.0                                                                              |
| Upstream Dependencies   | embeddings_clinical                                                              |




{:.h2_title}
## Data Source

Trained on plain n2c2 2014: De-identification and Heart Disease Risk Factors Challenge datasets with `embeddings_clinical`

