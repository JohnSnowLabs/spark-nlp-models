---
layout: model
title: Assertion DL Healthcare Embeddings
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-09-23
tags: [clinical,assertion]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Deep learning named entity recognition model for assertions.

 {:.h2_title}
## Predicted Entities
hypothetical, present, absent, possible, conditional, associated_with_someone_else 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/>[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.Clinical_Assertion_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_dl_healthcare_en_2.6.0_2.4_1600849811713.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
| Model Name              | assertion_dl_healthcare          |
| Model Class             | AssertionDLModel                 |
| Spark Compatibility     | 2.6.0                            |
| Spark NLP Compatibility | 2.4                              |
| License                 | Licensed                         |
| Edition                 | Official                         |
| Input Labels            | document, chunk, word_embeddings |
| Output Labels           | assertion                        |
| Language                | en                               |
| Case Sensitive          | False                            |
| Upstream Dependencies   | embeddings_healthcare_100d       |





{:.h2_title}
## Data Source
Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_clinical`.

