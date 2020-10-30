---
layout: model
title: Ner DL Model Events `embeddings_healthcare`
author: John Snow Labs
name: ner_events_healthcare
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


 {:.h2_title}
## Predicted Entities
CLINICAL_DEPT,DATE,DURATION,EVIDENTIAL,FREQUENCY,OCCURRENCE,PROBLEM,TEST,TIME,TREATMENT 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_events_healthcare_en_2.6.0_2.4_1600849907632.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|-----------------------------------------------------------------------------------------|
| Model Name              | ner_events_healthcare                                                                   |
| Model Class             | NerDLModel                                                                              |
| Spark Compatibility     | 2.6.0                                                                                   |
| Spark NLP Compatibility | 2.4                                                                                     |
| License                 | Licensed                                                                                |
| Edition                 | Healthcare                                                                              |
| Input Labels            |                                                                                         |
| Output Labels           | CLINICAL_DEPT,DATE,DURATION,EVIDENTIAL,FREQUENCY,OCCURRENCE,PROBLEM,TEST,TIME,TREATMENT |
| Language                | en                                                                                      |
| Dimension               |                                                                                         |
| Case Sensitive          |                                                                                         |
| Upstream Dependencies   | embeddings_healthcare_100d                                                              |




{:.h2_title}
## Data Source
Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_healthcare_100d`

