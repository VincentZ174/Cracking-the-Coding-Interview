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

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)
node4 = Node(37)


node1.next = node2
node2.next = node3
node3.next = node4

print "----------Linked List----------"
node1.traverse()
node1.delete(99)
print "----------Linked List after Deleting----------"
node1.traverse()
