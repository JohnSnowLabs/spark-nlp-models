---
layout: model
title: Ner DL Model Enriched
author: John Snow Labs
name: 
class: 
language: 
repository: clinical/models
date: 2020-04-21
tags: [clinical,ner,generic,en]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Pretrained named entity recognition deep learning model for clinical terminology.

 {:.h2_title}
## Predicted Entities
Age,Allergenic_substance,Blood_Pressure,Causative_Agents_(Virus_and_Bacteria),Diagnosis,Dosage,Drug_Name,Frequency,Gender,Lab_Name,Lab_Result,Maybe,Modifier,Name,Negation,O2_Saturation,Procedure,Procedure_Name,Pulse_Rate,Respiratory_Rate,Route,Section_Name,Substance_Name,Symptom_Name,Temperature,Weight 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_jsl_enriched_en_2.4.2_2.4_1587513303751.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

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
|-------------------------|----------------------------------|
| Model Name              | ner_jsl_enriched                 |
| Model Class             | NerDLModel                       |
| Spark Compatibility     | 2.4.2                            |
| Spark NLP Compatibility | 2.4                              |
| License                 | Licensed                         |
| Edition                 | Official                         |
| Input Labels            | sentence, token, word_embeddings |
| Output Labels           | ner                              |
| Language                | en                               |
| Case Sensitive          | False                            |
| Upstream Dependencies   | embeddings_clinical              |





{:.h2_title}
## Data Source
Trained on data gathered and manually annotated by John Snow Labs.

