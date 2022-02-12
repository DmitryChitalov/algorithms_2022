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
from time import time


def time_of_function(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        end_time = time()
        print(f'{func.__name__}: {end_time - start_time}')
        return res
    return wrapper


@time_of_function
def fill_dictionary():  # Заполнение словаря
    for i in range(1, 100001):
        my_dictionary[i] = i   # O(1) - Константная


@time_of_function
def fill_list():  # Заполнение списка
    for i in range(1, 100001):
        my_list.append(i)    # O(1) - Константная


@time_of_function
def dict_insert():  # Изменение словаря
    for i in range(1, 50000):
        my_dictionary[i] = 'Cat'    # O(1) - Константная


@time_of_function
def list_insert():  # Изменение списка
    for i in range(50000):
        my_list[i] = my_list[i * 2]     # O(1) - Константная


@time_of_function
def fill_list_pop():  # Удаление из списка
    for i in range(1, 50000):
        my_list.pop(i)  # O(1) - Константная


@time_of_function
def fill_dict_pop():  # Удаление из словаря
    for i in range(1, 50000):
        my_dictionary.pop(i)  # O(1) - Константная


print('Заполнение списка происходит быстрее чем словаря')
my_dictionary = {}
fill_dictionary()
my_list = []
fill_list()
print('Изменение словаря происходит быстрее чем списка')
dict_insert()
list_insert()
print('Удаление элементов из словаря быстрее чем из списка')
fill_list_pop()
fill_dict_pop()


