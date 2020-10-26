---
layout: model
title: ChunkResolver Icd10cm Clinical
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-04-21
tags: [clinical,entity_resolution,icd10,en]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
ICD10-CM Codes and their normalized definition with `clinical_embeddings` 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICD10_CM/){:.button.button-orange}<br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/jupyter/enterprise/healthcare/EntityResolution_ICD10_RxNorm_Detailed.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10cm_clinical_en_2.4.5_2.4_1587491222166.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|-------------------------------|
| Model Name              | chunkresolve_icd10cm_clinical |
| Model Class             | ChunkEntityResolverModel      |
| Spark Compatibility     | 2.4.2                         |
| Spark NLP Compatibility | 2.4                           |
| License                 | Licensed                      |
| Edition                 | Official                      |
| Input Labels            | token, chunk_embeddings       |
| Output Labels           | entity                        |
| Language                | en                            |
| Case Sensitive          | True                          |
| Upstream Dependencies   | embeddings_clinical           |





{:.h2_title}
## Data Source
Trained on ICD10 Clinical Modification datasetwith tenths of variations per code.

