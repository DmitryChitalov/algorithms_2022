from collections import deque
from timeit import timeit

lst_test = [5, 60, 900]
deq_test = deque('307981456820')

num = 50

""" 1. append, pop, extend списка и дека """
# Список


def append_to_lst(lst_test):
    for i in range(num):
        lst_test.append(i)
    return lst_test


def pop_from_lst(lst_test):
    for i in range(num):
        lst_test.pop()
    return lst_test


def extend_lst(lst_test):
    for i in range(num):
        lst_test.extend([1, 9])
    return lst_test

# Дек


def append_to_deq(deq_test):
    for i in range(num):
        deq_test.append(i)
    return deq_test


def pop_from_deq(deq_test):
    for i in range(num):
        deq_test.pop()
    return deq_test


def extend_deq(deq_test):
    for i in range(num):
        deq_test.extend([1, 9])
    return deq_test


# Замеры времени
print(timeit("append_to_lst(lst_test)", globals=globals()))
print(timeit("append_to_deq(deq_test)", globals=globals()))
print(timeit("pop_from_lst(lst_test)", globals=globals()))
print(timeit("pop_from_deq(deq_test)", globals=globals()))
print(timeit("extend_lst(lst_test)", globals=globals()))
print(timeit("extend_deq(deq_test)", globals=globals()))

"""
7.4964883
5.782048
Операции добавления элементов в конец дека производятся быстрее

6.7843208
5.6018498
Операции удаления элементов из дека производятся быстрее

12.801383099999999
14.473382200000003
Операции по вставке списка в конец дека производятся медленнее
"""
