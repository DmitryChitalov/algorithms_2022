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

import time

# Декоратор
def time_counter(func):
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        finish = time.perf_counter()
        print(f'Time "{func.__name__}": {finish - start}.')
        return result
    return wrapper


# a) Спискок не выполняет хеширование и заполняется быстрее.
@time_counter
def fill_list(lst=[]):     # O(n)
    for i in range(10000): # O(n)
        lst.append(i)      # O(1)

@time_counter
def fill_dict(dct={}):     # O(n)
    for i in range(10000): # O(n)
        dct[i] = str(i)    # O(1)

fill_list()
fill_dict()


# b) Почти одинаково, видимо потому что элементы перебираются в цикле.
test_list = []
test_dict = {}

for i in range(10000):
    test_list.append(i)
    test_dict[i] = str(i)

@time_counter
def get_elem_from_list(lst, n):  # О(n)
    for i in lst:                # О(n)
        if i == n:               # О(n)
            return lst[i]        # О(n)

@time_counter
def get_elem_from_dict(dct, n):  # O(n)
    for key in dct:              # O(n)
        if key == n:             # О(1)
            return dct[key]      # O(1)

get_elem_from_list(test_list, 1000)
get_elem_from_dict(test_dict, 1000)


# c) Минимальная разница, видимо потому что элементы перебираются в цикле.
@time_counter
def remove_elem_from_list(lst=[]):  # O(n)
    for i in range(len(lst)):       # O(n)
        lst.pop()                   # O(1)


@time_counter
def remove_elem_from_dict(dct={}):  # O(n)
    for i in range(len(dct)):       # O(n)
        del dct[i]                  # O(1)


remove_elem_from_list(test_list)
remove_elem_from_dict(test_dict)