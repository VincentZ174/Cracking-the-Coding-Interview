from collections import deque


class Dog:
    def __init__(self, name):
        self.dog = name

    def __str__(self):
        return str(self.dog)


class Cat:
    def __init__(self, name):
        self.cat = name

    def __str__(self):
        return str(self.cat)


class AnimalShelter:

    def __init__(self):
        self.q1 = deque([])

    def __iter__(self):
        for animal in self.q1:
            yield animal

    def __str__(self):
        animals = [str(x) for x in self]
        return str(animals)

    def enqueue(self, item):
        self.q1.append(item)

    def dequeue_any(self):
        return self.q1.popleft()

    def dequeue_cat(self):
        for index in range(len(self.q1)):
            if type(self.q1[index]) is Cat:
                adopted = self.q1[index]
                del self.q1[index]
                return adopted

    def dequeue_dog(self):
        for index in range(len(self.q1)):
            if type(self.q1[index]) is Dog:
                adopted = self.q1[index]
                del self.q1[index]
                return adopted


Shelter = AnimalShelter()
Dog1 = Dog("Marley")
Dog2 = Dog("Milo")
Dog3 = Dog("Coco")
Dog4 = Dog("Buster")

Cat1 = Cat("Carrot")
Cat2 = Cat("Garfield")
Cat3 = Cat("Bella")
Cat4 = Cat("Kermit")

Shelter.enqueue(Cat1)
Shelter.enqueue(Dog1)
Shelter.enqueue(Dog2)
Shelter.enqueue(Cat2)
Shelter.enqueue(Dog3)
Shelter.enqueue(Dog4)
Shelter.enqueue(Cat3)
Shelter.enqueue(Cat4)

print("------Shelter before adoption------")
print(Shelter)
print()

Shelter.dequeue_dog()  # Marley gets adopted
Shelter.dequeue_any()  # Carrot gets adopted
Shelter.dequeue_cat()  # Garfield gets adopted

print("------Shelter after adoption------")
print(Shelter)


