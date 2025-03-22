class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def info(self):
        print(f'Колір {self.name} - {self.color}')

class Parrot(Animal):
    def fly(self):
        print(f'Папуга {self.name} вміє добре літати')

animal = Parrot('kesha', 'purple')
animal.info()
animal.fly()





