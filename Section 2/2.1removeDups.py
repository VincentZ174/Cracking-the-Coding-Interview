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

	def deleteDups(self):
		node = self
		for key,val in hash_table.items():
			print val
			if val > 1:
				node.delete(key)

linkedList = Node(12)
linkedList.appendToTail(30)
linkedList.appendToTail(50)
linkedList.appendToTail(1000)
linkedList.appendToTail(99)
linkedList.appendToTail(99)
linkedList.appendToTail(50)

print "----------Linked List----------"
linkedList.traverse()
linkedList.deleteDups()
print "----------Deleting Duplicates----------"
linkedList.traverse()
