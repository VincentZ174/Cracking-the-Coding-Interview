from linkedlist import LinkedList


def sum_lists(l1, l2):

    total = ""
    carry = 0

    if l1.__len__() > l2.__len__():

        node1 = l1.head
        node2 = l2.head
        while node2:
            total = str(((node1.value + node2.value) % 10) + carry) + total
            carry = (node1.value + node2.value) // 10
            node1 = node1.next
            node2 = node2.next

        while node1:
            total = str(node1.value + carry) + total
            node1 = node1.next

    elif l1.__len__() < l2.__len__():
        node1 = l2.head
        node2 = l1.head

        while node2:
            total = str(((node1.value + node2.value) % 10) + carry) + total
            carry = (node1.value + node2.value) // 10
            node1 = node1.next
            node2 = node2.next

        while node1:
            total = str(node1.value + carry) + total
            node1 = node1.next

    else:
        node1 = l1.head
        node2 = l2.head

        while node1:
            total = str(((node1.value + node2.value) % 10) + carry) + total
            carry = (node1.value + node2.value) // 10
            node1 = node1.next
            node2 = node2.next

    print(total)


l1 = LinkedList()
l1.add_multiple([9, 2, 3])

l2 = LinkedList()
l2.add_multiple([1, 1, 1])

sum_lists(l1, l2)
