class Animals:
    pass

class Cat(Animals):

    def make_sound(self):
        print('Meooow')

class Dog(Animals):

    def make_sound(self):
        print('Woof woof')

a1 = Cat()
a2 = Dog()
animals = [a1, a2, a2, a1, a1, a2]


def sound(ekz):
    ekz.make_sound()

sound(a1)