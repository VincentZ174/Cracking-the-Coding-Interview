# check substring
def is_substring(wordOne, wordTwo):
	
	if wordTwo in wordOne:
		return True
	
	else:
		return False
	
	
# check if it is a rotation
def is_rotation(s1, s2):
	
	len_one = len(s1)
	len_two = len(s2)

	if len_one == len_two:
		s1s1 = s1 + s1
		return is_substring(s1s1, s2)

	return False


s1 = "waterbottle"
x = "wat"
y = "erbottle"
s2 = y + x

print(is_rotation(s1, s2))