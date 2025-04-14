# Абстракція
# приховання імплементації (логіка)
# from random import randint
# number = randint(1, 10)
# print(number)

# class Cat:
#     name = 'John'
#     age = 10
#
#     def say_meow(self):
#         print('Meow')
#
# my_cat = Cat()
# my_cat_1 = Cat()
#
# print( my_cat.name, my_cat_1.name )
# my_cat_1.name = 'Bob'
# print( my_cat.name, my_cat_1.name )

# ООП
# class Book:
#     ...
#
# my_book = Book()
# my_book.title = 'IT'
# my_book.pages = 700
# my_book.author = 'Stephen King'
#
# print(my_book.title)
# print(my_book.pages)

# # Конструктор
# class Book:
#     # метод конструктора, викликається після створення об'єкту
#     # self - це посилання но новостворений об'єкт
#     # ПРИКЛАД: Якщо X не встиг вчасно зайти в кабінет, не впускати X
#     def __init__(self, __title, __pages, __author):
#            #     my_book, 'IT', 700, 'S. King'
#         print("Створюю об'єкт типу Книга")
#         self.title = __title
#         self.pages = __pages
#         self.author = __author
#
# class Dog:
#     def __init__(self, __name):
#         print("Створюю об'єкт типу Собака")
#         self.name = __name
#
# # my_book = Book()
# # my_book.title = 'IT'
# # my_book.pages = 700
# # my_book.author = 'Stephen King'
# my_book = Book('IT', 700, 'S. King')
# print(my_book.name)


# class Book:
#
#     def __init__(self, __title, __pages, __author):
#         self.title = __title
#         self.pages = __pages
#         self.author = __author
#
#     # Магічний метод, який викликається якщо об'єкт треба представити текстом (рядком)
#     # print()!
#     def __str__(self):
#         return self.title
#
#     # метод об'єкту / instance method
#     def get_reading_days(self, reading_speed):
#         return self.pages / reading_speed
#
# it = Book('IT', 700, 'S. King')
# potter = Book('HarryPotter1', 500, 'JKRoaling')
#
# print(    it.get_reading_days(100)         )
# print(    potter.get_reading_days(100)         )


# Типи методів
# class Cat:
#     number_of_cats = 0
#     important_info = 'Cats have 9 lives'
#
#     def __init__(self, nickname):
#         Cat.number_of_cats += 1
#         self.nickname = nickname
#
#     # потребує об'єкт
#     def meow(self):
#         print( f'Meow! My name is {self.nickname}!' )
#
#     # методом класу: 1) він працює на класі 2) має достуб до атрибутів на рівні класу
#     @classmethod
#     def info(cls):
#         return cls.important_info
#
# # barsik = Cat('Barsik')
# # barsik.meow()
# print( Cat.info() )

############## ------------------  Наслідування / Inheritance

# # батьківський клас
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f'{self.name} is eating...')
#
# # клас нащадок
# class Dog(Animal):
#     # МЕТОД ПЕРЕВИЗНАЧАЄТЬСЯ, тобто батьківський метод - ігнорується
#     def __init__(self, name, collar_size):
#         # якщо ми хочемо перевизначити метод __init__ в іншому класі,
#         # то нам треба викликать батьківський метод __init__
#         # super() = "мій батько", звертання до батьківського класу
#         super().__init__(name) # передаємо атрибути, які є в батьківському класі
#         self.collar_size = collar_size
#
#     def bark(self):
#         print(f'{self.name} is barking')
#
# # клас нащадок
# class Cat(Animal):
#     def meow(self):
#         print(f'{self.name} is meowing')
#
#     # перевизначити метод
#     def eat(self):
#         print(f'{self.name} is eating and purring...')
#
# cat = Cat('Barsik')
# cat.eat()

# my_dog = Dog('Bob')
# my_cat = Cat('Barsik')
#
# # my_dog.eat()
# # my_cat.eat()
#
# my_dog.bark()
# my_cat.meow()

# my_dog = Dog('Bob', 22)
# print(my_dog.name, my_dog.collar_size)

# class Human:
#     def __init__(self, name):
#         self.name = name
#
# class Policeperson:
#     def arrest(self):
#         print('The policeperson arrests a suspect')
#
# class Bob(Policeperson, Human):
#     ...
#
# bob = Bob('Bob')
# bob.arrest()
