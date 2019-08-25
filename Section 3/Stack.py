class Stack():

    def __init__(self):

        self.items = []

    def __len__(self):

        size = 0
        for items in self.items:
            size += 1
        return size

    def __str__(self):

        return ' '.join(str(x) for x in self.items)

    def push(self, item):

        self.items.append(item)

    def push_multiple(self, items):

        for item in items:
            self.items.append(item)

    def pop(self):

        return self.items.pop()

    def get_stack(self):

        return self.items

    def is_empty(self):

        return self.items == []

    def peek(self):

        if not self.is_empty():
            return self.items[-1]
