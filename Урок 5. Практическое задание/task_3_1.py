"""
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
"""
from random import randint
from timeit import timeit
from collections import deque

lst = [i for i in range(10 ** 6)]
deq = deque(lst)


def append_lst():
    for i in range(1000):
        lst.append(i)


def append_deq():
    for i in range(1000):
        deq.append(i)


print(timeit(append_lst, number=10000))  # 0.43
print(timeit(append_deq, number=10000))  # 0.42


def pop_lst():
    for i in range(1000):
        lst.pop()


def pop_deq():
    for i in range(1000):
        deq.pop()


print(timeit(pop_lst, number=10000))  # 0.43
print(timeit(pop_deq, number=10000))  # 0.42


def extend_lst():
    for i in range(1000):
        lst.extend([randint(1, 50) for _ in range(5)])


def extend_deq():
    for i in range(1000):
        deq.extend([randint(1, 50) for _ in range(5)])


print(timeit(extend_lst, number=1000))  # 3.3
print(timeit(extend_deq, number=1000))  # 3.3

# В целом всё +/- одинаково
