from linkedlist import LinkedList

def checkPalindrome(ll):
	node = ll.head
	temp = ""
	while node:
		temp = temp + node.value
		node = node.next
	if temp == temp[::-1]:
		return True
	else:
		return False

ll = LinkedList()
ll.add_multiple(['T,A,C,O,C,A,T'])
print checkPalindrome(ll)