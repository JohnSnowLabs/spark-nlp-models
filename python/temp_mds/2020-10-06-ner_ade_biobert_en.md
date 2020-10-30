---
layout: model
title: NER Adverse Drug Events
author: John Snow Labs
name: ner_ade_biobert
class: 
language: en
repository: clinical/models
date: 06/10/2020
tags: [clinical,ner]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Extract adverse drug reaction events and drug entites from text

 {:.h2_title}
## Predicted Entities
ADE, DRUG 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_ade_biobert_en_2.6.0_2.4_1601594787264.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = NerDLModel.pretrained("ner_ade_biobert","en","clinical/models")\
	.setInputCols("sentence","token","word_embeddings")\
	.setOutputCol("ner")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|----------------------------------|
| Model Name              | ner_ade_biobert                  |
| Model Class             | NerDLModel                       |
| Spark Compatibility     | 2.6.2                            |
| Spark NLP Compatibility | 2.4                              |
| License                 | Licensed                         |
| Edition                 | Healthcare                       |
| Input Labels            | sentence, token, word_embeddings |
| Output Labels           | ner                              |
| Language                | en                               |
| Upstream Dependencies   | biobert_pubmed_base_cased        |




{:.h2_title}
## Data Source
Trained on DRUG-AE, 2018 i2b2, CADEC, and twitter ADE dataset

