################################################################
##	Ryan McArdle
## 24 Sept.  2020
##
## Creates and compares two kinds of classifiers for identifying
## the author of provided text.  Can also test a number of
## different preprocessing methods to find the best method for
## the data set.
################################################################

import nltk
import string
import os
import re
import pathlib
import sklearn.naive_bayes as nb
from sklearn.feature_extraction.text import CountVectorizer
import itertools


class author_classifier_preprocess:
	"""Class defined for the purpose of reading a selection of
	Project Gutenberg and Internet Archive texts and processing
	the works for text classification models found in the 
	author_classifier() class below."""

	def __init__(self):

		self.tagged_works = [] # List of tuples (work,author) for the corpus
		self.tagged_sequences = [] # List of tuples (sequence,author) for the training set
		self.corpus = [] # List of text of works
		self.tagged_test = [] # List of tuples (work,author) for the test set
		return


	def preprocess(self,text_dir,test_titles_file, clean=False, removables=[string.whitespace,string.punctuation], stopwords=nltk.corpus.stopwords.words('english'), stem_type=(False,False)):
		"""Processes the texts from their raw format into 
		tokens. Will clean up the text using the provided 
		arguments. Finally, fits a count vectorizer to the 
		corpus of words."""

		self.clean = clean
		self.removables = removables
		self.stopwords = stopwords
		self.stem_type = stem_type
		test_titles = self.get_test_titles(test_titles_file) 
		print("Building corpus...")
		corpus = self.build_corpus(text_dir,test_titles)
		print("Fitting to corpus...")
		self.vectorizer = self.fit_vectorizer(corpus)


	def tag(self):
		"""Takes the works tagged in the preprocessing method
		and gets sequences of 500 words from each text, tagging
		these sequences with the same author and transforming
		the sequences using the vectorizer."""

		print("Tagging sequences...")
		sequences = self.get_tagged_sequences(self.tagged_works)
		print("Transforming sequences...")
		training_sequences = [' '.join(seq) for (seq,auth) in sequences] ## Turns the sequence from a list of words to a single string
		self.training_sequences = self.vectorizer.transform(training_sequences)
		self.training_authors = [auth for (seq,auth) in sequences]


	def process_testing(self):
		"""Analagous to the tag() method. Prepares the test 
		works by creating sequences, tagging, and 
		transforming."""

		test_data = self.get_tagged_sequences(self.tagged_test)
		test_sequences = [' '.join(seq) for (seq,auth) in test_data]
		self.test_sequences = self.vectorizer.transform(test_sequences)
		self.test_authors = [auth for (seq,auth) in test_data]


	def get_test_titles(self,testing_file):
		"""Reads in the titles in the provided file and
		recognizes them as the test works."""

		titles = []
		print('Getting test files...')
		with open(testing_file, encoding='utf-8') as f:
			text = f.readlines()
		text = [title.strip() for title in text]
		print(text)
		for title in text:
			titles.append(title)
		return titles


	def build_corpus(self,text_dir,testing_titles):
		"""Builds a corpus of texts, excluding works listed in 
		testing_titles."""

		for file in os.listdir(text_dir):
			#print(str(file))
			file_loc = os.path.join(text_dir,file)
			if str(file) not in testing_titles:
				#print(f'Training Title: {file}')
				self.add_to_corpus(file_loc)
			else:
				print(f'Testing Title: {file}')
				self.add_to_test_data(file_loc)
		return self.corpus


	#def get_testing_data(self,testing_titles):
	#	"""Adds the texts identified as test works to the
	#	testing data."""

	#	for file in os.listdir(text_dir):
	#		file_loc = os.path.join(text_dir,file)
	#		if file in testing_titles:
	#			print(f'Testing Title: {file}')
	#			self.add_to_test_data(file_loc)


	def add_to_test_data(self,title):
		"""Reads the work with the given title and adds it to 
		the testing data."""

		text = self.read_file(title,training=False)


	def add_to_corpus(self,title):
		"""Reads in the provided work, tokenizes and cleans the
	    text, and adds the work to the corpus."""

		text = self.read_file(title)
		cleaned_text = ' '.join(self.tokenize_text(text))
		self.corpus.append(cleaned_text)


	def read_file(self,file,training=True):
		""" Reads in the provided text file. Adds the work to 
		list of tagged works for either the training set or
	    the testing set."""

		with open(file, encoding='utf-8') as f:
			text = f.read()
		if training == True:
			self.tagged_works.append((text,self.get_author(file)))
		else:
			self.tagged_test.append((text,self.get_author(file)))
		return text


	def fit_vectorizer(self,corpus,vectorizer=CountVectorizer()):
		""" Fits the vecotrizer on the corpus of words."""

		vectorizer.fit(corpus)
		return vectorizer


	def get_author(self,file):
		"""Returns the author of a given text file."""

		file_name = os.path.basename(file)
		file_name_regex = re.compile(r'(.*)(-)(.*)(-)(.*)(.txt)')
		file_searched = file_name_regex.search(file_name)
		author_last = file_searched.group(1)
		author_first = file_searched.group(3)
		author = author_first + ' ' + author_last
		title = file_searched.group(5)
		return author


	def tokenize_text(self, target):
		""" Tokenizes the provided target text. If 
		clean == True, then remove undesired characters,
		remove stopwords, and stem or lemmatize words. """

		text = target.lower()
		tokens = nltk.word_tokenize(text)
		if self.clean == True:
			remove = ''.join(self.removables)
			tab = "".maketrans("","",remove)
			tokens = [token.translate(tab) for token in tokens]
			if self.stem_type[0] == True:
				if self.stem_type[1] == False:
					stemmer = nltk.stem.PorterStemmer()
					tokens = [stemmer.stem(token) for token in tokens if token not in self.stopwords]
				else:
					lemmer = nltk.stem.WordNetLemmatizer()
					tokens = [lemmer.lemmatize(token) for token in tokens if token not in self.stopwords]
			else:
				tokens = [token for token in tokens if token not in self.stopwords]
		self.current_tokenized = tokens
		return tokens


	def get_tagged_sequences(self, target, sequence_length=500):
		""" Takes the tagged works and returns tagged sequences
		of 500 tokens for training/classification. """

		for (work,author) in target:
			tokens = nltk.word_tokenize(work)
			sequences = [tokens[i:i + sequence_length] for i in range(0,len(tokens),sequence_length) if len(tokens[i:i + sequence_length]) == sequence_length]
			self.tagged_sequences.extend([(sequence, author) for sequence in sequences])
		return self.tagged_sequences



class author_classifier:
	"""A class definied for classifying texts provided by the 
	author_classifier_preprocess() class above. Currently
	defined with options for Multinomial and Bernoulli Naive
	Bayes classifiers."""
	
	def __init__(self,training_x,training_y):
		"""Initializes the classifier class with training data
		provided by the preprocess class."""

		self.training_x = training_x
		self.training_y = training_y
		return

	def multinomial(self,testing_x,testing_y):
		"""Trains a Multinomial Naive Bayes model."""

		learner = nb.MultinomialNB()
		print("Fitting classifier...")
		learner.fit(self.training_x,self.training_y)

		print("Predicting...")
		predictions = learner.predict(testing_x)
		score = learner.score(testing_x,testing_y)

		print(f"Multinomial NB Score: {score}\n")
		return score

	def bernoulli(self,testing_x,testing_y):
		"""Trains a Bernoulli Naive Bayes model."""

		learner = nb.BernoulliNB()
		print("Fitting classifier...")
		learner.fit(self.training_x,self.training_y)

		print("Predicting...")
		predictions = learner.predict(testing_x)
		score = learner.score(testing_x,testing_y)

		print(f"Bernoulli NB Score: {score}\n")
		return score



def main():
	"""Runs the classification process using the best found
    model."""

	acp = author_classifier_preprocess()
	text_dir = pathlib.Path("./text/")
	testing_titles_file = pathlib.Path("./testing_works.txt")

	acp.preprocess(str(text_dir),testing_titles_file,clean=True,removables=['0123456789'], stopwords=[], stem_type=(True,True))
	acp.tag()

	auth_clf = author_classifier(acp.training_sequences,acp.training_authors)

	acp.process_testing()

	auth_clf.bernoulli(acp.test_sequences,acp.test_authors)


def find_best_model():
	"""Runs multiple iterations of the classification process,
	recording performance of each model and recommending the 
	best model found."""

	text_dir = pathlib.Path("./text/")
	testing_titles_file = pathlib.Path("./testing_works.txt")

	best_acc = 0.0

	clean = [True] ## True will implement cleaning process
	removables = powerset([string.whitespace, string.punctuation, '0123456789'])
	stops = powerset([nltk.corpus.stopwords.words('english')])
	stem = [(False,False),(True,False),(True,True)] ## (edit,type) - if edit == true, implement a type.  if type == false, then stem, else lemmatize

	combinations = list(itertools.product(clean,removables,stops,stem))
	combinations.append([False,None,None,None,None]) ## Includes the model for which no cleaning is done.
	

	record = [] ## List containing tuples of method and score
	
	## Loops through the provided combinations of cleaning
	## arguments, running the models for each kind.
	for combo in combinations:
		print("Combo:")
		print(combo)

		acp = author_classifier_preprocess()
		acp.preprocess(text_dir,testing_titles_file,combo[0],combo[1],combo[2],combo[3])
		acp.tag()

		auth_clf = author_classifier(acp.training_sequences,acp.training_authors)

		acp.process_testing()

		multi = auth_clf.multinomial(acp.test_sequences,acp.test_authors)
		bern = auth_clf.bernoulli(acp.test_sequences,acp.test_authors)

		record.append((combo,multi,bern))

		if (multi > bern) and (multi > best_acc):
			best_acc = multi
			best_model = ['multi',combo]
		elif (bern > multi) and (bern > best_acc):
			best_acc = bern
			best_model = ['bern',combo]

	print(f"Best Model: {best_model}")

	## Saves a record of the tested models and their accuracies. 
	with open('record.txt', 'w') as f:
		f.write(f"Best Model: {best_model}\n\n")
		for item in record:
			f.write(f"{item}\n")


def powerset(iterable):
	"""A recipe take from the itertools page for returning the 
	powerset of the provided iterable. Used to try each 
	possible combination of arguments provided in the
	find_best_model() function."""
	
	s = list(iterable)
	return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))
	

if __name__ == "__main__":
	main()
	#find_best_model()