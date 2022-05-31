"""
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
"""
from random import randint
from timeit import timeit
from collections import deque

lst = [i for i in range(10 ** 6)]
deq = deque(lst)


def append_left_lst():
    for i in range(100):
        lst.insert(0, i)


def append_left_deq():
    for i in range(100):
        deq.appendleft(i)


print(timeit(append_left_lst, number=100))  # 3.46
print(timeit(append_left_deq, number=100))  # 0.0004


def pop_left_lst():
    for i in range(100):
        lst.pop(0)


def pop_left_deq():
    for i in range(100):
        deq.popleft()


print(timeit(pop_left_lst, number=100))  # 4.01
print(timeit(pop_left_deq, number=100))  # 0.0003


def extend_left_lst(my_lst):
    for i in range(100):
        my_lst.insert(0, [randint(1, 50) for _ in range(5)])


def extend_left_deq():
    for i in range(100):
        deq.extendleft([randint(1, 50) for _ in range(5)])


print(timeit('extend_left_lst(lst)', globals=globals(), number=100))  # 3.49
print(timeit(extend_left_deq, number=100))  # 0.03

# Во всех случаях выигрывают операции с deque

"""
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
"""


def get_val_lst():
    for i in range(1000):
        lst[i] = i


def get_val_deq():
    for i in range(1000):
        deq[i] = i


print(timeit(get_val_lst, number=10000))  # 0.3
print(timeit(get_val_deq, number=10000))  # 0.5

# Получение элемента списка быстрее, чем у deque
