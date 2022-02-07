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

import time

def count_time(func):
    def wraper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения: {end - start} {return_value}')
        return return_value
    return wraper


@count_time
def fill_dict(dict_name, **kwargs):
    for i, j in kwargs.items():  # O(n)
        dict_name[i] = j  # O(1)
    return dict_name

@count_time
def fill_list(list_name, *args,):
    for i in args:  # O(n)
        list_name.append(i)  # O(1)
    return list_name

dict_1 = {}
list_1 = []

fill_dict(dict_1, **{str(key): key for key in range(10000)})
fill_list(list_1, *(i for i in range(10000)))

@count_time
def delete_elem_list(list_1, elem):  # O(n)
    list_1.remove(elem)
    return list_1

@count_time
def change_elem_list(list_1, index, new_elem):  # O(n)
    for i in index:
        list_1[i] = new_elem
    return list_1

@count_time
def delete_elem_dict(dict_1, dict_key):  # O(1)
    del dict_1[dict_key]
    return dict_1

@count_time
def change_elem_dict(dict_1, dict_key, new_value):  # O(n)
    for i in dict_key:
        dict_1[i] = new_value
    return dict_1
ls_c = [i for i in range(1, 5000)]

change_elem_list(list_1, ls_c, 4000)
change_elem_dict(dict_1, ls_c, 1)

list_2 = delete_elem_list(list_1, 4000)
dict_2 = delete_elem_dict(dict_1, '8000')



'''
Время выполнения операций у списка быстрее чем у словаря,
как мне кажется, у словаря нужно посчитать хэш.

Время замены елементов у словаря немного быстрее, хотя разница
ничтожно мала

Время удаления елемента в словаре быстрее по O-нотации, потомучто
работать с хеш таблицей быстрее
'''













