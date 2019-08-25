# create empty hash table
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


# insert function for hash table
def insert(hash_table, key, value):

    hash_table[key] = value


# check if permutations of entered word is a palindrome
def check_palindrome(word):
    
    for value in hash_table:
        if value.replace(" ", "").lower() == value[::-1].replace(" ", "").lower():
            return True
        
        else:
            return False
        
        
# get user input
word_one = input("Enter first word: ")

permutations(word_one)
print(check_palindrome(word_one))
