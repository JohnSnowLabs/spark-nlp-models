---
layout: model
title: 
author: John Snow Labs
name: sent_biobert_clinical_base_cased
class: 
language: en
repository: public/models
date: 19/09/2020
tags: [embeddings]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/><button class="button button-orange" disabled>Open in Colab</button><br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sent_biobert_clinical_base_cased_en_2.6.0_2.4_1600533460155.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = BertSentenceEmbeddings.pretrained("sent_biobert_clinical_base_cased","en","public/models")\
	.setInputCols("document")\
	.setOutputCol("bert_sentence_embeddings")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|----------------------------------|
| Model Name              | sent_biobert_clinical_base_cased |
| Model Class             | BertSentenceEmbeddings           |
| Spark Compatibility     | 2.6.0                            |
| Spark NLP Compatibility | 2.4                              |
| License                 | open source                      |
| Edition                 | public                           |
| Input Labels            | document                         |
| Output Labels           | bert_sentence_embeddings         |
| Language                | en                               |




{:.h2_title}
## Data Source


