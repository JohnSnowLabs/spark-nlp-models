---
layout: model
title: Assertion ML
author: John Snow Labs
name: assertion_ml
class: AssertionLogRegModel
language: en
repository: clinical/models
date: 2020-01-28
tags: [clinical,assertion,dl,n2c2,en]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description
Assertion of Clinical Entities based on Logistic Regression
Deep learning named entity recognition model for assertions 

{:.h2_title}
## Prediction Domain
hypothetical, present, absent, possible, conditional, associated_with_someone_else

{:.h2_title}
## Data Source
Trained on 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text with `embeddings_clinical`
https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/

{:.btn-box}
[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.Clinical_Assertion_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_ml_en_2.4.0_2.4_1580237286004.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
{:.h2_title}
## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = AssertionLogRegModel.pretrained("assertion_ml","en","clinical/models")
	.setInputCols("document","chunk","word_embeddings")
	.setOutputCol("assertion")
```

```scala
val model = AssertionLogRegModel.pretrained("assertion_ml","en","clinical/models")
	.setInputCols("document","chunk","word_embeddings")
	.setOutputCol("assertion")
```
</div>



{:.model-param}
## Model Information

{:.table-model}
|----------------|----------------------------------|
| name           | assertion_ml                     |
| model_class    | AssertionLogRegModel             |
| compatibility  | 2.4.0                            |
| license        | Licensed                         |
| edition        | Healthcare                       |
| inputs         | document, chunk, word_embeddings |
| output         | assertion                        |
| language       | en                               |
| case_sensitive | False                            |
| upstream_deps  | embeddings_clinical              |

