#compress a string by character followed by the number of repeats

def StringCompress(origString):
	counter = 1
	prev = ""
	compressed = ""
	origString = origString + "\0" # \0 to indicate end of string
	for i in range(len(origString)):
		#checking for number of repetitions
		if prev == origString[i]:
			counter = counter + 1
		else:
			if prev != "": # if new character is encountered and it is not the end of the string
				compressed = compressed + prev + str(counter) #store previous character and count
				counter = 1 # reset counter
		prev = origString[i] # set prev to the newest encountered character
	# if compressed string is shorter than original print compressed	
	if len(compressed) < len(origString):
		print compressed
	else: # if it is longer print out the original string
		print origString
		
origString = raw_input("Enter a string to compress: ") 
StringCompress(origString)
