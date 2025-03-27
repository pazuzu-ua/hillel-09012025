# наслідування
# абстракцію

# інкапсуляція
# int numbers[] = { 1, 2, 3 }
# numbers[15]

# class Account:
#     def __init__(self, amount):
#         # публічний атрибут
#         self.amount = amount

# a.amount
# a.amount = 200

# class Account:
#     def __init__(self, amount):
#         # приватними (private) атрибут
#         self._amount = amount
#
#     # getter
#     def get_amount(self):
#         # тут буде валідація
#         return self._amount
#
#     # setter
#     def set_amount(self, value):
#         # тут буде валідація
#         self._amount = value
#
#
# a = Account(0)
# a.set_amount(1000)
# a._amount = 400
# print( a.get_amount() )

# class Account:
#     def __init__(self, amount, name):
#         # protected (захищені) атрибути
#         self.__amount = amount           #  _Account__amount
#         self.name = name
#
#     # getter
#     @property
#     def amount(self):
#         # validation
#         return self.__amount
#
#     # setter
#     @amount.setter
#     def amount(self, value):
#         # validation
#         if value > 9999:
#             raise ValueError('Too much money')
#         self.__amount = value
#
# a = Account(200, 'MyMoney')
# a.amount = 5020
# print(a.amount)

# -------------------------- поліморфізм
# class Account:
#     def __init__(self, amount):
#         self.amount = amount
#
#     # for print() and str()
#     def __str__(self):
#         return f"Account with {self.amount} money"
#
#     # for +
#     #            a1    a2
#     def __add__(self, other):
#         #                       a2
#         if isinstance( other, Account ):
#             #         a1.amount + a2.amount
#             #         5000      + 4000
#             return self.amount + other.amount
#         elif isinstance( other, int ) or isinstance( other, float ):
#             #       a1.amount  + 22
#             #          5000    + 22
#             return self.amount + other
#
#     # for -
#     def __sub__(self, other):
#         return self.amount - other.amount
#
#     # for >
#     def __gt__(self, other):
#         return self.amount > other.amount
#
# a1 = Account(5000)
# a2 = Account(4000)
#
# a1 + a2             # ===>     a1.__add__(a2)
#
# print( a1 + a2 ) # ===>     a1.__add__(a2)
# print( a1 + 22 ) # ===>     a1.__add__(22)

# ---------------------- dataclasses
class PersonA:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def info(self):
        return f'Name: {self.name} {self.surname}\nAge: {self.age}'

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    surname: str
    age: int

    def info(self):
        return f'Name: {self.name} {self.surname}\nAge: {self.age}'


pa = PersonA('John', 'Doe', 40)
p1 = Person('John', 'Doe', 40)
p2 = Person('John', 'Doe', 40)
print( pa )
print( p1 == p2 )
