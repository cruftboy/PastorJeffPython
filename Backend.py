import spacy
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
from sklearn import feature_extraction


nlp = spacy.load('en_core_web_sm')

#appends mean sentences to one data table
def build_training_set(in_df):
	"""Create a table given a list of phrases"""
	data = []
	for index, row in in_df.iterrows():
		sent = row[0]
		is_mean = row[1]
		nsent = nlp(sent)
		lemmas = [lemma.lower_ for lemma in nsent if lemma.pos_ != 'PUNCT' and  ("'" not in lemma.lower_) and len(lemma.lower_)>1 and lemma.lower_[0]!="'"]
 		#generate lemma
		token_counts = pd.Series(lemmas).value_counts()
		#find values for lemma
		d = token_counts.to_dict()
		d['is_mean'] = is_mean
		data.append(d)
		#append a dict of tokens and token values to data
	out1 = pd.DataFrame.from_dict(data).fillna(0.0)
	features = [c for c in out1.columns if c is not 'is_mean']	
	out2 = feature_extraction.text.TfidfTransformer().fit_transform(out1[features])
	out_df_tdidf = pd.SparseDataFrame(out2, columns=features).to_dense().fillna(0.0).to_dense().assign(is_mean=out1['is_mean'])

	#create a dataframe with all the data
	return out_df_tdidf

def build_model(train_df):
	#take training set
	features = [c for c in train_df.columns if c is not 'is_mean']
	y = train_df['is_mean']
	clf = RandomForestClassifier(n_jobs=2, random_state=0, n_estimators=500)
	#init random forest
	model = clf.fit(train_df[features], y)
	model_lemmas = features
	return model, model_lemmas

def eval_model(in_df):
	#take training set
	train_df, test_df = model_selection.train_test_split(in_df, random_state=1, test_size=0.25)
	features = [c for c in train_df.columns if c is not 'is_mean']
	y_train = train_df['is_mean']
	clf = RandomForestClassifier(n_jobs=2, random_state=0, n_estimators=1000)
	#init random forest
	model = clf.fit(train_df[features], y_train)

	pred = model.predict(test_df[features])
	y_test = test_df['is_mean']
	accuracy = sklearn.metrics.accuracy_score(y_test, pred)
	return accuracy


def predict(model, model_lemmas, input_str):
	nsent = nlp(input_str)
	lemmas = [lemma.lower_ for lemma in nsent if lemma.pos_ != 'PUNCT' and len(lemma.lower_)>1 and ("'" not in lemma.lower_) and lemma.lower_ in model_lemmas]
	lemma_counts = pd.Series(lemmas).value_counts()
	d = lemma_counts.to_dict()
	for t in model_lemmas:
		if t not in d:
			d[t] = 0
#	print (d)
	df = pd.DataFrame.from_dict([d]).fillna(0.0)
#	print (df.columns)
	return model.predict(df)

csv_training_df = pd.read_csv('nice_mean_v4.csv',header=None)
df = build_training_set(csv_training_df)
print (df.head(10))

accuracy = eval_model(df)
print(accuracy)

model, model_lemmas = build_model(df)


