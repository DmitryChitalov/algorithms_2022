"""
Задание 1.
Реализуйте:
a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.
b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.
ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

import time


# print('hi')
number = 100000


def dec_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f'Время выполнения функции {func.__name__} \n'
              f'составило {end - start}')
        return result

    return wrapper


@dec_func
def filling_list(lst, n):
    for i in range(n):  # O(n)
        lst.append(i)  # O(1)


some_list = []
filling_list(some_list, number)


@dec_func
def filling_dict(dct, n):
    for i in range(n):  # O(n)
        dct[i] = i  # O(1)


some_dict = {}
filling_dict(some_dict, number)
# print(dct)

'''
время выполнениея filling_list - 0.005984306335449219

время выполнениея filling_dict - 0.007978677749633789
'''

@dec_func
def change_list(lst):
    for i in range(10000):
        lst.pop(i)
    for i in range(1000):
        lst[i] = 'list'


change_list(some_list)

'''
Oперация удаление элемента списка не с конца lst.pop(i) выполняется за O(n), 
а изменеие элемента по индексу O(1)
'''


@dec_func
def change_dict(dct):
    for i in range(10000):
        dct.pop(i)
    for i in range(1000):
        dct[i] = 'dict'


change_dict(some_dict)

'''
Операция удаление элемента из словаря dct.pop(i), также как и изменеие элемента по ключу, 
выполняется за O(1) 
'''


'''
время выполнениея change_list - 0.2104322910308838

время выполнениея change_dict - 0.000997781753540039
'''
