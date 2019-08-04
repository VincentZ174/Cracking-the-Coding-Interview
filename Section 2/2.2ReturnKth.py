hash_table = dict()
sizeLinkedList = 0
class Node:
	#constructor
	def __init__(self, val):
		global sizeLinkedList
		sizeLinkedList = sizeLinkedList + 1
		self.val = val # set node value
		self.next = None #set end of linked list to None
		if val in hash_table:
			hash_table[val] = hash_table[val] + 1
		else:
			hash_table[val] = 1

	def appendToTail(self, val):
		end = Node(val)
		n = self
		while(n.next != None):
			n = n.next
		n.next = end

	def traverse(self):
		node = self # start at head
		while node != None: # while not at end of linked list
			print node.val 
			node = node.next

	def returnKth(self, kth):
		node = self # start at head
		for i in range(0, sizeLinkedList-kth+1): # traverse linkedlist until you reach kth value
			if i == sizeLinkedList-kth: #print only kth value
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
				
linkedList = Node(12)
linkedList.appendToTail(30)
linkedList.appendToTail(50)
linkedList.appendToTail(1000)
linkedList.appendToTail(99)
linkedList.appendToTail(99)



kth = int(raw_input("Enter kth value to return: "))
linkedList.returnKth(kth)