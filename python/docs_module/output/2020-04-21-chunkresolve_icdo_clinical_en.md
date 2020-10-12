---
layout: model
title: ChunkResolver Icdo Clinical
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-04-21
tags: [clinical,entity_resolution,icd10,icdo,en]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
ICD-O Codes and their normalized definition with `clinical_embeddings` 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICDO/){:.button.button-orange}<br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icdo_clinical_en_2.4.5_2.4_1587491354644.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|----------------------------|
| Model Name              | chunkresolve_icdo_clinical |
| Model Class             | ChunkEntityResolverModel   |
| Spark Compatibility     | 2.4.2                      |
| Spark NLP Compatibility | 2.4                        |
| License                 | Licensed                   |
| Edition                 | Official                   |
| Input Labels            | token, chunk_embeddings    |
| Output Labels           | entity                     |
| Language                | en                         |
| Case Sensitive          | True                       |
| Upstream Dependencies   | embeddings_clinical        |





{:.h2_title}
## Data Source
Trained on ICD-O Histology Behaviour dataset.

