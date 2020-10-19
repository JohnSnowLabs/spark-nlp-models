---
layout: model
title: Ner DL Model Clinical (Large)
author: John Snow Labs
name: ner_clinical_large
class: NerDLModel
language: en
repository: clinical/models
date: 21/05/2020
tags: [clinical,ner]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Clinical NER (Large) is a Named Entity Recognition model that annotates text to find references to clinical events. The entities it annotates are Problem, Treatment, and Test. Clinical NER is trained with the 'embeddings_clinical' word embeddings model, so be sure to use the same embeddings in the pipeline.

 {:.h2_title}
## Predicted Entities
Problem, Test, Treatment 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_EVENTS_CLINICAL/){:.button.button-orange}<br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_EVENTS_CLINICAL.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_large_en_2.5.0_2.4_1590021302624.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
| Model Name              | ner_clinical_large       |
| Model Class             | NerDLModel               |
| Spark Compatibility     | 2.5.0                    |
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

Trained on i2b2 augmented data with `clinical_embeddings`

