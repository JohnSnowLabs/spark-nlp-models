---
title: Sentiment classifier  
author: John Snow Labs
name: sentiment_dl
date: 2020-07-21 11:33:00 +0800
categories: [Open Source, Model]
tags: [sentiment]
---

## Model name: *sentiment_dl*
## Type: *sentiment*
## Compatibility: *Spark NLP 2.4.4*
## License: *Open Source*
## Spark inputs: *[sentence_embeddings]*
## Spark outputs: *[sentiment]*
## Language: *[en]*
## Thesold: 0.6000000238418579
## Theshold label: neutral
## Embeddings: glove_100d

## Description
SentimentDLModel is a classification model trained by deep learning approach and using glove embeddings..
## How to use
```python

documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
    
use = UniversalSentenceEncoder.pretrained(name="tfhub_use", lang="en")\
 .setInputCols(["document"])\
 .setOutputCol("sentence_embeddings")


sentimentdl = SentimentDLModel.pretrained(name=MODEL_NAME, lang="en")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("sentiment")

nlpPipeline = Pipeline(
      stages = [
          documentAssembler,
          use,
          sentimentdl
      ])
```
## Run in colab

<p style="text-align:left"> 


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/SENTIMENT_EN.ipynb)


</p>


## Streamlit example
<https://demo.johnsnowlabs.com/public/SENTIMENT_EN/>

## Dataset used for training 
N/A

## Evaluation results
N/A

## Download address
<https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentimentdl_glove_imdb_en_2.5.0_2.4_1588682682507.zip>

