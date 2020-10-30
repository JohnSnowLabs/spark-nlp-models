---
layout: model
title: Classifierdl Biobert-clinical Adverse Events
author: John Snow Labs
name: classifierdl_ade_clinicalbert
class: 
language: en
repository: clinical/models
date: 06/10/2020
tags: [clinical,classifier]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Classify if a user review/tweet contains any adverse drug reaction

 {:.h2_title}
## Predicted Entities
True, False 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/classifierdl_ade_clinicalbert_en_2.6.0_2.4_1601594738356.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = ClassifierDLModel.pretrained("classifierdl_ade_clinicalbert","en","clinical/models")\
	.setInputCols("sentence_embeddings","label")\
	.setOutputCol("category")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|-------------------------------|
| Model Name              | classifierdl_ade_clinicalbert |
| Model Class             | ClassifierDLModel             |
| Spark Compatibility     | 2.6.2                         |
| Spark NLP Compatibility | 2.4                           |
| License                 | Licensed                      |
| Edition                 | Healthcare                    |
| Input Labels            | sentence_embeddings, label    |
| Output Labels           | category                      |
| Language                | en                            |
| Upstream Dependencies   | biobert_clinical_base_cased   |




{:.h2_title}
## Data Source
Trained on DRUG-AE, 2018 i2b2, CADEC, and twitter ADE dataset

