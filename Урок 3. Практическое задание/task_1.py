"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
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

import random
import time


def show_time(func):
    def wrapper(*args, **kvargs):
        start_time = time.time()
        func(*args, **kvargs)
        print(f'Time spent for {func.__name__}: {time.time() - start_time}')
        return func(*args, **kvargs)

    return wrapper


# пункт а)
@show_time
def list_filling(list_length=1000000):
    my_list = list()
    for _ in range(list_length):  # O(n)
        my_list.append(random.random())
    return my_list


@show_time
def dict_filling(list_length=1000000):
    my_dict = dict()
    for i in range(list_length):  # O(n)
        my_dict[i] = random.random()
    return my_dict


# пункт b)
@show_time
def get_list_element(list, position):
    return list[position]  # O(1)


@show_time
def get_dict_element(dict, key):
    return dict[key]  # O(1)


# пункт с)
@show_time
def remove_list_element(list, position):
    list.pop(position)  # O(n)


@show_time
def remove_dict_element(dict, key):
    dict.pop(key, None)  # O(1)


if __name__ == '__main__':
    # пункт а)
    lst = list_filling()
    dct = dict_filling()
    # времени на заполнение словаря уходит больше, т.к. каждый ключ нужно захешировать

    # пункт b)
    lst_element = get_list_element(lst, 100)
    dct_element = get_dict_element(dct, 100)
    # время получения элемента словаря меньше в 2-3 раза, т.к идет взятие по ключу

    # пункт c)
    remove_list_element(lst, 200)
    remove_dict_element(dct, 200)
    # время удаления элемента словаря меньше, т.к. сложность O(1) (не нужно сдвигать элементы после удаленного)
