---
layout: model
title: ChunkResolver Athena Conditions Healthcare
author: John Snow Labs
name: chunkresolve_athena_conditions_healthcare
class: 
language: en
repository: clinical/models
date: 16/09/2020
tags: [clinical,entity_resolver,athena]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
Athena Codes and their normalized definition 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_athena_conditions_healthcare_en_2.6.0_2.4_1600265258887.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = ChunkEntityResolverModel.pretrained("chunkresolve_athena_conditions_healthcare","en","clinical/models")\
	.setInputCols("token","chunk_embeddings")\
	.setOutputCol("entity")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|-------------------------------------------|
| Model Name              | chunkresolve_athena_conditions_healthcare |
| Model Class             | ChunkEntityResolverModel                  |
| Spark Compatibility     | 2.6.0                                     |
| Spark NLP Compatibility | 2.4                                       |
| License                 | Licensed                                  |
| Edition                 | Healthcare                                |
| Input Labels            | token, chunk_embeddings                   |
| Output Labels           | entity                                    |
| Language                | en                                        |
| Case Sensitive          | 1.0                                       |
| Upstream Dependencies   | embeddings_healthcare_100d                |




{:.h2_title}
## Data Source
Trained on Athena dataset

