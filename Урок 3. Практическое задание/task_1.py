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
from random import randint
from time import time

def measure_time(f):
    def measuring(*args):
        start = time()
        f_return = f(*args)
        end = time()
        print(f'{f.__name__} \n{end - start}')
        return f_return
    return measuring



@measure_time
def list_creation(n):
    lst = [randint(0, 10000) for i in range(n)] # не нашел для list comprehension. Предполагаю,что O(n) т.к. есть for i in range
    return lst

@measure_time
def dict_creation(n):
    dct = {key: randint(0, 10000) for key in range(n)} # : Предполагаю,что также O(n) как в случае с list comprehension
    return dct


lst = list_creation(10)
dct = dict_creation(10)


@measure_time
def get_from_list(lst):
    for i in range(len(lst)): # O(n) если без цикла для одного элемента, то О(1)
        print(f'{lst[i]},', end=' ')

    return None

@measure_time
def get_from_dict(dct): # O(n) если без цикла для одного элемента, то О(1)
    for key, val in dct.items():
        print(f'{key}: {dct[key]},', end=' ')
    return None


get_from_list(lst)
get_from_dict(dct)

@measure_time
def del_from_list(lst):
    for i in range(len(lst)): #О(n)
        lst.pop() #O(1)
    return None

@measure_time
def del_from_dict(dct):
    dct_lst = [] #O(1)
    for key in dct.keys(): #О(n)
        dct_lst.append(key)  #O(1)
    for i in range(len(dct_lst)): #О(n)
        dct.pop(dct_lst[i]) #O(1)
    return None


del_from_list(lst)
del_from_dict(dct)