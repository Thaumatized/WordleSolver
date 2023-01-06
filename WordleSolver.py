alphabet = "abcdefghijklmnopqrstuvwxyz"
requiredcharacters = ""
requiredpositionedcharacters = "     "

for attempt in range(6):
	listedsuggestions = []
	for i in range(len(alphabet)):
		listedsuggestions.append([])
	for i1 in range(len(alphabet)):
		suggestion = "";
		for i2 in range(len(alphabet)):
			for i3 in range(len(alphabet)):
				for i4 in range(len(alphabet)):
					for i5 in range(len(alphabet)):
						suggestion = alphabet[i1] + alphabet[i2] + alphabet[i3] + alphabet[i4] + alphabet[i5]
						skip = False
						for i in range(len(suggestion)):
							if requiredpositionedcharacters[i] != ' ' and suggestion[i] != requiredpositionedcharacters[i]:
								skip = True
							break
						for i in range(len(requiredcharacters)):
							if requiredcharacters[i] not in suggestion:
								skip = True
							break
							
						if skip:
							suggestion = ""
							
		if suggestion != "":
			listedsuggestions[i1].append(suggestion)
	
	for i in range(len(listedsuggestions)-1, -1, -1):
			if listedsuggestions[i] != []:
				listedsuggestions.pop(i)
	
	row = 0
	while True:
		listsover = True
		for i in range(len(listedsuggestions)):
			if len(listedsuggestions[i]) > row:
				print(listedsuggestions + "     ")
				listsover = False
			else:
				print("          ")
		if listsover:
			break
		row += 1
	
	
	
	print("alphabet: " + alphabet)
	print("required characters: " + requiredcharacters)
	print("positioned characters: " + requiredpositionedcharacters)
	
	print("What word did you try?")
	answer = input()
	print("Please input the result as a string of numbers. use 0 for not in word, 1 for in word but wrong place and 2 for correct place")
	evaluation = input()
	for i in range(len(answer)):
		if evaluation[i] == '0':
			alphabet = alphabet.replace(answer[i], "")
		if evaluation[i] == '1':
			requiredcharacters += answer[i]
		if evaluation[i] == '2':
			requiredpositionedcharacters = requiredpositionedcharacters[:i] + answer[i] + requiredpositionedcharacters[i+1:]
