from Stack import Stack


class MinStack:

	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def push(self, item):

		self.s1.push(item)
		
		if self.s2.is_empty() or item <= self.get_min():
			self.s2.push(item)

	def pop(self):
		
		if self.peek() == self.get_min():
			self.s2.pop()
			
		self.s1.pop()

	def peek(self):
		
		return self.s1.items[-1]

	def get_min(self):
		
		if not self.s2.is_empty():
			return self.s2.items[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

print(minStack.get_min())
minStack.pop()
minStack.peek()
print(minStack.get_min())
