---
title: NerDLModel Clinical Large
author: John Snow Labs
name: ner_clinical_large_en
date: 2020-05-23
tags: [ner, en, ner_clinical_large]
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms. The SparkNLP deep learning model (NerDL) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN. 

{:.h2_title}
## Included Entities  
Problem, Test, Treatment


{:.btn-box}
[Live Demo](){:.button.button-orange}
[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_large_en_2.5.0_2.4_1590021302624.zip){:.button.button-orange.button-orange-trans.arr.button-icon}


## How to use

Use as part of an nlp pipeline with the following stages: DocumentAssembler, SentenceDetector, Tokenizer, WordEmbeddingsModel, NerDLModel. Add the NerConverter to the end of the pipeline to convert entity tokens into full entity chunks.

{% include programmingLanguageSelectScalaPython.html %}


```python

clinical_ner = NerDLModel.pretrained("ner_clinical_large", "en", "clinical/models") \
  .setInputCols(["sentence", "token", "embeddings"]) \
  .setOutputCol("ner")

nlpPipeline = Pipeline(stages=[clinical_ner])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

results = model.transform(data)

```

```scala
val ner = NerDLModel.pretrained("ner_clinical_large", "en", "clinical/models") \
  .setInputCols(["sentence", "token", "embeddings"]) \
  .setOutputCol("ner")

val pipeline = new Pipeline().setStages(Array(ner))

val result = pipeline.fit(Seq.empty[String].toDS.toDF("text")).transform(data)

```
{:.model-param}
## Model Parameters

{:.table-model}
|---|---|
|Model Name:|ner_clinical_large_en_2.5.0_2.4|
|Type:|ner|
|Compatibility:|Spark NLP 2.5.0|
|Edition:|Healthcare|
|License:|Licenced|
|Spark inputs:|[sentence, token, embeddings]|
|Spark outputs:|[ner]|
|Language:|[en]|
|Case sensitive:|false|

{:.h2_title}
## Dataset used for training
Trained on augmented 2010 i2b2 challenge data with 'embeddings_clinical'.
https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/

{:.h2_title}
## Results
The output is a dataframe with a sentence per row and a "ner" column containing all of the entity labels in the sentence, entity character indices, and other metadata. To get only the tokens and entity labels, without the metadata, select "token.result" and "ner.result" from your output dataframe:

![image](\assets\images\ner_clinical.png)