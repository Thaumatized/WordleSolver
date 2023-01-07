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
	forbiddenletters = ""
	includedletters = ""
	forcedletters = []
	misplacedletters = []
	for i in range(len(word)):
		if evaluation[i] == '0':
			forbiddenletters += word[i]
		if evaluation[i] == '1':
			includedletters += word[i]
			misplacedletters.append([word[i], i])
		if evaluation[i] == '2':
			forcedletters.append([word[i], i])
	
	for i in range(len(dictionary)-1, -1, -1):
		for forbiddenletter in forbiddenletters:
			if forbiddenletter in dictionary[i]:
				dictionary.pop(i)
				break
	
	for i in range(len(dictionary)-1, -1, -1):
		for includedletter in includedletters:
			if includedletter not in dictionary[i]:
				dictionary.pop(i)
				break
	
	for i in range(len(dictionary)-1, -1, -1):
		for forcedletter in forcedletters:
			if dictionary[i][forcedletter[1]] != forcedletter[0]:
				dictionary.pop(i)
				break
				
	for i in range(len(dictionary)-1, -1, -1):
		for misplacedletter in misplacedletters:
			if dictionary[i][misplacedletter[1]] == misplacedletter[0]:
				dictionary.pop(i)
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
	
	
	
