#!/usr/bin/python

regString = "Mr John Smith"


def urlify(regString):
	
	url = ""
	
	for i in range(len(regString)):
		if regString[i] == " ":
			url = url + "%20"
			
		else:
			url = url + regString[i]

	return url


print(urlify(regString))
