class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Клічка: {self.name}, вік: {self.age} років.")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} Мяу!")
