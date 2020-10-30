---
layout: model
title: ChunkResolver LOINC Clinical
author: John Snow Labs
name: chunkresolve_loinc_clinical
class: 
language: en
repository: clinical/models
date: 16/05/2020
tags: [clinical,entity_resolver]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
LOINC Codes and ther Standard Name with `clinical_embeddings` 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_loinc_clinical_en_2.5.0_2.4_1589599195201.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = ChunkEntityResolverModel.pretrained("chunkresolve_loinc_clinical","en","clinical/models")\
	.setInputCols("token","chunk_embeddings")\
	.setOutputCol("entity")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|-----------------------------|
| Model Name              | chunkresolve_loinc_clinical |
| Model Class             | ChunkEntityResolverModel    |
| Spark Compatibility     | 2.5.0                       |
| Spark NLP Compatibility | 2.4                         |
| License                 | Licensed                    |
| Edition                 | Healthcare                  |
| Input Labels            | token, chunk_embeddings     |
| Output Labels           | entity                      |
| Language                | en                          |
| Case Sensitive          | 1.0                         |
| Upstream Dependencies   | embeddings_clinical         |




{:.h2_title}
## Data Source
Trained on LOINC dataset with `embeddings_clinical`

