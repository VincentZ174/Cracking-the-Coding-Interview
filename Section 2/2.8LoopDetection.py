from linkedlist import LinkedList


def loop_detect(ll):

    node = ll.head
    node = node.next

    while node:
        if node == ll.head:

            print("Loop detected at:", node)
            break

        node = node.next


def set_up(ll):

    node = ll.tail
    node.next = ll.head


ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])

set_up(ll)
loop_detect(ll)
