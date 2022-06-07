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

from time import time

# декоратор для замеров
def time_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} 'f'составило {end - start}')
        return result
    return timer

# Задание а список
@time_decorator
def fill_list_append(lst, num):
    for i in range(num):
        lst.append(i)  # O(1)

@time_decorator
def fill_list_insert(lst, num):
    for i in range(num):
        lst.insert(0, i)  #O(n)

# Задание а словарь
@time_decorator
def fill_dict(dct, num):
    for i in range(num):
        dct[i] = i  # O(1)

"""
Заполнение списка через метод insert значительно превышает через метод append и заполнение словоря и составляет почти 3 секунды
"""

# Задание b список
@time_decorator
def get_list(lst, start, stop):
    result = []
    for i in range(len(lst)):
        if start < i < stop:
            result.append(i)

# Задание b словарь
@time_decorator
def get_dict(dct, start, stop):
    result = {}
    for i in range(len(dct)):
        if start < i < stop:
            result[i] = i

"""
Получение элемента как списка, так и словоря по заданому индексу/ключу выполняется очень быстро и практически одинаково, так как в обоих случаях О(1)
"""

# Задание c список
@time_decorator
def delete_list(lst, start, stop):
    for i in range(len(lst)):
        if start < i < stop:
            lst.pop(i)

@time_decorator
def delete_dict(dct, start, stop):
    for i in range(len(dct)):
        if start < i < stop:
            dct.pop(i)

"""
Удаление элментов словоря быстрее почти в 10 раз, так как d.pop О(1), в отличии O(n) для l.pop
"""

n = 100000  # число операций
some_list = []
fill_list_append(some_list, n)
print('=' * 100)
some_list = []
fill_list_insert(some_list, n)
print('=' * 100)
some_dict = {}
fill_dict(some_dict, n)
print('=' * 100)
get_list(some_list, 1000, 2000)
print('=' * 100)
get_dict(some_dict, 1000, 2000)
print('=' * 100)
delete_list(some_list, 1000, 2000)
print('=' * 100)
delete_dict(some_dict, 1000, 2000)
print('=' * 100)