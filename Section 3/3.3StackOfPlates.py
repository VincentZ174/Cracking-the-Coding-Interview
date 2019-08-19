class StackOfPlates:

	def __init__(self, capacity):
		capacity = capacity - 1
		self.stacks = []
		if capacity < 1:
			raise Exception("Must be greater than one")
		else:
			self.capacity = capacity 


	def push(self, item):

		if self.stacks == []:
			self.stacks.append([item])
		else:
			if len(self.stacks[-1]) >= self.capacity:
				self.stacks.append([item])
			else:
				self.stacks[-1].append(item)

	def pop(self):
		
		if self.stacks == []:
			raise Exception("Stack is empty")
		else:
			data = self.stacks[-1][-1]

			if len(self.stacks[-1]) == 1:
				del self.stacks[-1]
			else:
				del self.stacks[-1][-1]

		return data

	def popAt(self, stackNum):

		if self.stacks[stackNum][-1] == []:
			raise Exception("Stack is empty")
		else:
			if len(self.stacks[stackNum]) == 1:
				del self.stacks[stackNum]
			else:
				del self.stacks[stackNum][-1]

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
stack.popAt(1)
print stack.peek()





