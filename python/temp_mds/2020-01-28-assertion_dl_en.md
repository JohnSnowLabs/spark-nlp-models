---
layout: model
title: Assertion DL Clinical Embeddings
author: John Snow Labs
name: assertion_dl
class: 
language: en
repository: clinical/models
date: 28/01/2020
tags: [clinical,assertion]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Deep learning named entity recognition model for assertions 

 {:.h2_title}
## Predicted Entities
hypothetical, present, absent, possible, conditional, associated_with_someone_else 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/>[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.Clinical_Assertion_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_dl_en_2.4.0_2.4_1580237286004.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = AssertionDLModel.pretrained("assertion_dl","en","clinical/models")\
	.setInputCols("document","chunk","word_embeddings")\
	.setOutputCol("assertion")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|----------------------------------|
| Model Name              | assertion_dl                     |
| Model Class             | AssertionDLModel                 |
| Spark Compatibility     | 2.4.0                            |
| Spark NLP Compatibility | 2.4                              |
| License                 | Licensed                         |
| Edition                 | Healthcare                       |
| Input Labels            | document, chunk, word_embeddings |
| Output Labels           | assertion                        |
| Language                | en                               |
| Case Sensitive          | 0.0                              |
| Upstream Dependencies   | embeddings_clinical              |




{:.h2_title}
## Data Source
Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_clinical`

