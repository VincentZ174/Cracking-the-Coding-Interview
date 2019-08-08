from linkedlist import LinkedList

hash_table = dict()

def deleteDups(ll):
	if ll.head is None:
		return

	node = ll.head
	hash_table[node.value] = node.value

	while node.next:
		if node.next.value in hash_table:
			node.next = node.next.next
		else:
			hash_table[node.next.value] = node.next.value
			node = node.next
	return ll

ll = LinkedList()
ll.add_multiple([1,1,2,2,3,4,5,5])

print "----------Linked List----------"
ll.traverse()
deleteDups(ll)
print "----------Deleting Duplicates----------"
ll.traverse()
