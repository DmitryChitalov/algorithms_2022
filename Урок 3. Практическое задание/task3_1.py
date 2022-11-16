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


def calc_time(func):
    def wrap(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        delta = f"\nFunction: {func.__name__} \ntook: {end_time - start_time}sec \n"
        print(delta)
        return result

    return wrap


@calc_time
def fill_list(stop):   # O(n^2)

    time.sleep(1)  # O(1)
    result = []  # O(1)
    for i in range(1, stop):  # O(n)
        result.append(f"{i} : {chr(i)}")  # (1)
    return result  # O(1)


@calc_time
def fill_dict(stop):
    """
    сложность :
    """
    time.sleep(1)  # O(1)
    result = {}  # O(1)
    for i in range(1, stop):  # O(n)
        result[i] = chr(i)  # O(1)
    return result  # O(1)


filled_list = fill_list(127)
filled_dict = fill_dict(127)


@calc_time
def get_elem_lst(lst: list):
    """
    Сложность : O(n)
    """
    time.sleep(1)
    for i in range(len(lst)):  # O(n)
        elem = lst[i]  # O(1)


@calc_time
def get_elem_dict(dic: dict):
    time.sleep(1)
    for k in dic.keys():  # O(n)
        elem = dic[k]  # O(n)


get_elem_lst(filled_list)
get_elem_dict(filled_dict)


@calc_time
def del_elem_lst(lst: list):
    """
    Сложность : O(n^2)
    """
    time.sleep(1)
    for i in range(len(lst) - 1, -1, -1):  # O(n)
        del lst[i]  # O(n)
    return lst  # O(1)


@calc_time
def del_elem_dict(data: dict):
    time.sleep(1)
    keys = list(data.keys())
    for k in keys:  # O(n)
        del data[k]  # O(1)
    return data


a = del_elem_lst(filled_list)
b = del_elem_dict(filled_dict)