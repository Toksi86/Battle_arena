class Person:
    class_name = 'Человек'

    def __init__(self, name, health, attack, protection):
        self.name = name
        self.health = health
        self.attack = attack
        self.protection = protection

    def __repr__(self):
        # return self.class_name
        return str(self.name) + ' (' + self.class_name + ')'

    def equip(self, item):
        self.health = self.health + item.health
        self.attack = self.attack + item.attack
        self.protection = self.protection + item.protection
        print(f'{self} получает предмет {item}')

    def punch(self, defender):
        defender.health = defender.health - max(1, (self.attack - defender.protection))

    def info(self):
        print(f'{self}, атака: {self.attack}, защита: {round(self.protection, 2)}, здоровье: {self.health}')


class Paladin(Person):
    class_name = 'Paladin'

    def __init__(self, name, health, attack, protection):
        super().__init__(name, health, attack, protection)
        self.health = health * 2
        self.protection = protection * 2


class Warrior(Person):
    class_name = 'Warrior'

    def __init__(self, name, health, attack, protection):
        super().__init__(name, health, attack, protection)
        self.attack = attack * 4.7


class Manchikin(Person):
    class_name = 'Manchikin'

    def equip(self, item):
        self.health = self.health + item.health * 2
        self.attack = self.attack + item.attack * 3
        self.protection = self.protection + item.protection * 2
        print(f'{self} получает предмет {item}')