---
layout: model
title: ChunkResolver Rxnorm Sbd Clinical
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-07-27
tags: [clinical,entity_resolution,rxnorm,en]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
RxNorm Codes and their normalized definition with `clinical_embeddings` 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_RXNORM/){:.button.button-orange}<br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_rxnorm_sbd_clinical_en_2.5.1_2.4_1595813912622.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|----------------------------------|
| Model Name              | chunkresolve_rxnorm_sbd_clinical |
| Model Class             | ChunkEntityResolverModel         |
| Spark Compatibility     | 2.5.1                            |
| Spark NLP Compatibility | 2.4                              |
| License                 | Licensed                         |
| Edition                 | Official                         |
| Input Labels            | token, chunk_embeddings          |
| Output Labels           | entity                           |
| Language                | en                               |
| Case Sensitive          | True                             |
| Upstream Dependencies   | embeddings_clinical              |





{:.h2_title}
## Data Source
Trained on December 2019 RxNorm Clinical Drugs (TTY=SBD) ontology graph with `embeddings_clinical`.

