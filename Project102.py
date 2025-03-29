class MagicNumber:
    def __init__(self, value):

        self.__value = value


    def __add__(self, other):
        if isinstance(other, MagicNumber):
            return MagicNumber(self.__value + other.__value)
        return NotImplemented


    def get_value(self):
        return self.__value



magic1 = MagicNumber(10)
magic2 = MagicNumber(20)


result = magic1 + magic2

print(result.get_value())
