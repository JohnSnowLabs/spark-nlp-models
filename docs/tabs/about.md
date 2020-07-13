---
title: FAQ

# FAQ page
# © 2020 Spark NLP Models Hub
# MIT License
---

# Frequently Asked Questions
* [What type of models can the user upload?](#q1) 
* [Are there any naming conventions?](#q2)
* [Where are the models stored?](#q2)


# <a id="q1">What type of models can  a user upload</a>
This model hub is currently focussed on Spark NLP pretrained models and pipelines. 

# <a id="q3">Where are the models stored</a>
The models are stored on AWS on the following public s3 bucket: <https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/>.
They will be published as open source. Any other models hub user can download and used them.  

 
# <a id="q2">How to name your model</a>
The name of a pretrained model/pipeline is formed by several elements separated by "." (dot). 
The **first** element of a model name should be the language. This can be either:
*	The ISO 629-1 two-letter langauge code (en, fr, de, ...)
*	'mu' for 'multi-lingual'
*	? for 'please detect the language first, and then use the models for that language'

The **second** element should picture the type of model and should be one of: **ner**, **embed**, **clean**, **spell**, **resolve**, **sentiment**

The third element represents the type  of model, and can be one of: **dl**, **ml** for models or **glove**, **bert** for embeddings. 
The forth element represents the size of the model - one of **large**, **med**, **small**. 
Examples:
* nl.explain.dl.large
* nl.explain.dl.med
* nl.explain.dl.small
* nl.ner.dl.large 
* nl.ner.dl.med
* nl.ner.dl.small
* en.explain.ml
* en.explain.dl
* en.ner.dl.small.glove.onto
* en.ner.dl.med.bert.onto
* en.ner.dl.small.glove
* en.ner.onto.large
* en.match.datetime
* en.match.pattern
* en.match.chunks
* en.match.phrases
* en.clean.stopwords
* en.clean.pattern
* en.clean.slang
* en.spell.ml
* en.spell.dl
* en.emotion.sentiment
* en.emotion.sentiment.imdb
* en.emotion.sentiment.twitter
* en.dependency
