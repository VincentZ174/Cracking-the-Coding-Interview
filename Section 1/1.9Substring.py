#check substring
def isSubstring(wordOne, wordTwo):
	if wordTwo in wordOne:
		return True
	else:
		return False
# check if it is a rotation
def isRotation(s1, s2):
	lenOne = len(s1)
	lenTwo = len(s2)
	if (lenOne == lenTwo):
		s1s1 = s1 + s1
		return isSubstring(s1s1, s2)
	return False

s1 = "waterbottle"
x = "wat"
y = "erbottle"
s2 = y + x

print isRotation(s1, s2)