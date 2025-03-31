class Magic_Number:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __add__(self, other):
        if isinstance(other, Magic_Number):
            return Magic_Number(self.__value + other.__value)
        return NotImplemented

# Приклад використання
magic1 = Magic_Number(5)
magic2 = Magic_Number(10)

result = magic1 + magic2
print(result.value)
