---
layout: article
key: page-about
---

# Frequently Asked Questions
* [What type of models can the user upload?](#q1) 
* [Are there any naming conventions?](#q2)
* [Where are the models stored?](#q2)

___


# <a id="q1">What type of models can  a user upload</a>
This model hub is currently focussed on Spark NLP pretrained models and pipelines. 

# <a id="q3">Where are the models stored</a>
The models are stored on AWS on the following public s3 bucket: <https://s3.amazonaws.com/community.johnsnowlabs.com/>.
Any models hub user can download and use the published models via the **nlu** library or directly using the pretrained call on a Spark NLP Model.

**Python Example**:
```python 
# load NER model trained by deep learning approach and GloVe word embeddings
ner_dl = NerDLModel.pretrained('ner_dl')
# load NER model trained by deep learning approach and BERT word embeddings
ner_bert = NerDLModel.pretrained('ner_dl_bert')  
```
 
# <a id="q2">How to name your model</a>
You can name your models as you wish. When you upload the model archive, it will be automatically unzipped for reading the metadata file and then published to the community s3 bucket under a new name which will be build as follows:
model_name + spark_nlp_version + apache_spark_version + timestamp.zip