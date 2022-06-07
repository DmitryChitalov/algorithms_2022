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

my_list = []
my_dict = {}

# функция декоратор для замера времени выполнения


def timing(f):
    def wrapper(*args):
        start_time = time.time()
        res = f(*args)
        stop_time = time.time()
        print('%sfunction took %0.1f ms' % (f.__name__, (stop_time-start_time) * 1000))
    return wrapper

#Пункт А - сравниваваем наполнение списка и словаря

@timing
def list_filling(massive, num):  # O(n)
    for i in range(num):  # O(n)
        massive.append(i)  # O(1)

@timing
def dict_filling(massive, num):  # O(n)
    for i in range(num):  # O(n)
        massive[i] = i  # O(1)
#
#
print(list_filling(my_list, 100000))
print(dict_filling(my_dict, 100000))
print('Несмотря на одинаковую сложность функции наполнения, словарь заполняется медленнее, \n'
'т.к. у словаря помимо заполнения генерируется хэш')

#Пункт B - сравниваваем чтение списка и словаря

@timing
def list_reading(massive):
    for i in massive: #O(n)
        print(i)  #O(1)
    return massive

@timing
def dict_reading(dictionary):
    for key in dictionary:  # O(n)
        print(dictionary[key])  # O(1)
    return dictionary

print(list_reading(my_list))
print(dict_reading(my_dict))
print('Несмотря на одинаковую сложность функции чтения, скорость считывания данных со словаря быстрее')


# Пункт С - сравнивание скорости удаления

@timing
def dict_pop(dictionary):
    for i in range(10000):    # O(n)
        dictionary.popitem()           # O(1)
    return dictionary


@timing
def list_pop(massive):
    for i in range(len(massive)):   # O(n)
        massive.pop(0)              # O(n)
    return massive


print(list_pop(my_list))
print(dict_pop(my_dict))
print('Удаление элементов словаря происходит быстрее чем у списков')