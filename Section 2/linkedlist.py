class Node:

    def __init__(self, value, next_node=None):
        
        self.value = value
        self.next = next_node

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
            length += 1
            node = node.next

        return length

    def traverse(self):
        current = self.head

        while current:
            if current.next is not None:
                print(str(current) + " ->", end=' ')

            else:
                print(current.value)

            current = current.next

    def add(self, value):

        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_multiple(self, values):
        for v in values:
            self.add(v)
