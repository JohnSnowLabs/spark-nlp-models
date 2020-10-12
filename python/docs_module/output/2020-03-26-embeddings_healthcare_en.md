---
layout: model
title: Embeddings Healthcare
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-03-26
tags: [clinical,embeddings,en]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
Word2Vec feature vectors based on embeddings_healthcare 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/embeddings_healthcare_en_2.4.4_2.4_1585188313964.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|-----------------------|
| Model Name              | embeddings_healthcare |
| Model Class             | WordEmbeddingsModel   |
| Spark Compatibility     | 2.4.4                 |
| Spark NLP Compatibility | 2.4                   |
| License                 | Licensed              |
| Edition                 | Official              |
| Input Labels            | document, token       |
| Output Labels           | word_embeddings       |
| Language                | en                    |
| Dimension               | 400.0                 |





{:.h2_title}
## Data Source
Trained on PubMed + ICD10 + UMLS + MIMIC III corpora.

