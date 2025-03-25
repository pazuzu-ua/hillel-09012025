
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} говорить!")
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} гавкає!")
dog = Dog("Шерлок", 3, "Джек Рассел")
dog.speak()
dog.bark()

