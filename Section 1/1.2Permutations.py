#create empty hash table
hash_table = {}

def permutations(string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        insert(hash_table, "".join(string), "".join(string))
    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)

#insert function for hash table
def insert(hash_table, key, value):
    hash_table[key] = value

#check if one word is a permutation of another
def checkPerm(wordOne, wordTwo):
    if wordOne == hash_table[wordOne]:
        print wordOne + " is a permutation of " + wordTwo
    else:
        print wordOne + "is not a permutation of " + wordTwo
        
#get user input
wordOne = raw_input("Enter first word: ")
wordTwo = raw_input("Enter second word: ")

permutations(wordTwo)
checkPerm(wordOne, wordTwo)