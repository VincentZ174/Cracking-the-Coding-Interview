# compress a string by character followed by the number of repeats
def string_compress(orig_string):
	
	counter = 1
	prev = ""
	compressed = ""
	orig_string += "\0"  # \0 to indicate end of string

	for i in range(len(orig_string)):
		# checking for number of repetitions
		if prev == orig_string[i]:
			counter += 1

		else:
			if prev != "": # if new character is encountered and it is not the end of the string
				compressed = compressed + prev + str(counter) # store previous character and count
				counter = 1 # reset counter

		prev = orig_string[i] # set prev to the newest encountered character

	# if compressed string is shorter than original print compressed	
	if len(compressed) < len(orig_string):
		print(compressed)
	# if it is longer print out the original string
	else:
		print(orig_string)


orig_string = input("Enter a string to compress: ") 
string_compress(orig_string)
