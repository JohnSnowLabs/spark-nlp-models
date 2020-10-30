---
layout: model
title: ChunkResolver SNOMED Findings Clinical
author: John Snow Labs
name: chunkresolve_snomed_findings_clinical
class: 
language: en
repository: clinical/models
date: 20/06/2020
tags: [clinical,entity_resolver,snomed]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 


 {:.h2_title}
## Predicted Entities
Snomed Codes and their normalized definition with `clinical_embeddings` 

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_SNOMED/){:.button.button-orange}<br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/13.Snomed_Entity_Resolver_Model_Training.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_snomed_findings_clinical_en_2.5.1_2.4_1592617161564.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python
model = ChunkEntityResolverModel.pretrained("chunkresolve_snomed_findings_clinical","en","clinical/models")\
	.setInputCols("token","chunk_embeddings")\
	.setOutputCol("entity")
```

```scala

```
</div>



{:.model-param}
## Model Information

{:.table-model}
|-------------------------|---------------------------------------|
| Model Name              | chunkresolve_snomed_findings_clinical |
| Model Class             | ChunkEntityResolverModel              |
| Spark Compatibility     | 2.5.1                                 |
| Spark NLP Compatibility | 2.4                                   |
| License                 | Licensed                              |
| Edition                 | Healthcare                            |
| Input Labels            | token, chunk_embeddings               |
| Output Labels           | entity                                |
| Language                | en                                    |
| Case Sensitive          | 1.0                                   |
| Upstream Dependencies   | embeddings_clinical                   |




{:.h2_title}
## Data Source
Trained on SNOMED CT Findings

