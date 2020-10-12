---
layout: model
title: ChunkResolver Snomed Findings Clinical
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-06-20
tags: [clinical,entity_resolution,snomed,en]
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
| Edition                 | Official                              |
| Input Labels            | token, chunk_embeddings               |
| Output Labels           | entity                                |
| Language                | en                                    |
| Case Sensitive          | True                                  |
| Upstream Dependencies   | embeddings_clinical                   |





{:.h2_title}
## Data Source
Trained on SNOMED CT Findings.

