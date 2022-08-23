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


def stopwatch(function):

    def wrapper():
        start = time()
        result = function()
        end = time()
        print(f'Время работы: {end - start:.10f}')
        return result
    return wrapper


@stopwatch
def fill_list():   # O(1)
    result_list = []
    for i in range(10 ** 5):
        result_list.append(i)
    return result_list


@stopwatch
def fill_dict():   # O(1)
    result_dict = {}
    for i in range(10 ** 5):
        result_dict.setdefault(i, None)
    return result_dict


res_list = fill_list()
res_dict = fill_dict()
# ------------------------------


@stopwatch
def elem_list():    # O(N)
    for i in range(len(res_list)):
        print(res_list[i], end=' ')


@stopwatch
def val_dict(): # O(N)
    for key in res_dict.keys():
        print(res_dict[key], end=' ')


elem_list()
val_dict()
# ------------------------------


@stopwatch
def del_elem_list():    # O(N)
    for i in range(len(res_list)):
        res_list.remove(i)
    return res_list


@stopwatch
def del_key_val_dict():    # O(N)
    for key in range(len(res_dict.keys())):
        del res_dict[key]


del_elem_list()    # 0.8854355812
del_key_val_dict()    # 0.0156199932
