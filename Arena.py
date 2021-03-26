# Thing.create_things() - метод создает 40 вещей, которые хранятся в списке thing_objects_list.
# Person.create_person() - метод создает 10 человек, которые хранятся в списке person_list
# start() - функция начинает бой


import random
from Thing import Thing
from Person import Person, Warrior, Paladin, Manchikin

thing_objects_list = []
person_list = []
totalizator = True


def random_class():
    class_list = [Paladin, Warrior, Manchikin]
    choice_class = random.choice(class_list)
    return choice_class


def create_person():
    name_person = ['Gladiator', 'Psycho', 'Beast', 'Maniac', 'Madman', 'Freak', 'Junkie', 'Nastya', 'Iron fist',
                   'Shooter']
    for i in range(10):
        name = random.choice(name_person)
        name_person.remove(name)
        health = 20
        attack = 10
        protection = 5
        person_list.append(random_class()(name, health, attack, protection))


def distribution_of_clothes():
    global thing_objects_list
    print('НАЧАЛАСЬ РАЗДАЧА ВЕЩЕЙ')
    for person in person_list:
        n = random.randint(1, 4)
        for j in range(n):
            item = random.choice(thing_objects_list)
            person.equip(item)


def fight():
    attacker = random.choice(person_list)
    defender = random.choice(person_list)
    while attacker == defender:
        defender = random.choice(person_list)
    print(f'{attacker} наносит удар по {defender}')
    print(f'Уровень здоровья {defender} до удара: {round(defender.health, 2)}')
    attacker.punch(defender)
    print(f'Уровень здоровья {defender} после удара: {round(defender.health, 2)}')
    if defender.health <= 0:
        person_list.remove(defender)


def init():
    global thing_objects_list
    thing_objects_list = Thing.create_things()


def start_arena():
    create_person()
    print(f'На арене будут сражаться:')
    for i in person_list:
        print(i, end=' ')
    print()
    print()
    distribution_of_clothes()
    print()
    for person in person_list:
        person.info()
    print()

    if totalizator:
        winner = input('Кто победит? Выберите персонажа: ')
        b = input('Ваша ставка: ')

    while len(person_list) > 1:
        fight()
    print()
    print(f'Победитель {person_list[0]}')

    if totalizator:
        if winner == person_list[0].name:
            print(f'Вы выиграли {b * 2}')
        else:
            print('Вы проиграли')


def stop_arena():
    global person_list
    person_list = []
