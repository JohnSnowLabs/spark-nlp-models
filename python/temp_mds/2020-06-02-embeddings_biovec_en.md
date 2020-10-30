---
layout: model
title: Embeddings BioVec
author: John Snow Labs
name: embeddings_biovec
class: 
language: en
repository: clinical/models
date: 02/06/2020
tags: [clinical,embeddings]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
Word2Vec feature vectors based on embeddings_biovec 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/embeddings_biovec_en_2.5.0_2.4_1591068211397.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = WordEmbeddingsModel.pretrained("embeddings_biovec","en","clinical/models")\
	.setInputCols("document","token")\
	.setOutputCol("word_embeddings")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|---------------------|
| Model Name              | embeddings_biovec   |
| Model Class             | WordEmbeddingsModel |
| Spark Compatibility     | 2.5.0               |
| Spark NLP Compatibility | 2.4                 |
| License                 | Licensed            |
| Edition                 | Healthcare          |
| Input Labels            | document, token     |
| Output Labels           | word_embeddings     |
| Language                | en                  |
| Dimension               | 300.0               |




{:.h2_title}
## Data Source
Trained on PubMed corpora

