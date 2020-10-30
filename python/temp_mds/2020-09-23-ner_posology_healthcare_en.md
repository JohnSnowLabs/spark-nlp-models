---
layout: model
title: 
author: John Snow Labs
name: ner_posology_healthcare
class: NerDLModel
language: en
repository: clinical/models
date: 23/09/2020
tags: [clinical,ner]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Pretrained named entity recognition deep learning model for posology, this NER is trained with the 'embeddings_healthcare' word embeddings model, so be sure to use the same embeddings in the pipeline

 {:.h2_title}
## Predicted Entities
Dosage,Drug,Duration,Form,Frequency,Route,Strength 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_posology_healthcare_en_2.6.0_2.4_1600849852424.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|----------------------------------------------------|
| Model Name              | ner_posology_healthcare                            |
| Model Class             | NerDLModel                                         |
| Spark Compatibility     | 2.6.0                                              |
| Spark NLP Compatibility | 2.4                                                |
| License                 | Licensed                                           |
| Edition                 | Healthcare                                         |
| Input Labels            |                                                    |
| Output Labels           | Dosage,Drug,Duration,Form,Frequency,Route,Strength |
| Language                | en                                                 |
| Dimension               |                                                    |
| Case Sensitive          |                                                    |
| Upstream Dependencies   | embeddings_healthcare                              |




{:.h2_title}
## Data Source
Trained on the 2018 i2b2 dataset and FDA Drug datasets with `embeddings_healthcare_100d`.

