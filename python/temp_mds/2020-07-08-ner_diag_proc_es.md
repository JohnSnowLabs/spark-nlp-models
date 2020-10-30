---
layout: model
title: Ner DL Model Clinical
author: John Snow Labs
name: ner_diag_proc
class: 
language: es
repository: clinical/models
date: 08/07/2020
tags: [clinical,ner]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Pretrained named entity recognition deep learning model for diagnostics and procedures in spanish

 {:.h2_title}
## Predicted Entities
Diagnostico, Procedimiento 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_diag_proc_es_2.5.3_2.4_1594168623415.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = NerDLModel.pretrained("ner_diag_proc","es","clinical/models")\
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
| Model Name              | ner_diag_proc                    |
| Model Class             | NerDLModel                       |
| Spark Compatibility     | 2.5.3                            |
| Spark NLP Compatibility | 2.4                              |
| License                 | Licensed                         |
| Edition                 | Healthcare                       |
| Input Labels            | sentence, token, word_embeddings |
| Output Labels           | ner                              |
| Language                | es                               |
| Upstream Dependencies   | embeddings_scielowiki_300d       |




{:.h2_title}
## Data Source
Trained on CodiEsp Challenge dataset trained with `embeddings_scielowiki_300d`

