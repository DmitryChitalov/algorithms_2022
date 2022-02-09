from collections import deque
from timeit import timeit

lst_test = [5, 60, 900, 8000, 15000, 350000, 700000]
deq_test = deque('307981456820')

num = 5

""" 3. операции получения элемента списка и дека """
# Список


def get_el_from_lst(lst_test):
    for i in range(num):
        j = lst_test[i]


# Дек


def get_el_from_deq(deq_test):
    for i in range(num):
        j = deq_test[i]


# Замеры времени
print(timeit("get_el_from_lst(lst_test)", globals=globals()))
print(timeit("get_el_from_deq(deq_test)", globals=globals()))

"""
1.0776244000000001
1.1385243
Элементы из списка можно получить быстрее
"""
