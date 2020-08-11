---
title: Sentiment classifier
author: John Snow Labs
name: sentiment_dl
date: 2020-07-21 11:33:00 +0800
tags: [sentiment]
article_header:
  type: cover
---


## Description
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


<div class="grid" style="align-content: center;">
  <div class="cell cell--8 cell--md-3 cell--lg-4 content" style="align-content: center;">
    <a href="https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/NER_EN.ipynb">
      <img src="https://assets.website-files.com/5dc3b47ddc6c0c2a1af74ad0/5e18182886ccdc638908b3a0_RGB_Logomark_Color_Dark_Bg.png" alt="Live demo" style="width: 70px">Live Demo</a>
  </div>
  <div class="cell cell--8 cell--lg-3 content" style="align-content: center;">
  <a href="https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/NER_EN.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="width: 170px;"></a>
</div>

  <div class="cell cell--8 cell--md-4 cell--lg-4 content" style="align-content: center;">
    <a href="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sentimentdl_glove_imdb_en_2.5.0_2.4_1588682682507.zip">
      <img src="https://icons.iconarchive.com/icons/dtafalonso/android-lollipop/512/Downloads-icon.png" alt="Download" style="width: 40px">Download</a>
  </div>
</div>


## How to use (we should create one tab for each language)
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


## Dataset used for training
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Evaluation results
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
