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
import random

def get_time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        return ('Функция ' + function.__name__ + ' заняла ' + str(time.time() - start_time))
    return wrapped

some_array = []
some_dict = {}

@get_time_of_function
def fill_array():
    global some_array                     # O(1)
    for i in range(1, 101):               # O(1)
        some_array.append('a'*i)          # O(1)
    return                                # O(1)

# Сложность fill_array() = O(1)

@get_time_of_function
def fill_dict():
    global some_dict                      # O(1)
    for i in range(1, 101):               # O(1)
        some_dict['a'*i] = i              # O(1)
    return                                # O(1)

# Сложность fill_dict() = O(1)

@get_time_of_function
def get_array_el(el):
    global some_array                     # O(1)
    for array_el in some_array:           # O(N)
        if array_el == el:                # O(1)
            return el                     # O(1)
    return 'Нет такого элемента'          # O(1)

# Сложность get_array_el() = O(N)

@get_time_of_function
def get_dict_el(el):
    global some_dict                      # O(1)
    for dict_el in some_dict:             # O(N)
        if dict_el == el:                 # O(1)
            return el                     # O(1)
    return 'Нет такого элемента'          # O(1)

# Сложность get_array_el() = O(N)

@get_time_of_function
def delete_array_el(el):
    global some_array                     # O(1)
    for array_el in some_array:           # O(N)
        if array_el == el:                # O(1)
            some_array.remove(array_el)   # O(N)
            return                        # O(1)
    return 'Нет такого элемента'          # O(1)

# Сложность delete_array_el() = O(N^2)

@get_time_of_function
def delete_dict_el(key):
    global some_dict                      # O(1)
    for dict_key in some_dict:            # O(N)
        if dict_key == key:               # O(1)
            del some_dict[dict_key]       # O(N)
            return                        # O(1)
    return 'Нет такого элемента'          # O(1)

# Сложность delete_dict_el() = O(N^2)

print('ПУНКТ А: Сравнение заполнения списка и словаря')
print(fill_array())
print(fill_dict())
el_to_find = 'a' * random.randint(0, 200)
print('ПУНКТ Б: Сравнение получения элемента списка и словаря')
print(get_array_el(el_to_find))
print(get_dict_el(el_to_find))
print('ПУНКТ В: Сравнение удаления элемента списка и словаря')
print(delete_array_el(el_to_find))
print(delete_dict_el(el_to_find))
