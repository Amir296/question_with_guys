from collections import Counter
from dataclasses import dataclass

import itertools
from enum import Enum, auto


class Country(Enum):
    ENGLAND = auto()
    USA = auto()
    RUSSIA = auto()
    NORWAY = auto()
    JAPAN = auto()


class Subject(Enum):
    MATH = auto()
    PHYSICS = auto()
    LITERATURE = auto()
    BIBLE = auto()
    SCIENCE = auto()


class Drink(Enum):
    MILK = auto()
    TEA = auto()
    JUICE = auto()
    COFFE = auto()
    WATER = auto()


class Hobby(Enum):
    NEWS_PAPERS = auto()
    TV = auto()
    COMICS = auto()
    BOOKS = auto()
    RADIO = auto()


class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()
    WHITE = auto()


class Position(Enum):
    RIGHT = auto()
    RIGHT_MED = auto()
    MED = auto()
    LEFT_MED = auto()
    LEFT = auto()


@dataclass
class Person:
    country: Country
    favorite_subject: Subject
    drink: Drink
    hobby: Hobby
    house_color: Color
    position: Position


def xor_bool(a, b):
    return (a or b) and not (a and b)


def legal_alone(person: Person) -> tuple[bool, int]:
    amir =1
    # cond2
    if xor_bool(person.country == Country.ENGLAND, person.drink == Drink.TEA):
        # print(f'false 2{person}')
        return False, 2
    # cond 3
    if person.hobby == Hobby.COMICS and person.favorite_subject == Subject.MATH:
        return False, 3


    # cond 4
    if xor_bool(person.country == Country.USA, person.house_color == Color.RED):
        return False, 4



    # cond 5
    if person.position == Position.MED or person.house_color == Color.RED or person.hobby == Hobby.NEWS_PAPERS or person.drink == Drink.MILK:
        if person.position != Position.MED or person.house_color != Color.RED or person.hobby != Hobby.NEWS_PAPERS or person.drink != Drink.MILK:
            # print(f'false 5 {person}')
            return False, 5

    if person.country == Country.NORWAY:
        amir = 2
        print(amir)

    # cond6
    if xor_bool(person.country == Country.RUSSIA, person.favorite_subject == Subject.PHYSICS):
        return False, 6
    # cond 7
    if person.country == Country.NORWAY and person.house_color == Color.BLUE:
        return False, 7
    # cond8
    if xor_bool(person.hobby == Hobby.NEWS_PAPERS, person.favorite_subject == Subject.LITERATURE):
        return False, 8
    # cond 9
    if person.hobby == Hobby.TV and person.favorite_subject == Subject.BIBLE:
        return False, 9

    # cond10
    if person.country == Country.NORWAY or person.hobby == Hobby.TV or person.position == Position.LEFT:
        if person.country != Country.NORWAY or person.hobby != Hobby.TV or person.position != Position.LEFT:
            # print(f'false 10 {person}')
            return False, 10

    # cond11
    if xor_bool(person.hobby == Hobby.TV, person.house_color == Color.YELLOW):
        # print(f'false 11{person}')
        return False, 11
    # cond12
    if xor_bool(person.hobby == Hobby.BOOKS, person.drink == Drink.JUICE):
        # print(f'false 11{person}')
        return False, 12

    # cond14
    if xor_bool(person.hobby == Hobby.RADIO, person.country == Country.JAPAN):
        # print(f'false 14{person}')
        return False, 14

    # cond15
    if person.hobby == Hobby.RADIO or person.house_color == Color.GREEN or person.drink == Drink.COFFE:
        if person.hobby != Hobby.RADIO or person.house_color != Color.GREEN or person.drink != Drink.COFFE:
            # print(f'false_15 {person}')
            return False, 15

    return True, 0


fails = []


def next_solution_generator():
    cartesian_product = list(itertools.product(Country, Subject, Drink, Hobby, Color, Position))

    index = -1
    print(len(list(cartesian_product)))

    while index < len(cartesian_product):
        index += 1  # Move to the next index
        # print(index)
        tup = cartesian_product[index]
        person = Person(country=tup[0], favorite_subject=tup[1], drink=tup[2], hobby=tup[3], house_color=tup[4], position=tup[5])
        is_legal, fail_cond = legal_alone(person)

        if not is_legal:
            fails.append(fail_cond)
            continue
        yield cartesian_product[index]  # Yield the current element


def tuple_2_person(tup: tuple) -> Person:
    return Person(country=tup[0], favorite_subject=tup[1], drink=tup[2], hobby=tup[3], house_color=tup[4], position=tup[5])


def neighbours(person1: Person, person2: Person):
    if person1.position == Position.LEFT:
        return person2.position == Position.LEFT_MED
    if person1.position == Position.LEFT_MED:
        return person2.position in [Position.LEFT, Position.MED]
    if person1.position == Position.MED:
        return person2.position in [Position.LEFT_MED, Position.RIGHT_MED]
    if person1.position == Position.RIGHT_MED:
        return person2.position in [Position.MED, Position.RIGHT]
    if person1.position == Position.RIGHT:
        return person2.position == Position.RIGHT_MED


def cond2(person1: Person, person2: Person) -> bool:
    if person1.country == Country.ENGLAND and person2.country == Country.NORWAY or person2.country == Country.ENGLAND and person1.country == Country.NORWAY:
        if neighbours(person1, person2):
            return True
        else:
            return False
    else:
        return True


def cond3(person1: Person, person2: Person) -> bool:
    if person1.hobby == Hobby.COMICS and person2.favorite_subject == Subject.MATH or person2.hobby == Hobby.COMICS and person1.favorite_subject == Subject.MATH:
        if neighbours(person1, person2):
            return True
        else:
            return False
    else:
        return True


def cond7(person1: Person, person2: Person) -> bool:
    if person1.country == Country.NORWAY and person2.house_color == Color.BLUE or person2.country == Country.NORWAY and person1.house_color == Color.BLUE:
        if neighbours(person1, person2):
            return True
        else:
            return False
    else:
        return True


def cond9(person1: Person, person2: Person) -> bool:
    if person1.hobby == Hobby.TV and person2.favorite_subject == Subject.BIBLE or person2.hobby == Hobby.TV and person1.favorite_subject == Subject.BIBLE:
        if neighbours(person1, person2):
            return True
        else:
            return False
    else:
        return True


def cond12(person1: Person, person2: Person) -> bool:
    # check only books, juice was check before
    if person1.country == Country.USA and person2.hobby == Hobby.BOOKS or person2.country == Country.USA and person1.hobby == Hobby.BOOKS:
        if neighbours(person1, person2):
            return True
        else:
            return False
    else:
        return True


def right_to(person1: Person, person2: Person) -> bool:
    match person1.position:
        case Position.LEFT:
            return person2.position == Position.LEFT_MED
        case Position.LEFT_MED:
            return person2.position == Position.MED
        case Position.MED:
            return person2.position == Position.RIGHT_MED
        case Position.RIGHT_MED:
            return person2.position == Position.RIGHT
        case Position.RIGHT:
            return False


def cond13(person1: Person, person2: Person) -> bool:
    # check only books, juice was check before
    if person1.house_color == Color.WHITE and person2.house_color == Color.GREEN:
        return right_to(person1, person2)
    if person2.house_color == Color.WHITE and person1.house_color == Color.GREEN:
        return right_to(person2, person1)
    return True


def are_2_comply(person1: tuple, person2: tuple):
    if any(person1[i] == person2[i] for i in range(len(person1))):
        return False
    person_1 = tuple_2_person(person1)
    person_2 = tuple_2_person(person2)
    if not cond2(person_1, person_2):
        return False
    if not cond3(person_1, person_2):
        return False

    if not cond7(person_1, person_2):
        return False

    if not cond9(person_1, person_2):
        return False

    if not cond12(person_1, person_2):
        return False

    if not cond13(person_1, person_2):
        return False

    return True


def check_if_group_legal(group: list[tuple]) -> bool:
    for pair in itertools.combinations(group, r=2):
        if not are_2_comply(pair[0], pair[1]):
            return False
    return True


print(f'len = {len(list(itertools.product(itertools.permutations(Color), itertools.permutations(Subject))))}')
# itertools.product(itertools.permutations(Color), itertools.permutations(Subject))))}')

person = next_solution_generator()
# person2 = next_solution_generator()
# person3 = next_solution_generator()
# person4 = next_solution_generator()
# person5 = next_solution_generator()

legal_persons = []

while True:  # len(legal_persons) < 76:
    try:
        person1 = next(person)
        legal_persons.append(person1)
    except Exception as e:
        break

element_count = Counter(fails)
print(f'legal persons = {len(legal_persons)}')
# person2 = next(person)
# are_2_comply(person1, person2)
index = 0
brut = 1
if brut:
    for group in itertools.combinations(legal_persons, r=5):
        #print(index)
        if check_if_group_legal(group):
            print(f'!!!! {group}')
            exit(7)
        index += 1
group_usa = [person for person in legal_persons if person[0] == Country.USA]  # only 1
legal_persons_set = set(legal_persons)
legal_persons_set.remove(group_usa[0])

for group1 in itertools.combinations(legal_persons_set, r=4):
    print(index)
    g = list(group1) + group_usa
    if check_if_group_legal(g):
        print(f'{g}')
        break
    index += 1
