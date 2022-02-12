import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(num)

    person = {
        'name': name,
        'tel': tel
    }

    return person


persons = []
for i in range(5):
    persons.append(gen_person())

with open('persons.json', 'w') as f:
    json.dump(persons, f, indent=2)

with open('persons.json', 'r') as f:
    print(json.load(f))
