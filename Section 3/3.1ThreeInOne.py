class ThreeInOne:

	def __init__(self, sizePerStack):
		self.numOfStacks = 3
		self.array = [0] * (sizePerStack * self.numOfStacks)
		self.sizes = [0] * self.numOfStacks
		self.sizePerStack = sizePerStack

	def push(self, item, stackNum):
		if self.isFull(stackNum):
			raise Exception("Stack is full")
		self.sizes[stackNum] += 1
		self.array[self.topIndex(stackNum)] = item

	def pop(self, stackNum):
		if self.isEmpty(stackNum):
			raise Exception ("Stack is empty")
		value = self.array[self.topIndex(stackNum)] = 0
		self.sizes[stackNum] -= 1
		return value

	def peek(self, stackNum):
		if self.isEmpty(stackNum):
			raise Exception("Stack is empty")
		return self.array[self.topIndex(stackNum)]

	def isEmpty(self, stackNum):
		return self.sizes[stackNum] == 0

	def isFull(self, stackNum):
		return self.sizes[stackNum] == self.sizePerStack

	def topIndex(self, stackNum):
		offset = stackNum * self.sizePerStack
		return offset + self.sizes[stackNum] - 1

stack = ThreeInOne(10)
print stack.isEmpty(1)
stack.push(5,0)
stack.push(10,1)
stack.push(50,2)
print stack.peek(0)
print stack.peek(1)
print stack.peek(2)

