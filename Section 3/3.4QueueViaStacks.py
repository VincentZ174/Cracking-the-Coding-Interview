class Queue:

	def __init__(self):

		self.s1 = []
		self.s2 = []

	def enqueue(self, item):

		if not self.s1:
			self.s1.append(item)

		else:
			self.s2 = self.s1
			self.s1 = []
			self.s1.append(item)

			for x in self.s2:
				self.s1.append(x)

			self.s2 = []
	
	def dequeue(self):

		self.s1.pop()

	def peek(self):

		return self.s1[-1]


q = Queue()
q.enqueue(5)
q.enqueue(1)
q.enqueue(3)
q.enqueue(1)
q.enqueue(9)
q.enqueue(20)

print((q.peek()))
q.dequeue()

print((q.peek()))
q.dequeue()

q.enqueue(30)
print((q.peek()))
