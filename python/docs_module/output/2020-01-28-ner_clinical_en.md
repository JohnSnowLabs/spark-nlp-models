---
layout: model
title: Ner DL Model Clinical
author: John Snow Labs
name: ner_clinical
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
Pretrained named entity recognition deep learning model for clinical terms.

 {:.h2_title}
## Predicted Entities
Problem, Test, Treatment 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_DIAG_PROC/){:.button.button-orange}<br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_en_2.4.0_2.4_1580237286004.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|--------------------------|
| Model Name              | ner_clinical             |
| Model Class             | NerDLModel               |
| Spark Compatibility     | 2.4.0                    |
| Spark NLP Compatibility | 2.4                      |
| License                 | Licensed                 |
| Edition                 | Healthcare               |
| Input Labels            |                          |
| Output Labels           | Problem, Test, Treatment |
| Language                | en                       |
| Dimension               |                          |
| Case Sensitive          | 0.0                      |
| Upstream Dependencies   | embeddings_clinical      |




{:.h2_title}
## Data Source

Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_clinical`

