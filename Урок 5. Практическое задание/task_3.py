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

some_lst = [i for i in range(10 ** 5)]

some_deque = deque([i for i in range(10 ** 5)])

n = 10 ** 4


# 1. операции, равные по смыслу и используемым выражениям
# в списке - append, pop, extend

def append_list(some_lst):
    for i in range(n):
        some_lst.append(i)
    return some_lst


def append_deque(some_deque):
    for i in range(n):
        some_deque.append(i)
    return some_deque


print(timeit('append_list(some_lst.copy())', globals=globals(), number=100))
print(timeit('append_deque(some_deque.copy())', globals=globals(), number=100))
# 0.28035639999999995
# 0.2636795


def pop_list(some_lst):
    for i in range(n):
        some_lst.pop()
    return some_lst


def pop_deque(some_deque):
    for i in range(n):
        some_deque.pop()
    return some_deque


print(timeit('pop_list(some_lst.copy())', globals=globals(), number=100))
print(timeit('pop_deque(some_deque.copy())', globals=globals(), number=100))
# 0.1177974
# 0.14932239999999997


def extend_list(some_lst):
    for i in range(n):
        some_lst.extend([1, 2, 3])
    return some_lst


def extend_list(some_deque):
    for i in range(n):
        some_deque.extend([1, 2, 3])
    return some_deque


print(timeit('extend_list(some_lst.copy())', globals=globals(), number=100))
print(timeit('extend_list(some_deque.copy())', globals=globals(), number=100))
# 0.3577401
# 0.3708876


# 2. операции, равные по смыслу, но отличающиеся по выражениям:
# в деке - appendleft, popleft, extendleft
# в списке - соответствующие им операции списка

def appendleft_list(some_lst):
    for i in range(n):
        some_lst.insert(0, i)
    return some_lst


def appendleft_deque(some_deque):
    for i in range(n):
        some_deque.appendleft(i)
    return some_deque


print(timeit('appendleft_list(some_lst.copy())', globals=globals(), number=100))
print(timeit('appendleft_deque(some_deque.copy())', globals=globals(), number=100))
# 49.1110707
# 0.1969752999999983

def popleft_list(some_lst):
    for i in range(n):
        some_lst.pop(i)
    return some_lst


def popleft_deque(some_deque):
    for i in range(n):
        some_deque.popleft()
    return some_deque


print(timeit('popleft_list(some_lst.copy())', globals=globals(), number=100))
print(timeit('popleft_deque(some_deque.copy())', globals=globals(), number=100))
# 22.3985409
# 0.17606899999999825


def extendleft_list(some_lst):
    for i in range(n):
        some_lst.insert(0, [1, 2, 3])
    return some_lst


def extendleft_deque(some_deque):
    for i in range(n):
        some_deque.extendleft([1, 2, 3])
    return some_deque


print(timeit('extendleft_list(some_lst.copy())', globals=globals(), number=100))
print(timeit('extendleft_deque(some_deque.copy())', globals=globals(), number=100))
# 52.493336199999995
# 0.3010936000000015


# 3. операции доступа к случайным элементам.
# Сделайте замеры и аналитику

def get_elem_list(some_lst):
    for i in range(n):
        some_lst[i] = i
    return some_lst


def get_elem_deque(some_deque):
    for i in range(n):
        some_deque[i] = i
    return some_deque


print(timeit('get_elem_list(some_lst.copy())', globals=globals(), number=100))
print(timeit('get_elem_deque(some_deque.copy())', globals=globals(), number=100))
# 0.1759118
# 0.4197225