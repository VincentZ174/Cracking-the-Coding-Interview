#!/usr/bin/python

#get user input
unique = raw_input("Enter a string to check if it has unique characters: ")

#check if it is unique using no addiontal data structures
def checkUnique(word):
	for i in range(len(unique)):
		curletter = unique[i]
		for j in range(len(unique)):
			if curletter == unique[j]:
				return "Not unique!"
			else:
				return "Unique"

print checkUnique(unique)
