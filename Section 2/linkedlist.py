class Node:

    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __len__(self):
        length = 0
        node = self.head
        while node:
            length = length + 1
            node = node.next
        return length

    def traverse(self):
        current = self.head
        while current:
            if current.next != None:
                print str(current) + " ->",
            else:
                print current.value
            current = current.next


    def add(self, value):
        if self.head == None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail


    def add_multiple(self, values):
        for v in values:
            self.add(v)
