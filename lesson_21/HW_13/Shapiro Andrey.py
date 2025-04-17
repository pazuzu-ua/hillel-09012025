class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eating(self):
        print("The animal is eating")

class Bird(Animal):
    def flying(self):
        print("The bird is flying")


my_bird = Bird(name='John',age=5)
print(f"I have a bird, its name is {my_bird.name} and it's {my_bird.age} years old.")
my_bird.eating()
my_bird.flying()