---
layout: model
title: ChunkResolver RxNorm Sbd Clinical
author: John Snow Labs
name: chunkresolve_rxnorm_sbd_clinical
class: 
language: en
repository: clinical/models
date: 27/07/2020
tags: [clinical,entity_resolver,rxnorm]
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
model = ChunkEntityResolverModel.pretrained("chunkresolve_rxnorm_sbd_clinical","en","clinical/models")\
	.setInputCols("token","chunk_embeddings")\
	.setOutputCol("entity")
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
| Edition                 | Healthcare                       |
| Input Labels            | token, chunk_embeddings          |
| Output Labels           | entity                           |
| Language                | en                               |
| Case Sensitive          | 1.0                              |
| Upstream Dependencies   | embeddings_clinical              |




{:.h2_title}
## Data Source
Trained on December 2019 RxNorm Clinical Drugs (TTY=SBD) ontology graph with `embeddings_clinical`

