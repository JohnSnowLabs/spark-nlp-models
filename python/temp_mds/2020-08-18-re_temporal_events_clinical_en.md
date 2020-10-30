---
layout: model
title: Relation Extraction Model Clinical
author: John Snow Labs
name: re_temporal_events_clinical
class: 
language: en
repository: clinical/models
date: 18/08/2020
tags: [clinical,relation_extraction]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
TrIP (improved), TrWP (worsened), TrCP (caused problem), TrAP (administered), TrNAP (avoided), TeRP (revealed problem), TeCP (investigate problem), PIP (problems related) 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/RE_CLINICAL_EVENTS/){:.button.button-orange}<br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/10.Clinical_Relation_Extraction.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/re_temporal_events_clinical_en_2.5.5_2.4_1597774124917.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = RelationExtractionModel.pretrained("re_temporal_events_clinical","en","clinical/models")\
	.setInputCols("word_embeddings","chunk","pos","dependency")\
	.setOutputCol("category")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|-----------------------------------------|
| Model Name              | re_temporal_events_clinical             |
| Model Class             | RelationExtractionModel                 |
| Spark Compatibility     | 2.5.5                                   |
| Spark NLP Compatibility | 2.4                                     |
| License                 | Licensed                                |
| Edition                 | Healthcare                              |
| Input Labels            | word_embeddings, chunk, pos, dependency |
| Output Labels           | category                                |
| Language                | en                                      |
| Case Sensitive          | 0.0                                     |
| Upstream Dependencies   | embeddings_clinical                     |




{:.h2_title}
## Data Source
Trained on data gathered and manually annotated by John Snow Labs

