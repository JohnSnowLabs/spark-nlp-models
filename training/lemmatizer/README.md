# Lemmatizer

How to train Spark NLP `Lemmatizer` annotator:

```scala
val lemmatizer = new Lemmatizer()
    .setInputCols(Array("token"))
    .setOutputCol("lemma")
    .setDictionary("AntBNC_lemmas_ver_001.txt", "->", "\t")
```

The file must have the following format where the `keyDelimiter` in this case is `->` and the `valueDelimiter` is `\t`:

```bash
abnormal    ->  abnormal    abnormals
abode   ->	abode	abodes
abolish ->	abolishing	abolished	abolish	abolishes
abolitionist	->	abolitionist	abolitionists
abominate	->	abominate	abominated	abominates
abomination	->	abomination	abominations
aboriginal	->	aboriginal	aboriginals
aborigine	->	aborigines	aborigine
abort	->	aborted	abort	aborts	aborting
abortifacient	->	abortifacients	abortifacient
abortionist	->	abortionist	abortionists
abortion	->	abortion	abortions
abo	->	abo	abos
abotrite	->	abotrites	abotrite
abound	->	abound	abounds	abounding	abounded
```

> NOTE: For now, the `Lemmatizer` uses path to a file instead of a DataFrame. So any DataFrame iside `.fit()` will be ignored for this annotator.
