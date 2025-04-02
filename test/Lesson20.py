class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.animal_type = 'cat'

    def call(self, name):
        if name == self.name:
            print('Cat is looking at you')
        else:
            print('Cat is ignoring you')


cat = Cat('Chloe', 1, 'brown')
cat2 = Cat('Chico', 2, 'black')

cat.call('Chico')
