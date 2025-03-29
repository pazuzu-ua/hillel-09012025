class MagicNumber:
    def __init__(self, value = 0):
        self.__value = value
    @property
    def value(self):
        return self.__value
    def __str__(self):
        return f'{self.__value}'
    def __add__(self, other: 'MagicNumber'):
        return MagicNumber(self.__value + other.__value)


a = MagicNumber(3)
b = MagicNumber(4)
print(a + b)
