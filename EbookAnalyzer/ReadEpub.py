import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import re
from pattern.de import parse, split, parsetree, tag, Word
from germalemma import GermaLemma
import json


BookTitle = "Gustave Flaubert.epub"

def addWordToDict(word, tag, dictionary):
	if len(word) > 2:
		if word in dictionary:
			dictionary[word][1] += 1
		else:
			dictionary[word] = [tag, 1]

def open_obj(name):
	with open('obj/' + name + '.json', 'rb') as f:
		return json.load(f)

def save_obj(obj, name):
	toSave = json.dumps(obj)
	with open('obj/'+ name + '.json', 'w') as f:
		f.write(toSave)

def listBookContent(path):
	book = epub.read_epub(path)
	dictionaryHelper = {}
	dictionary = {}
	error = "generator raised StopIteration"
	lemmatizer = GermaLemma()

	for item in book.get_items():
		if item.get_type() == ebooklib.ITEM_DOCUMENT:
			#print('NAME : ', item.get_name())
			markup = item.get_content()
			soup = BeautifulSoup(markup, features="lxml")
			text = soup.get_text()
			# print(text[:100])
			while (error != "allfine"):
				try:
					error = "allfine"
					text = parse(text, tokenize=True, tags=True, chunks=False, lemmata=True).split()
					for sentence in text:
						for word in sentence:
							singleWord = word[0].lower().replace("„","")
							if word[1][0] == "N":
								addWordToDict(singleWord, "N", dictionaryHelper)
							elif word[1][0] == "J":
								addWordToDict(singleWord, "ADJ", dictionaryHelper)
							elif word[1][0] == "R":
								addWordToDict(singleWord, "ADV", dictionaryHelper)
							elif word[1][0] == "V":
								addWordToDict(singleWord, "V", dictionaryHelper)
						# lemma = lemmatizer.find_lemma(, 'N')
				except Exception as e:
					error = e
					print(e)
			error = "jubbijab"
	# print(len(dictionaryHelper))
	for i in dictionaryHelper:
		lemma = lemmatizer.find_lemma(i, dictionaryHelper[i][0])
		addWordToDict(lemma, dictionaryHelper[i][0], dictionary)
	# print(len(dictionary))
	dictionary = sorted(dictionary.items(), key=lambda kv: kv[1][1])
	# print(dictionary)
	save_obj(dictionary, "Bovary")




	# 		text = re.split("\W+", text)
	# 		for i in text:
	# 			if i.isupper() == False and len(i) > 1:
	# 				if i in dictionaryHelper:
	# 					dictionaryHelper[i] += 1
	# 				else:
	# 					dictionaryHelper[i] = 1
	# print(len(dictionaryHelper))
	# neuesdictionaryHelper = {}
	# for i in dictionaryHelper:
	# 	w_key, w_value = i, dictionaryHelper[i]
	# 	dictionaryHelper[w_key] = 0
	# 	i = i.lower()
	# 	if i in dictionaryHelper:
	# 		neuesdictionaryHelper[i] = w_value + dictionaryHelper[i]
	# 	else:
	# 		neuesdictionaryHelper[w_key] = w_value

	# print(len(neuesdictionaryHelper))

# 	dictionaryHelper = {}
# 	uppers = []
# 	for i in text:
# #		if i.istitle() and len(i) > 3:
# 		if len(i) > 2:
# 			if i in dictionaryHelper:
# 				dictionaryHelper[i] += 1
# 			else:
# 				dictionaryHelper[i] = 1
# 	#for i in dictionaryHelper.items():
# 	if "und" in dictionaryHelper:
# 		print("klein", dictionaryHelper["und"])
# 	if "Und" in dictionaryHelper:
# 		print("groß", dictionaryHelper["Und"])
# 	values = dictionaryHelper.items()
# 	sorted_dictionaryHelper = []
# 	for i in values:
# 		sorted_dictionaryHelper.append((i))
# 	sorted_dictionaryHelper = sorted(sorted_dictionaryHelper, key=lambda tup: tup[1])
	#print(sorted_dictionaryHelper	)

			# try:
			# 	b = TextBlob(text, parser=PatternParser(pprint=True, lemmata=True))
			# 	b = b.parse()
			# 	print(b)
			# 	for i in b:
			# 		if i in dictionaryHelper:
			# 			dictionaryHelper[i[0]][1] += 1
			# 		else:
			# 			dictionaryHelper[i[0]] = (i[1], 1)
			# 	for x in dictionaryHelper:
			# 		if dictionaryHelper[x][0] == "NN":
			# 			a.append(x)
			# 	print(a)
			# except Exception as e:
			# 	print(e)



# listBookContent(BookTitle)
dictionary = {}
a = open_obj("Bovary")
print(a)