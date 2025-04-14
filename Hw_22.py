class MagicNumber:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def __add__(self, other):
        if isinstance(other, MagicNumber):
            return self.__value + other.__value
        else:
            return NotImplemented


