---
layout: model
title: Ner DL Model Clinical (Large)
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-05-21
tags: [clinical,ner,generic,large,en]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
PROBLEM,TEST,TREATMENT 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_large_clinical_en_2.5.0_2.4_1590021302624.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
| Model Name              | ner_large_clinical               |
| Model Class             | NerDLModel                       |
| Spark Compatibility     | 2.5.0                            |
| Spark NLP Compatibility | 2.4                              |
| License                 | Licensed                         |
| Edition                 | Official                         |
| Input Labels            | sentence, token, word_embeddings |
| Output Labels           | ner                              |
| Language                | en                               |
| Upstream Dependencies   | embeddings_clinical              |





{:.h2_title}
## Data Source
Trained on data gathered and manually annotated by John Snow Labs.

