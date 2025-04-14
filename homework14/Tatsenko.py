class MagicNumber:
    def __init__(self, value):
        self.__value = value

    def __add__(self, other):
        if isinstance(other, MagicNumber):
            return MagicNumber(self.__value + other.__value)

    def get_value(self):
        return self.__value

    def __repr__(self):
        return f"MagicNumber({self.__value})"

num1 = MagicNumber(5)
num2 = MagicNumber(10)
num3 = num1 + num2

print(num3)
