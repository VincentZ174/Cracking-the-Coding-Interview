from Stack import Stack

def sortStack(unsorted, sorted):

	size = len(unsorted)

	while len(sorted) != size:
		curr = unsorted.pop()

		if len(sorted) == 0:
			sorted.push(curr)
		else:
			while sorted.peek() > curr:
				temp = sorted.pop()
				unsorted.push(temp)
			sorted.push(curr)

	return sorted

sorted = Stack()

unsorted = Stack()
unsorted.push_multiple([4,8,2,9,1])

sortStack(unsorted, sorted)
print sorted
