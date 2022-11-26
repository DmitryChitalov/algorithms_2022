"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

from random import shuffle
from time import time

# def time_checker(*args, **kwargs):
#     def wrapper(func):
#         start = time()
#         func(*args, **kwargs)
#         end = time()
#         return func, end - start
#     return wrapper

def sort_quadro(lst: list):
    '''функция поиска минимального числа в списке
        с квадратичной сложностью алгоритма'''
    res = lst[0]
    for el in lst:

        for el_check in lst:
            flag = False
            if el < el_check:
                flag = True
            if flag and el < res:
                res = el
    return res


def sort_line(lst: list):
    '''функция поиска минимального числа в списке
    с линейной сложностью алгоритма'''
    res = lst[0]
    for el in lst:
        if res > el:
            res = el
    return res


find_min_lst = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
find_list_2 = [x for x in range(10000)]
shuffle(find_min_lst)
shuffle(find_list_2)

print(sort_line(find_min_lst))
print(sort_quadro(find_min_lst))
print(sort_line(find_list_2))
print(sort_quadro(find_list_2))