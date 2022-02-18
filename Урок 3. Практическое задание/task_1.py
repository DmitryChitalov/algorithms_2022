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

import time

# декоратор времени


def timeline(func):

    def time_line_2(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'время выполнения {func.__name__} составило {end - start} с')
        return res
    return time_line_2


num_list = []
num_dict = {}

# a)


@timeline
def list_append_a_1(num):
    for i in range(num):
        num_list.append(i)  # O(1)


@timeline
def dict_add_a_2(num):
    for i in range(num):
        num_dict[i] = i  # O(1)


# b)


@timeline
def list_get_value_b_1(num):
    for i in range(num):
        return num_list[i]   # O(1)


@timeline
def dict_get_value_b_2(num):
    for i in range(num):
        return num_dict[i]   # O(1)


# c)


@timeline
def list_pop_1(num):
    for i in range(num):
        return num_list.pop(i)   # O(n)


@timeline
def dict_pop_c_2(num):
    for i in range(num):
        return num_dict.pop(i)   # O(1)


if __name__ == "__main__":
    list_append_a_1(1000000)
    dict_add_a_2(1000000)
    print("_" * 100)
    list_get_value_b_1(1000000)
    dict_get_value_b_2(1000000)
    print("_" * 100)
    list_pop_1(100000)
    dict_pop_c_2(100000)
