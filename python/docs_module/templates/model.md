---
layout: model
title: {{title}}
author: {{author}}
name: {{name}}
class: {{model_class}}
language: {{language}}
repository: {{repo}}
date: {{latest_date}}
tags: [{{tags}}]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description
{{class_description}}  
{{description}}
{% if labels %}
{:.h2_title}
## Prediction Domain
{{labels}}
{% endif %}
{% if reference_url %}[{{reference_url}}]({{reference_url}}){% endif %}
{% if included_models %}
{:.h2_title}
## Included Models
{{included_models}}
{% else %}
{:.h2_title}
## Data Source
{{dataset_info}}
{% endif %}
{{buttons}}
{:.h2_title}
## How to use 
<div class="tabs-box" markdown="1">
{% raw %}
{% include programmingLanguageSelectScalaPython.html %}
{% endraw %}
```python
{{python_sample}}
```

```scala
{{scala_sample}}
```
</div>

{#
{:.h2_title}
## Results
{{class_annotation_sample}}

{:.result_box}
```python
{{model_output_schema}}
```
#}

{:.model-param}
## Model Information

{:.table-model}
{{table}}

{#
{:.h2_title}
## Benchmarking 
{{model_benchmarks}}
#}
