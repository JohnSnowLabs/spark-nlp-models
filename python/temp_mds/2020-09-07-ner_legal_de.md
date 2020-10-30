---
layout: model
title: NER DL Model Legal
author: John Snow Labs
name: ner_legal
class: 
language: de
repository: clinical/models
date: 07/09/2020
tags: [clinical,ner]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
AN,EUN,GRT,GS,INN,LD,LDS,LIT,MRK,ORG,PER,RR,RS,ST,STR,UN,VO,VS,VT 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_LEGAL_DE/){:.button.button-orange}<br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/15.German_Legal_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_legal_de_2.5.5_2.4_1599471454959.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = NerDLModel.pretrained("ner_legal","de","clinical/models")\
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
| Model Name              | ner_legal                        |
| Model Class             | NerDLModel                       |
| Spark Compatibility     | 2.5.5                            |
| Spark NLP Compatibility | 2.4                              |
| License                 | Licensed                         |
| Edition                 | Legal                            |
| Input Labels            | sentence, token, word_embeddings |
| Output Labels           | ner                              |
| Language                | de                               |
| Upstream Dependencies   | embeddings_clinical              |




{:.h2_title}
## Data Source


