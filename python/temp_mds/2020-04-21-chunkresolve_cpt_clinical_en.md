---
layout: model
title: ChunkResolver CPT Clinical
author: John Snow Labs
name: chunkresolve_cpt_clinical
class: 
language: en
repository: clinical/models
date: 21/04/2020
tags: [clinical,entity_resolver,cpt]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
chunkresolve_cpt_clinical Codes and their normalized definition 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_cpt_clinical_en_2.4.5_2.4_1587491373378.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = ChunkEntityResolverModel.pretrained("chunkresolve_cpt_clinical","en","clinical/models")\
	.setInputCols("token","chunk_embeddings")\
	.setOutputCol("entity")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|---------------------------|
| Model Name              | chunkresolve_cpt_clinical |
| Model Class             | ChunkEntityResolverModel  |
| Spark Compatibility     | 2.4.2                     |
| Spark NLP Compatibility | 2.4                       |
| License                 | Licensed                  |
| Edition                 | Healthcare                |
| Input Labels            | token, chunk_embeddings   |
| Output Labels           | entity                    |
| Language                | en                        |
| Case Sensitive          | 1.0                       |
| Upstream Dependencies   | embeddings_clinical       |




{:.h2_title}
## Data Source
Trained on Current Procedural Terminology dataset

