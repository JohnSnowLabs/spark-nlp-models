---
layout: model
title: ChunkResolver ICD10GM
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-09-06
tags: [clinical,entity_resolution,icd10,de]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
Codes and their normalized definition with `clinical_embeddings` 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICD10_GM_DE/){:.button.button-orange}<br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_ICD10GM_de_2.5.5_2.4_1599431635423.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|--------------------------|
| Model Name              | chunkresolve_ICD10GM     |
| Model Class             | ChunkEntityResolverModel |
| Spark Compatibility     | 2.5.5                    |
| Spark NLP Compatibility | 2.4                      |
| License                 | Licensed                 |
| Edition                 | Official                 |
| Input Labels            | token, chunk_embeddings  |
| Output Labels           | entity                   |
| Language                | de                       |
| Case Sensitive          | True                     |
| Upstream Dependencies   | w2v_cc_300d              |





{:.h2_title}
## Data Source
FILLUP.

