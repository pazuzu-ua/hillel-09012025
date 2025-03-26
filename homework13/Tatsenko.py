class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type

    def bark(self):
        return f"{self.name} says: Woof! Woof!"

my_dog = Dog("Barsik", 3, "Golden Retriever")

print(my_dog.name)
print(my_dog.bark())
print(my_dog.type)
print(my_dog.age)
