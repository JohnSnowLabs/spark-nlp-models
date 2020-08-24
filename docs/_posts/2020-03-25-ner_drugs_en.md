---
title: NerDLModel Drugs
author: John Snow Labs
name: ner_drugs_en
date: 2020-03-25
tags: [ner, en, ner_drugs]
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for Drugs. Includes 'DrugChem' (Drug or Chemical) entity. The SparkNLP deep learning model (NerDL) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN. 

{:.btn-box}
[Live Demo](){:.button.button-orange}
[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_drugs_en_2.4.4_2.4_1584452534235.zip){:.button.button-orange.button-orange-trans.arr.button-icon}


## How to use

Use as part of an nlp pipeline with the following stages: DocumentAssembler, SentenceDetector, Tokenizer, WordEmbeddingsModel, NerDLModel. Add the NerConverter to the end of the pipeline to convert entity tokens into full entity chunks.

{% include programmingLanguageSelectScalaPython.html %}


```python

clinical_ner = NerDLModel.pretrained("ner_drugs", "en", "clinical/models") \
  .setInputCols(["sentence", "token", "embeddings"]) \
  .setOutputCol("ner")

nlpPipeline = Pipeline(stages=[clinical_ner])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

results = model.transform(data)

```

```scala

val ner = NerDLModel.pretrained("ner_drugs", "en", "clinical/models") \
  .setInputCols(["sentence", "token", "embeddings"]) \
  .setOutputCol("ner")

val pipeline = new Pipeline().setStages(Array(ner))

val result = pipeline.fit(Seq.empty[String].toDS.toDF("text")).transform(data)


```
{:.model-param}
## Model Parameters

{:.table-model}
|---|---|
|Model Name:|ner_drugs_en_2.4.4_2.4|
|Type:|ner|
|Compatibility:|Spark NLP 2.4.4|
|Edition:|Healthcare|
|License:|Enterprise|
|Spark inputs:|[sentence,token, embeddings]|
|Spark outputs:|[ner]|
|Language:|[en]|
|Case sensitive:|false|

{:.h2_title}
## Dataset used for training
Trained on i2b2_med7 + FDA with 'embeddings_clinical'.
https://www.i2b2.org/NLP/Medication

{:.h2_title}
## Results
The output is a dataframe with a sentence per row and a "ner" column containing all of the entity labels in the sentence, entity character indices, and other metadata. To get only the tokens and entity labels, without the metadata, select "token.result" and "ner.result" from your output dataframe or add the "Finisher" to the end of your pipeline.

![](ner_drugs.png) 