"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit

my_lst = [i for i in range(10 ** 5)]

dq = deque([i for i in range(10 ** 5)])
n = 10 ** 4


# 1. append, pop, extend
# append
def append_list(my_lst):
    for i in range(n):
        my_lst.append(i)
    return my_lst


def append_dq(dq):
    for i in range(n):
        dq.append(i)
    return dq


print(timeit('append_list(my_lst.copy())', globals=globals(), number=100))
print(timeit('append_dq(dq.copy())', globals=globals(), number=100))


# pop
def pop_list(my_lst):
    for i in range(n):
        my_lst.pop()
    return my_lst


def pop_dq(dq):
    for i in range(n):
        dq.pop()
    return dq


print(timeit('pop_list(my_lst.copy())', globals=globals(), number=100))
print(timeit('pop_dq(dq.copy())', globals=globals(), number=100))


# extend
def extend_list(my_lst):
    for i in range(n):
        my_lst.extend([1])
    return my_lst


def extend_dq(dq):
    for i in range(n):
        dq.extend([1])
    return dq


print(timeit('extend_list(my_lst.copy())', globals=globals(), number=100))
print(timeit('extend_dq(dq.copy())', globals=globals(), number=100))


# 2. appendleft, popleft, extendleft
# appedleft
def appendleft_list(my_lst):
    for i in range(n):
        my_lst.append(i)
    return my_lst


def appendleft_dq(dq):
    for i in range(n):
        dq.appendleft(i)
    return dq


print(timeit('appendleft_list(my_lst.copy())', globals=globals(), number=100))
print(timeit('appendleft_dq(dq.copy())', globals=globals(), number=100))


# popleft
def popleft_list(my_lst):
    for i in range(n):
        my_lst.pop(i)
    return my_lst


def popleft_dq(dq):
    for i in range(n):
        dq.popleft()
    return dq


print(timeit('popleft_list(my_lst.copy())', globals=globals(), number=100))
print(timeit('popleft_dq(dq.copy())', globals=globals(), number=100))


# extendleft
def extendleft_list(my_lst):
    for i in range(n):
        my_lst.extend([1])
    return my_lst


def extendleft_dq(dq):
    for i in range(n):
        dq.extendleft([1])
    return dq


print(timeit('extendleft_list(my_lst.copy())', globals=globals(), number=100))
print(timeit('extendleft_dq(dq.copy())', globals=globals(), number=100))


# 3.
def get_elem_list(my_lst):
    for i in range(n):
        my_lst[i] = i
    return my_lst


def get_elem_dq(dq):
    for i in range(n):
        dq[i] = i
    return dq


print(timeit('get_elem_list(my_lst.copy())', globals=globals(), number=100))
print(timeit('get_elem_dq(dq.copy())', globals=globals(), number=100))
