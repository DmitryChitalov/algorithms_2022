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


def timer(f):
    def times(*args, **kw):
        t_start = time.time()
        result = f(*args, **kw)
        t_end = time.time()
        print(f'Function execution time {f.__name__} '
              f'equal {t_end - t_start}')
        return result

    return times

@timer
def list_completion():
    l = []
    for i in range(0, 100):
        l.append(i)
    return l                                          # Сложность операции O(n)


lst = list_completion()
print(lst)

@timer
def dict_completion(lst):
    dic = {k: v for k, v in zip(lst, lst)}            # Сложность операции O(n)
    return dic


dic = dict_completion(lst)
print(dic)

@timer
def get_list_item(args):
    lst1 = []
    for i in args:
        if i % 2 == 0:
            lst1.append(i)                            # Сложность операции O(n)
    return lst1


lst1 = get_list_item(lst)
print(lst1)

@timer
def get_dict_item(args):
    dic1 = {}
    for i in args.keys():
        dic1 = dic.items()                              # Сложность операции O(n)
    return dic1


print(get_dict_item(dic))

@timer
def del_list_item(args):
    for i in args:
        args.pop()                                      # Сложность операции O(n)
    return args


print(del_list_item(lst))

@timer
def del_dict_item(dct):
    for i in range(100):
        dct.pop(i)                                      # Сложность операции O(n)
    return dct


print(del_dict_item(dic))


