class ThreeInOne:

    def __init__(self, size_per_stack):
        
        self.numOfStacks = 3
        self.array = [0] * (size_per_stack * self.numOfStacks)
        self.sizes = [0] * self.numOfStacks
        self.size_per_stack = size_per_stack

    def push(self, item, stack_num):

        if self.is_full(stack_num):
            raise Exception("Stack is full")

        self.sizes[stack_num] += 1
        self.array[self.top_index(stack_num)] = item

    def pop(self, stack_num):

        if self.is_empty(stack_num):
            raise Exception("Stack is empty")

        value = self.array[self.top_index(stack_num)] = 0
        self.sizes[stack_num] -= 1

        return value

    def peek(self, stack_num):

        if self.is_empty(stack_num):
            raise Exception("Stack is empty")

        return self.array[self.top_index(stack_num)]

    def is_empty(self, stack_num):

        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):

        return self.sizes[stack_num] == self.size_per_stack

    def top_index(self, stack_num):

        offset = stack_num * self.size_per_stack

        return offset + self.sizes[stack_num] - 1


stack = ThreeInOne(10)
print((stack.is_empty(1)))

stack.push(5, 0)
stack.push(10, 1)
stack.push(50, 2)

print((stack.peek(0)))
print((stack.peek(1)))
print((stack.peek(2)))
