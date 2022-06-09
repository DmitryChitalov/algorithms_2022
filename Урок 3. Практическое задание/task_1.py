"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

from random import random
from time import time


def duration(func):
    def wrapper(*args, **kvargs):
        start_time = time()
        func(*args, **kvargs)
        print(f'Время выполнения {func.__name__}: {time() - start_time}')
        return func(*args, **kvargs)
    return wrapper


# а)
@duration
def list_add(list_len=1000000):
    list_1 = list()
    for i in range(list_len):  # O(n)
        list_1.append(random())
    return list_1


@duration
def dict_add(list_len=1000000):
    dict_1 = dict()
    for i in range(list_len):  # O(n)
        dict_1[i] = random()
    return dict_1


# b)
@duration
def get_element_from_list(list, position):
    return list[position]  # O(1)


@duration
def get_element_from_dict(dict, key):
    return dict[key]  # O(1)


# с)
@duration
def delete_list_element(list, position):
    list.pop(position)  # O(n)


@duration
def delete_dict_element(dict, key):
    dict.pop(key, None)  # O(1)


if __name__ == '__main__':
    # а)
    list_2 = list_add()
    dict_2 = dict_add()
    # Каждый ключ нужно захешировать, поэтому времени на заполнение словаря уходит больше

    # b)
    list_element = get_element_from_list(list_2, 100)
    dict_element = get_element_from_dict(dict_2, 100)
    # Здесь идет взятие по ключу, поэтому время получения элемента словаря меньше в 2-3 раза

    # c)
    delete_list_element(list_2, 100)
    delete_dict_element(dict_2, 100)
    # Тут сложность O(1), поэтому время удаления элемента словаря меньше
