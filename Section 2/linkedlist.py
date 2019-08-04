class Node:
	#constructor
	def __init__(self, val):
		self.val = val # set node value
		self.next = None #set end of linked list to None
	def traverse(self):
		node = self # start at head
		while node != None: # while not at end of linked list
			print node.val 
			node = node.next
	def appendToTail(self, val):
		end = Node(val)
		n = self
		while(n.next != None):
			n = n.next
		n.next = end

	def delete(self, val):
		temp = self

		if(temp is not None):
			if(temp.val == val):
				self = temp.next
				temp = None
				return

		while(temp is not None):
			if(temp.val == val):
				break
			prev = temp
			temp = temp.next

		if(temp == None):
			return

		prev.next = temp.next
		temp = None

linkedList = Node(12)
linkedList.appendToTail(50)
linkedList.appendToTail(30)
linkedList.appendToTail(40)

print "----------Linked List----------"
linkedList.traverse()
print "----------Linked List after Deleting----------"
linkedList.traverse()
