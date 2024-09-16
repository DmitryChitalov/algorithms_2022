from random import randint
from timeit import timeit
from collections import OrderedDict


def insert_val(dictionary):
    for i in range(1000):
        dictionary[i] = randint(0, 100)
    return dictionary


diction = {}
order_dict = OrderedDict()
print(timeit('insert_val(diction)', globals=globals(), number=1000))  # 1.13
print(timeit('insert_val(order_dict)', globals=globals(), number=1000))  # 1.14


def change_val(dictionary):
    for i in range(1000):
        dictionary[i] = randint(0, 100)
    return dictionary


print(timeit('change_val(diction)', globals=globals(), number=1000))  # 1.07
print(timeit('change_val(order_dict)', globals=globals(), number=1000))  # 1.11

# В операциях заполнения и изменения словарей времена исполнения от запуска к запуску
# очень близки, явного выигрыиша нет нигде.


def update_to(dictionary):
    sub_dict = {}
    for i in range(1000):
        sub_dict[i] = randint(0, 100)
        dictionary.update(sub_dict)


print(timeit('update_to(diction)', globals=globals(), number=100))  # 15.356
print(timeit('update_to(order_dict)', globals=globals(), number=100))  # 66.683
# операция update работает в 4 раза медленнее для упорядоченного словаря


def get_from(dictionary):
    return [(key, el) for key, el in dictionary.items()]


print(timeit('get_from(diction)', globals=globals(), number=100))  # 0.00603
print(timeit('get_from(order_dict)', globals=globals(), number=100))  # 0.014
# извлечение элемента в 2.5 раза быстрее из обычного словаря


def pop_from(dictionary):
    for i in range(10):
        dictionary.popitem()
    return dictionary


print(timeit('pop_from(diction)', globals=globals(), number=100))  # 0.00011
print(timeit('pop_from(order_dict)', globals=globals(), number=100))  # 0.00016


def make_copy(dictionary):
    copy_dict = dictionary.copy()
    return copy_dict


print(timeit('make_copy(diction)', globals=globals(), number=1000))  # 0.0043
print(timeit('make_copy(order_dict)', globals=globals(), number=1000))  # 0.076


def clear_dict(dictionary):
    dictionary.clear()
    return dictionary


print(timeit('clear_dict(diction)', globals=globals(), number=1))  # 1.13e-5
print(timeit('clear_dict(order_dict)', globals=globals(), number=1))  # 1.33e-5
'''
Таким образом, явные изменения во времени наблюдаются лищь в операциях update и получения связки
ключ-значение, при которых обыкновенный словарь работает быстрее. Т к после выхода версии 3.5
обыкновенный словарь запоминает порядок следования связки ключ-значение, а также т к он нигде
не проигрывает во времени упорядоченному словарю, то смысла использовать OrderedDict нет.
'''
