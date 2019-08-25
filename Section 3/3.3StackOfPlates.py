class StackOfPlates:

    def __init__(self, capacity):

        capacity -= 1
        self.stacks = []

        if capacity < 1:
            raise Exception("Must be greater than one")

        else:
            self.capacity = capacity

    def push(self, item):

        if not self.stacks:
            self.stacks.append([item])

        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])

            else:
                self.stacks[-1].append(item)

    def pop(self):

        if not self.stacks:
            raise Exception("Stack is empty")

        else:
            data = self.stacks[-1][-1]

            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]

            else:
                del self.stacks[-1][-1]

        return data

    def pop_at(self, stack_num):

        if not self.stacks[stack_num][-1]:
            raise Exception("Stack is empty")

        else:
            if len(self.stacks[stack_num]) == 1:
                del self.stacks[stack_num]

            else:
                del self.stacks[stack_num][-1]

    def peek(self):

        return self.stacks[-1][-1]


stack = StackOfPlates(5)
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.pop()
stack.push(0)
stack.push(321)
stack.pop_at(1)
print(stack.peek())
