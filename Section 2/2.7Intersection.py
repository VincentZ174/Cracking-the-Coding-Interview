from linkedlist import LinkedList
from linkedlist import Node


def intersection(l1, l2):

    nodel1 = l1.head
    nodel2 = l2.head

    if l1.__len__() > l2.__len__():
        difference = l1.__len__() - l2.__len__()

        for i in range(difference):
            nodel1 = nodel1.next

    elif l1.__len__() < l2.__len__():
        difference = l2.__len__() - l1.__len__()

        for i in range(difference):
            nodel2 = nodel2.next

    while nodel1 and nodel2:
        if nodel1 == nodel2:
            return nodel1
        
        nodel1 = nodel1.next
        nodel2 = nodel2.next


def set_up(l1, l2):
    
    intersecting_node = Node(5)
    intersecting_node.next = Node(6)
    intersecting_node.next.next = Node(7)

    l1tail = l1.head
    l2tail = l2.head

    while l1tail.next is not None:
        l1tail = l1tail.next

    l1tail.next = intersecting_node

    while l2tail.next is not None:
        l2tail = l2tail.next

    l2tail.next = intersecting_node


l1 = LinkedList()
l2 = LinkedList()
l1.add_multiple([1, 2, 3, 4])
l2.add_multiple([9, 2])

set_up(l1, l2)

print("The intersecting node contains the value:", intersection(l1,
                                                                l2))  # This returns the intersecting node but the
# __str__ function forces the return of the node value
