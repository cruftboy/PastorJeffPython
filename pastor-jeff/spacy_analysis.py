import spacy
nlp = spacy.load('en_core_web_sm')

def info(doc):
	"""Main information processing method"""
	info = {}
	info['sentences'] = [str(sent) for sent in doc.sents]
	#sentences : [sent1, sent2, ...]
	info['tokens'] = [str(token) for token in doc]
	#all tokens in info['tokens']
	token_vals = {}
	for token in info['tokens']:
		current_word = token
		i = 0
		current_sent = info['sentences'][i]
		for i in range(len(info['sentences'])): #for each sentence
			val = current_sent.count(str(current_word))
			#value is the number of times the current word is in the current sent
			token_vals[str(token)] = val
			#append to dictionary
	info['token_vals'] = token_vals
	#given a word and a sentence, val is how many times it appears in that sentence
	return info