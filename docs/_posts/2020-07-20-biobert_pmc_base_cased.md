---
title: BioBERT PMC
author: John Snow Labs
name: biobert_pmc_base_cased
date: 2020-07-20
tags: [embeddings, en, bert]
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description
This model contains a pre-trained weights of BioBERT, a language representation model for biomedical domain, especially designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering, etc. The details are described in the paper "[BioBERT: a pre-trained biomedical language representation model for biomedical text mining](https://arxiv.org/abs/1901.08746)".

{:.btn-box}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/biobert_pmc_base_cased_en_2.5.0_2.4_1590489029151.zip){:.button.button-orange.button-orange-trans.arr.button-icon}

## How to use

{% include programmingLanguageSelectScalaPython.html %}

```python

embeddings = BertEmbeddings.pretrained("biobert_pmc_base_cased", "en") \
      .setInputCols("sentence", "token") \
      .setOutputCol("embeddings")
```

```scala

val embeddings = BertEmbeddings.pretrained("biobert_pmc_base_cased", "en")
      .setInputCols("sentence", "token")
      .setOutputCol("embeddings")
```

{:.model-param}
## Model Parameters

{:.table-model}
|---|---|
|Model Name:|biobert_pmc_base_cased|
|Type:|embeddings|
|Compatibility:|Spark NLP 2.5.0|
|License:|Open Source|
|Edition:|Official|
|Spark inputs:|[sentence, token]|
|Spark outputs:|[word_embeddings]|
|Language:|[en]|
|Dimension:|768|
|Case sensitive:|true|


{:.h2_title}
## Source
The model is imported from [https://github.com/dmis-lab/biobert](https://github.com/dmis-lab/biobert)
