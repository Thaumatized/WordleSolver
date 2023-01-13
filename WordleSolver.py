import os
import random


characters = "abcdefghijklmnopqrstuvwxyz"
dictionary = []	
	
def getdictionary(length):
	if not os.path.exists("StrippedDictionaries"):
		os.makedirs("StrippedDictionaries")
	
	path = os.path.join("StrippedDictionaries", str(length) + "_dictionary.txt")
	
	if not os.path.exists(path):
		newdictionary = open(path, "w")
		masterdictionary = open("dictionary.txt", "r").read().split("\n")
		for word in masterdictionary:
			if len(word) == length:
				newdictionary.write(word.lower() + "\n")
				
	#last one is removed, because the automatic generation always makes the last row be empy.
	return open(path, "r").read().split("\n")[:-1]
	

#takes words out of a dictionary based on results from wordle
def stripdictionary(dictionary, word, evaluation):
	lettersmin = {}
	lettersmax = {}
	knownletterpositions = {}
	knownfalseletterpositions = {}
	
	#lettersmin and lettersmax
	for i in range(len(word)):
		zeroes = 0
		onesandtwos = 0
		for i2 in range(len(word)):
			if word[i2] == word[i]:
				if evaluation[i2] == '0':
					zeroes += 1
				else:
					onesandtwos += 1
		if onesandtwos != 0:
			if word[i] not in lettersmin:
				lettersmin[word[i]] = 0
			if lettersmin[word[i]] < onesandtwos:
				lettersmin[word[i]] = onesandtwos
		if zeroes != 0:
			if word[i] not in lettersmax:
				lettersmax[word[i]] = 69
			if lettersmax[word[i]] > onesandtwos:
				lettersmax[word[i]] = onesandtwos
	
	#Known- and and knownfalsepositions
	for i in range(len(word)):
		if evaluation[i] == '1' or evaluation[i] == 0:
			if word[i] not in knownfalseletterpositions:
				knownfalseletterpositions[word[i]] = []
			knownfalseletterpositions[word[i]].append(i)
		if evaluation[i] == '2':
			if word[i] not in knownletterpositions:
				knownletterpositions[word[i]] = []
			knownletterpositions[word[i]].append(i)
			
	#debugging for variables used in filtering
	'''
	print("lettersmin:")
	for key in lettersmin:
		print(" -> " + key + " -> " + str(lettersmin[key]))
	print("lettersmax:")
	for key in lettersmax:
		print(" -> " + key + " -> " + str(lettersmax[key]))
	print("known:")
	for key in knownletterpositions:
		print(" -> " + key)
		for pos in knownletterpositions[key]:
			print("     -> " + str(pos))
	print("known false:")
	for key in knownfalseletterpositions:
		print(" -> " + key)
		for pos in knownfalseletterpositions[key]:
			print("     -> " + str(pos))
	'''
	
	#remove words with too many instances of a letter
	for i in range(len(dictionary)-1, -1, -1):
		for char in lettersmax:
			if dictionary[i].count(char) > lettersmax[char]:
				dictionary.pop(i)
				break
	
	#remove words with too few instances of a letter
	for i in range(len(dictionary)-1, -1, -1):
		for char in lettersmin:
			if dictionary[i].count(char) < lettersmin[char]:
				dictionary.pop(i)
				break
	
	#remove word with letters in the wrong places
	for i in range(len(dictionary)-1, -1, -1):
		for char in knownfalseletterpositions:
			breakfurther = False
			for pos in knownfalseletterpositions[char]:
				if dictionary[i][pos] == char:
					dictionary.pop(i)
					breakfurther = True
					break
			if breakfurther:
				break
				
				
	#remove word with wrong letters in known positions
	for i in range(len(dictionary)-1, -1, -1):
		for char in knownletterpositions:
			breakfurther = False
			for pos in knownletterpositions[char]:
				if dictionary[i][pos] != char:
					dictionary.pop(i)
					breakfurther = True
					break
			if breakfurther:
				break
				
	return dictionary


print("Welcome to wordle solver.")
length = -1
while(length == -1):
	print("Please input the length of the word")
	lengthinput = input()
	if lengthinput.isnumeric():
		length = int(lengthinput)
dictionary = getdictionary(length)

print("now to get started, you should start with a word that has as many different characters as possible. Here is a few suggestions.")

for i in range(10):
	suggestion = ""
	while True:
		suggestion = dictionary[int(len(dictionary) * random.random())]
		breakingout = True
		for char in suggestion:
			if suggestion.count(char) > 1:
				breakingout = False
		if breakingout:
			break
	print(suggestion)
	
while True:
	validinput = False
	wordinput = ""
	while not validinput:
		print("What word did you use?")
		wordinput = input().lower()
		validinput = len(wordinput) == length
		
	validinput = False
	evaluationinput = ""
	while not validinput:
		print("What did we learn? write a string of numbers, with 0 meaning the letter is not in the word, 1 meaning it is but isn't in the correct position and 2 meaning it is fully correct.'")
		evaluationinput = input()
		validinput = len(evaluationinput) == length and len(evaluationinput.replace("0", "").replace("1", "").replace("2", "")) == 0
	
	if "0" not in evaluationinput and "1" not in evaluationinput:
		print("Wohoo!")
		break
	
	dictionary = stripdictionary(dictionary, wordinput, evaluationinput)
	
	if len(dictionary) == 0:
		print("Sorry, it seems the word isn't in my dictionary.")
		break
	if len(dictionary) == 1:
		print("It seems that the only possible answer is:")
		print(dictionary[0])
	elif len(dictionary) <= 10:
		print("We are getting close, only " + str(len(dictionary)) + " possibilities left. Here are all the possibilities I know;")
		for i in range(len(dictionary)):
			print(dictionary[i])
	else:
		print("there are " + str(len(dictionary)) + " possibilities left. Here are some of them:")
		for i in range(10):
			print(dictionary[int(len(dictionary) * random.random())])
	
	
	
