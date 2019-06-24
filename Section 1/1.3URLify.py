#!/usr/bin/python

regString = "Mr John Smith"

def URLify(regString):
	URL = ""
	for i in range(len(regString)):
		if regString[i] == " ":
			URL = URL + "%20"
		else:
			URL = URL + regString[i]
	return URL

print URLify(regString)
