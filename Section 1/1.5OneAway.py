# check if word is one edit away from original
def check_edit(word_one, word_two):
	
	# figure out which word is shorter
	if len(word_one) > len(word_two):
		longer_word = word_one
		shorter_word = word_two
		
	else:
		longer_word = word_two
		shorter_word = word_one
		
	index = 0
	counter = 0
	# check each individual character in both words to see if characters match
	for i in range(len(longer_word)):
		if shorter_word[index] != longer_word[i]:
			counter += 1
			
		elif shorter_word[index] == longer_word[i] and shorter_word[index] != shorter_word[-1]:
			index += 1
			
	# if there is only one character that is different, return true
	if counter == 1:
		print("True")
		
	else:
		print("False")


word_one = input("Enter a string: ")
word_two = input("Enter another string: ")

check_edit(word_one, word_two)
