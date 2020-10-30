---
layout: model
title: Explain Clinical Doc Clinical Relation Assertion
author: John Snow Labs
name: explain_clinical_doc_cra
class: 
language: en
repository: clinical/models
date: 19/08/2020
tags: [clinical,pipeline]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
A pretrained pipeline with ner_clinical, assertion_dl, re_clinical. It will extract clinical entities, assign assertion status and find relationships between clinical entities.



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_cra_en_2.5.5_2.4_1597846145640.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = PretrainedPipeline("explain_clinical_doc_cra","en","clinical/models")

model.annotate("Include a healthcare document here. Can be a prescription, medical note, anything...")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|--------------------------|
| Model Name              | explain_clinical_doc_cra |
| Model Class             | PipelineModel            |
| Spark Compatibility     | 2.5.5                    |
| Spark NLP Compatibility | 2.4                      |
| License                 | Licensed                 |
| Edition                 | Healthcare               |
| Language                | en                       |




{:.h2_title}
## Data Source


