class StackOfPlates:

	def __init__(self, capacity):

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
