import spacy
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np

nlp = spacy.load('en_core_web_sm')

#appends mean sentences to one data table
def build_model(df):
	"""Create a table given a list of phrases"""
	data = []
	for index, row in df.iterrows():
		sent = row[0]
		is_mean = row[1]
		nsent = nlp(sent)
		tokens = [token.lower_ for token in nsent if token.pos_ != 'PUNCT' and len(token.lower_)>1 and token.lower_[0]!="'"]
 		#generate tokens
		token_counts = pd.Series(tokens).value_counts()
		#find values for tokens
		d = token_counts.to_dict()
		d['is_mean'] = is_mean
		data.append(d)
		#append a dict of tokens and token values to data
	df = pd.DataFrame.from_dict(data).fillna(0.0)
	#create a dataframe with all the data
	return df

def train(df):
	"""Train the neural network given a dataframe (df)"""
	df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
	#add is_train column, 25% of the data should be training
	train, test = df[df['is_train']==True], df[df['is_train']==False]
	#create training set and test set
	features = set(df.columns) - set(['is_mean'])
	print (features)
	y = train['is_mean']
	clf = RandomForestClassifier(n_jobs=2, random_state=0)
	#init random forest
	clf.fit(train[features], y)
	#train random forest on token vals
	pred = clf.predict(test[features])
	print(test['is_mean'])
	print(pred)
	xx = pred - test['is_mean']
	num_right = sum([1 for z in xx if z==0])
	accuracy = num_right / len(pred)
	print("Accuracy: ", accuracy, "%")
	return accuracy
	
csv_df = pd.read_csv('nice_mean_v2.csv',header=None)
#phrases = [(u"You suck!",1), (u"I hope you die die die die die.",1), (u"Shut up nerd.",1), (u"how are you doing", 0)]
df = build_model(csv_df)


print (df.to_string())
print (df.shape)
train(df)
average_acc = []
for i in range(100):
	average_acc.append(train(df))
count = 0
for percent in average_acc:
	count += percent
average_accuracy = count / len(average_acc)
print (average_accuracy)
