"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!


ВЫВОДЫ:
а) Добавление элемента в словарь медленнее.
Я вижу тут две причины:
    1. Данных просто больше, есть ключи и значения
    2. Нужно вычислять хэши ключей и предотвращать коллизии

б) По моим замерам все операции вполне сравнимы по времени друг с другом, и это прекрасно, потому как структура
словаря значительно сложнее и может решить больший круг задач, а операции с ней стоят сравнимо со списком,
выбивается только удаление, думаю это потому, что нужно очистить больше данных и обновить хэш таблицу.

"""

from time import time
from random import randint


def take_time(func):
    def wrapper(n):
        start_val = time()
        print(f'Замер времени для функции {func.__name__}')
        obj = func(n)
        print(f'Время выполнения: {time() - start_val}')
        return obj
    return wrapper


@take_time
def load_list(n):  # O(n)
    return [i for i in range(n)]


@take_time
def load_dict(n):  # O(n)
    return {i: randint(1, 1000) for i in range(n)}


@take_time
def get_element_from_list(lst):  # O(n)
    for i in range(len(lst)):
        _ = lst[randint(0, len(lst) - 1)]


@take_time
def get_element_from_dict(dct):  # O(n)
    for i in range(len(dct.keys())):
        _ = dct[randint(0, len(lst) - 1)]


@take_time
def edit_element_from_list(lst):  # O(n)
    for i in range(len(lst)):
        lst[i] += 1


@take_time
def edit_element_from_dict(dct):  # O(n)
    for i in dct:
        dct[i] += 1


@take_time
def del_element_from_list(lst):  # O(n^2)
    for i in range(len(lst) - 1, -1, -1):
        del lst[i]


@take_time
def del_element_from_dict(dct):  # O(n)
    for i in range(len(dct.keys())):
        del dct[i]


if __name__ == '__main__':
    n = 5000000

    print('Задание а)')
    lst = load_list(n)
    dct = load_dict(n)
    print()

    print('Задание в)')
    get_element_from_list(lst)
    get_element_from_dict(dct)

    edit_element_from_list(lst)
    edit_element_from_dict(dct)

    del_element_from_list(lst)
    del_element_from_dict(dct)

    print(lst)
    print(dct)
