from linkedlist import LinkedList


def check_palindrome(ll):

    node = ll.head
    temp = ""

    while node:
        temp = temp + node.value
        node = node.next

    if temp == temp[::-1]:
        return True

    else:
        return False


ll = LinkedList()
ll.add_multiple(['T,A,C,O,C,A,T'])
print(check_palindrome(ll))
