---
layout: model
title: ChunkResolver ICD10CM Neoplasms Clinical
author: John Snow Labs
name: chunkresolve_icd10cm_neoplasms_clinical
class: 
language: en
repository: clinical/models
date: 28/04/2020
tags: [clinical,entity_resolver,icd10]
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
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICD10_CM/){:.button.button-orange}<br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10cm_neoplasms_clinical_en_2.4.5_2.4_1588108205630.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = ChunkEntityResolverModel.pretrained("chunkresolve_icd10cm_neoplasms_clinical","en","clinical/models")\
	.setInputCols("token","chunk_embeddings")\
	.setOutputCol("entity")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|-----------------------------------------|
| Model Name              | chunkresolve_icd10cm_neoplasms_clinical |
| Model Class             | ChunkEntityResolverModel                |
| Spark Compatibility     | 2.4.5                                   |
| Spark NLP Compatibility | 2.4                                     |
| License                 | Licensed                                |
| Edition                 | Healthcare                              |
| Input Labels            | token, chunk_embeddings                 |
| Output Labels           | entity                                  |
| Language                | en                                      |
| Case Sensitive          | 1.0                                     |
| Upstream Dependencies   | embeddings_clinical                     |




{:.h2_title}
## Data Source
Trained on ICD10CM Dataset Ranges: C000-D489, R590-R599

