---
title: Explain Document Small Dutch
author: John Snow Labs
name: explain_document_sm
date: 2020-07-06 11:33:00 +0800
categories: [Open Source, Pipelines]
tags: [dutch]
---

#### Model name: *explain_document_sm*
#### Type: *pipeline*
#### Size: *164Mb* 
#### Compatibility: *Spark NLP 2.5.0*
#### License: *Open Source*
#### Inputs: *[document, sentence, token]*
#### Outputs: *[embeddings]*
#### Languages: *[nl]*

## Description
ToDo 
#### Documentation
Relevant documentation (SEO purpose)
#### References
Relevant related work (SEO purpose)
#### Citations 
Relevant citations (SEO purpose)

## Usage example

```python
# Download a pre-trained pipeline
pipeline = PretrainedPipeline('explain_document_dl', lang='nl')

# Your testing dataset
text = """
The Mona Lisa is a 16th century oil painting created by Leonardo. 
It's held at the Louvre in Paris.
"""

# Annotate your testing dataset
result = pipeline.annotate(text)

# What's in the pipeline
list(result.keys())
Output: ['entities', 'stem', 'checked', 'lemma', 'document',
'pos', 'token', 'ner', 'embeddings', 'sentence']

# Check the results
result['entities']
Output: ['Mona Lisa', 'Leonardo', 'Louvre', 'Paris']
```
## Run complete example in colab 
Not available.
## See it in action
Not available. 

## Dataset used for training 
ToDo


## Dependencies (components) 
None 


## Evaluation results

ToDo

## Download address
<https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/explain_document_sm_nl_2.5.0_2.4_1588546621618.zip>

