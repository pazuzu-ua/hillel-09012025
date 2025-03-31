class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep (self):
        print(f'{self.name} is sleeping')

class Dog(Animal):
    def barking (self):
        print(f'{self.name} is barking')

my_dog = Dog('Rex', 2)

my_dog.barking()
my_dog.sleep()

