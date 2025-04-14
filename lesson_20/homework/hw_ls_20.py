class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self, sound):
        print(f"This animal says '{sound}'")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def purr(self):
        print(f"{self.name} the {self.color} cat is purring.")
