import spacy_analysis as sp
import spacy
import pandas as pd
nlp = spacy.load('en_core_web_sm')
mean_phrases = pd.DataFrame()
nice_phrases = pd.DataFrame()

def process_sent(sentence):
	"""Process a single sentence"""
	d = (sp.info(sentence))
	data = pd.DataFrame(d['token_vals'],index=d['sentences'])
	return data
#process an individual sentence
def create_table(sentences):
	"""Create a table given a list of sentences"""
	for i in range(len(sentences)):
		print(process_sent(sentences[i]))
		mean_phrases.append(process_sent(sentences[i]))
#appends mean sentences to one data table

mean_stuff = [nlp(u"You suck!"), nlp(u"I hope you die."), nlp(u"Shut up nerd.")]
create_table(mean_stuff)