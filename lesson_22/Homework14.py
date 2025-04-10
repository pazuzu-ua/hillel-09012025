class MagicNumber:
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return f"MagicNumber: {self.__value}"

    def __add__(self, other):
        if isinstance(other, MagicNumber):
            return MagicNumber(self.__value + other.__value)

        elif isinstance(other, int) or isinstance(other, float):
            return MagicNumber(self.__value + other)


num1 = MagicNumber(50)
num2 = MagicNumber(90)
result = num1 + num2
print(result)
