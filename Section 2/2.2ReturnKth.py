from linkedlist import LinkedList


def return_kth(ll, kth):

    node = ll.head  # start at head

    for i in range(0, ll.__len__() - kth + 1):  # traverse linkedlist until you reach kth value
        if i == ll.__len__() - kth:  # print only kth value
            print(node.value)

        node = node.next


ll = LinkedList()
ll.add_multiple([2, 3, 4, 5, 6, 7])

kth = int(input("Enter kth value to return: "))
return_kth(ll, kth)
