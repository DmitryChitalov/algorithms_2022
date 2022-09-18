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
"""
from time import time

def time_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        res_tim = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} - {round(end - start, 4)}')
        return res_tim
    return timer

@time_decorator
def list_ap(el):  # O(n)
    lst = []  # O(1)
    for i in range(el):  # O(n)
        lst.append(i)  # O(1)
    return lst  # O(1)

@time_decorator
def list_ins(el):  # O(n)
    lst = []  # O(1)
    for i in range(el):  # O(n)
        lst.insert(0, i)  # O(n)
    return lst  # O(1)

@time_decorator
def dict_write(el):  # O(n)
    res_dict = {}
    for i in range(el):  # O(n)
        res_dict[i] = i * 2  # O(1)
    return res_dict  # O(1)

@time_decorator
def list_change(my_lst):  # O(n)
    for i in range(len(my_lst)):  # O(n)
        my_lst[i] += 1  # O(1)

@time_decorator
def dict_change(my_dict):  # o(n)
    for key in my_dict.keys():  # O(n)
        my_dict[key] += 1  # O(1)

@time_decorator
def list_del(my_lst):  # O(n)
    if len(my_lst) > 40:  # O(1)
        for i in range(20):  # O(n)
            my_lst.pop(i)  # O(n)

@time_decorator
def dict_del(my_dict):  # O(n)
    if len(my_dict) > 20:  # O(1)
        for key in range(20):  # O(n)
            my_dict.pop(key)  # O(1)

if __name__ == '__main__':
    only_elem = 10 ** 5
    rez_list_ap = list_ap(only_elem)
    print('')
    rez_list_ins = list_ins(only_elem)
    print('')
    rez_dict = dict_write(only_elem)
    print('')
    list_change(rez_list_ap)
    print('')
    dict_change(rez_dict)
    print('')
    list_del(rez_list_ap)
    print('')
    dict_del(rez_dict)

# Быстрее всего заполняется список, используя append, т.к. добавляется один элемент.
# Чуть медленнее идет заполнение словаря, т.к. добавляется несколько элементов.
# Медленнее всего заполняется список, используя insert, т.к. его сложность О(n).

# Изменение словаря происходит быстрее, чем изменение списка.

# Удаление элементов из списка происходит медленнее, чем удаление элементов словаря,
# т.к.  сложность list.pop = O(n), dict.pop=O(1)