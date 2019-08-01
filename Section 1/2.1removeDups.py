hash_table = dict()
class Node:
	#constructor
	def __init__(self, val):
		self.val = val # set node value
		self.next = None #set end of linked list to None
		if val in hash_table:
			hash_table[val] = hash_table[val] + 1
		else:
			hash_table[val] = 1

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

	def deleteDups(self):
		node = self
		for key,val in hash_table.items():
			print val
			if val > 1:
				node.delete(key)
node1 = Node(12)
node2 = Node(99)
node3 = Node(37)
node4 = Node(37)


node1.next = node2
node2.next = node3
node3.next = node4

print "----------Linked List----------"
node1.traverse()
node1.deleteDups()
print "----------Deleting Duplicates----------"
node1.traverse()
