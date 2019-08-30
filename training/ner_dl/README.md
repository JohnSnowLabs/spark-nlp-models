# NerDLApproach

To train Named Entity Recognition (NER) model by Spark NLP we use `NerDLApproach` annotator.

## Data prepration

To prepare our training dataset and test dataset (optional), we use a class called `CoNLL()` to transform our CoNLL files (IOB and IOB2).

Here is an example for CoNLL 2003 `eng.train`:

```scala
import com.johnsnowlabs.nlp.training._
import com.johnsnowlabs.nlp.annotator._
import com.johnsnowlabs.nlp.base._

val conll = CoNLL()
val training_data = conll.readDataset(spark, "/conll2003/eng.train")

training_data.show(2)

+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+
|                text|            document|            sentence|               token|                 pos|               label|
+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+
|EU rejects German...|[[document, 0, 27...|[[document, 0, 47...|[[token, 0, 1, EU...|[[pos, 0, 1, NNP,...|[[named_entity, 0...|
|Rare Hendrix song...|[[document, 0, 96...|[[document, 0, 50...|[[token, 0, 3, Ra...|[[pos, 0, 3, NNP,...|[[named_entity, 0...|
+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+
```

Now that we have our training dataset with all the required columns, we can transform it by using `WordEmbeddingsModel` or `BertEmbeddings` to another DataFrame that has an extra column for word embeddings.

Her we use pre-trained WordEmbeddingsModel `GloVe 100d`:

```Scala
val embeddings = WordEmbeddingsModel.pretrained()
.setInputCols("sentence", "token")
.setOutputCol("embeddings")
.setCaseSensitive(false)

val readyTrainingData = embeddings.transform(training_data)


// Optional: You can save the result on disk if the DataFrame is too large.

readyTrainingData.write.mode("Overwrite").parquet("/tmp/conll2003/GloVeCoNLL2003_6B_100_train")

```

Now we can start training our `NerDLModel`:

```scala

// In case you saved it on disk, let's read it back first
val readyTrainingData = spark.read.parquet("/tmp/conll2003/GloVeCoNLL2003_6B_100_train")

val ner = new NerDLApproach()
.setInputCols("sentence", "token", "embeddings")
.setOutputCol("ner")
.setLabelColumn("label")
.setOutputCol("ner")
.setLr(1e-3f) //0.001
.setPo(5e-3f) //0.005
.setDropout(5e-1f) //0.5
.setBatchSize(128)
.setMaxEpochs(50)
.setRandomSeed(0)
.setVerbose(0)
.setIncludeValidationProp(false) //remove the sample from training
.setTrainValidationProp(0.1f)
.setEvaluationLogExtended(true)

val myNerModel = ner.fit(readyTrainingData)

myNerModel.write.save("/tmp/NerDLModel_conll2003")

```

You can later on use your `NerDLModel` inside any pipeline by simply loading it:

```scala

val ner = NerDLModel.load("/tmp/NerDLModel_conll2003")

```
