#check if word is one edit away from original
def checkEdit(wordOne, wordTwo):
	# figure out which word is shorter
	if len(wordOne) > len(wordTwo):
		longerWord = wordOne
		shorterWord = wordTwo
	else:
		longerWord = wordTwo
		shorterWord = wordOne
	index = 0
	counter = 0
	#check each individual character in both words to see if characters match
	for i in range(len(longerWord)):
		if shorterWord[index] != longerWord[i]:
			counter = counter + 1
		elif shorterWord[index] == longerWord[i] and shorterWord[index] != shorterWord[-1]:
			index = index + 1
	#if there is only one character that is different, return true
	if counter == 1:
		print "True"
	else:
		print "False"

wordOne = raw_input("Enter a string: ")
wordTwo = raw_input("Enter another string: ")

checkEdit(wordOne, wordTwo)
