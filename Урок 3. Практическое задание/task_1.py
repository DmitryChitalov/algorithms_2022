"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно проводить в цикле)
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


def time_decorator(func):
    def time_measurement(*args):
        start = time()
        res_func = func(*args)
        end = time()
        return end - start, res_func

    return time_measurement


'''a) ****************************************'''


@time_decorator
def fill_in_the_list(number):
    res_list = list()
    for i in range(number):
        res_list.append(i)
    return res_list


@time_decorator
def fill_in_the_dictionary(number):
    res_dict = dict()
    for i in range(number):
        res_dict[i] = i
    return res_dict


res_fill = fill_in_the_list(1000000), fill_in_the_dictionary(1000000)
if res_fill[0] > res_fill[1]:
    print(
        f'Скорость заполнения словаря быстрее на {round((res_fill[0][0] - res_fill[1][0]) * 100 / res_fill[0][0], 2)} %')
else:
    print(
        f'Скорость заполнения списка быстрее на {round((res_fill[1][0] - res_fill[0][0]) * 100 / res_fill[1][0], 2)} %')

'''b) ****************************************'''


@time_decorator
def search_through_the_list(number, list_):
    for i in range(number):
        if i in list_:
            pass


@time_decorator
def search_through_the_dict(number, dict_):
    for i in range(number):
        if i in dict_:
            pass


res_search = search_through_the_list(10000, res_fill[0][1]), search_through_the_dict(10000, res_fill[1][1])

if res_search[0] > res_search[1]:
    print(
        f'Скорость поиска по словарю быстрее на {round((res_search[0][0] - res_search[1][0]) * 100 / res_search[0][0], 2)} %')
else:
    print(
        f'Скорость поиска по списку быстрее на {round((res_search[1][0] - res_search[0][0]) * 100 / res_search[1][0], 2)} %')

'''с) ****************************************'''

@time_decorator
def removing_from_the_list(number, list_):
    for i in range(number):
        if i in list_:
            list_.remove(i)


@time_decorator
def removing_from_the_dict(number, dict_):
    for i in range(number):
        if i in dict_:
            del dict_[i]

res_removing = removing_from_the_list(10000, res_fill[0][1]), removing_from_the_dict(10000, res_fill[1][1])
print(res_removing)
'''Удаление из словаря значительно быстрее чем из списка'''