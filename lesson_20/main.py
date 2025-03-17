# ООП / об'єктно орієнтовне програмування (парадигма - це спосіб досягнення цілей)
# Об'єкт - це сутність яка щось описує (можуть бути атрибути / може бути поведінка)
# Клас - це "креслення", як саме має поводитися об'єкт
# Кожна окрема машина (об'єкт) - це сутність
# Кожен клас може містити АТРИБУТИ (колір, назва, кількість чогось) - змінні
# Кожен клас може містити МЕТОДИ (говорити, їхати, відправити повідомлення) - функції

# ключове слово + назва класу
# з великої літери, CamelCase
# class Animal:
#      ... # для пайтона - проігноруй
#
# # створення об'єкту
# # змінна = КонструкторКласу()
# my_animal = Animal()

# # __init__ - конструктор об'єкту класу
# class Animal:
#     # dunder method - магічний метод
#     # викликається при створенні об'єкту класу
#     # self - це перший аргумент методу, який вказує на новостворений об'єкт
#     def __init__(self, animal_type):
#         # атрибут об'єкту
#         self.animal_type = animal_type
#
# # 1. створюється об'єкт класу Animal
# # 2. викликається метод __init__, і туди передається цей об'єкт
# #          __init__( ОБ'ЄКТ, інші аргумент )
# # 3. об'єкт присвоюється змінній
# dog_animal = Animal("dog")
# print(dog_animal.animal_type)
#
# cat_animal = Animal("cat")
# print(cat_animal.animal_type)

# Людина
# атрибути: ім'я, прізвище, вік
# class Person:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
# # 1. Спочатку викликається конструктор класу і створюється об'єкт
# #    (створюється об'єкт типу Person, але він відносно пустий)
# #    об'єкту Person відповідає self
# # 2. викликається метод __init__()
# person_a = Person("Bob", "Dylan", 22)
# #  __init__( person_a, "Bob", "Dylan", 22 )
# # self.name = name - створи атрибут name у нового об'єкту і дай йому значення name
# print( person_a.name )
# person_a.name = "John"
# print( person_a.name )

# class Car:
#
#
#     def __init__(self, speed, color, wheels_number):
#         self.speed = speed
#         self.color = color
#         self.wheels_number = wheels_number
#
#     # метод об'єкту
#     def beep(self):
#         print('Beep!')
#
#     # ми створили метод
#     def describe(self):
#         print( f'Color: {self.color}, Speed: {self.speed}, Wheels: {self.wheels_number}' )
#
# new_car = Car( 100, 'red', 4 )
# new_car.describe()
# new_car.beep()
#
# car = Car( 55, 'blue', 8 )
# car.describe()
# car.beep()

# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#         # універсальний атрибут
#         self.animal_type = 'cat'
#
#     def call(self, name):
#         if name == self.name:
#             print('Кіт дивиться на вас.')
#         else:
#             print("Кіт вас ігнорує...")
#
# cat1 = Cat('Chloe', 1, 'brown')
# cat2 = Cat('Jack', 5, 'black')
#
# cat1.call('Chloe')
# cat2.call('Chloe')
#
# print(cat1.animal_type)
# cat1.animal_type = 'donkey'
# print(cat1.animal_type)
# print(cat2.animal_type)



# ################################
# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#         # універсальний атрибут
#         self.animal_type = 'dog'
#
# cat1 = Cat('Felix', 7, 'black')
# # cat1 = Cat()
# # Cat.__init__(cat1, 'Felix', 7, 'black' )
# # ( це всередині __init__)
# # def __init__(self, name, age, color):
# #     cat1.name = name
# #     cat1.age = age
# #     cat1.color = color
# #     cat1.animal_type = 'cat'
# print(cat1.animal_type)
# cat1.animal_type = 'cat'
# print(cat1.animal_type)