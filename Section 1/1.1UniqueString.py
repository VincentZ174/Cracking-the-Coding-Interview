# get user input
unique = input("Enter a string to check if it has unique characters: ")

# check if it is unique using no addiontal data structures

def check_unique(word):
	
	for i in range(len(unique)):
		curletter = unique[i]
		
		for j in range(len(unique)):
			if curletter == unique[j]:
				return "Not unique!"
			
			else:
				return "Unique"

print(check_unique(unique))
