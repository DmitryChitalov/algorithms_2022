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

# Заполнение списка
some_lst = [i for i in range(10 ** 5)]

# Заполнение очереди
some_deque = deque([i for i in range(10 ** 5)])

n = 10 ** 4


# 1. операции, равные по смыслу и используемым выражениям
# в списке - append, pop, extend

# append
def append_list(some_lst):
    for i in range(n):
        some_lst.append(i)
    return some_lst


# append
def append_deque(some_deque):
    for i in range(n):
        some_deque.append(i)
    return some_deque


# print(timeit('append_list(some_lst.copy())', globals=globals(), number=100))
# print(timeit('append_deque(some_deque.copy())', globals=globals(), number=100))
# 0.17083706399999998
# 0.17358429199999997


# pop
def pop_list(some_lst):
    for i in range(n):
        some_lst.pop()
    return some_lst


# pop
def pop_deque(some_deque):
    for i in range(n):
        some_deque.pop()
    return some_deque


# print(timeit('pop_list(some_lst.copy())', globals=globals(), number=100))
# print(timeit('pop_deque(some_deque.copy())', globals=globals(), number=100))
# 0.01335096600000002
# 0.013849336999999962


# extend
def extend_list(some_lst):
    for i in range(n):
        some_lst.extend([1, 2, 3])
    return some_lst


# extend
def extend_list(some_deque):
    for i in range(n):
        some_deque.extend([1, 2, 3])
    return some_deque


# print(timeit('extend_list(some_lst.copy())', globals=globals(), number=100))
# print(timeit('extend_list(some_deque.copy())', globals=globals(), number=100))
# 0.24264321900000002
# 0.24306069100000005