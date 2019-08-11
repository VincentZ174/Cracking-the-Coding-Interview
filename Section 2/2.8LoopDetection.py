from linkedlist import LinkedList

def loopDetect(ll):
	node = ll.head
	node = node.next
	while node:
		if node == ll.head:
			print "Loop detected at:", node
			break
		node = node.next

def setUp(ll):
	node = ll.tail
	node.next = ll.head


ll = LinkedList()
ll.add_multiple([1,2,3,4])

setUp(ll)
loopDetect(ll)