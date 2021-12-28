"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

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
(append, pop и т.д.) проводить в циклах
"""
from collections import deque
from random import randint, sample
from timeit import timeit

list_1 = [randint(0, 10000) for i in range(10000)]

deque_1 = deque([randint(0, 10000) for j in range(10000)])


# 1) сравнить операции  append, pop, extend


def list_app(list_1):
    for i in range(1000):
        list_1.append(i)
    return list_1


def deque_app(deque_1):
    for i in range(1000):
        deque_1.append(i)
    return deque_1


print(timeit("list_app(list_1)", globals=globals(), number=1000))  # 0.0583916
print(timeit("deque_app(deque_1)", globals=globals(), number=1000))  # 0.04081199999999999 - немного быстрее, чем list


def list_pop(list_1):
    for i in range(1000):
        list_1.pop()
    return list_1


def deque_pop(deque_1):
    for i in range(1000):
        deque_1.pop()
    return deque_1


print(timeit("list_pop(list_1)", globals=globals(), number=1000))  # 0.03890349999999998
print(timeit("deque_pop(deque_1)", globals=globals(), number=1000))  # 0.035758399999999996 - почти одинаково с list

lst = [i for i in range(10)]


def list_extend(list_1):
    for i in range(1000):
        list_1.extend(lst)
    return list_1


def deque_extend(deque_1):
    for i in range(1000):
        deque_1.extend(lst)
    return deque_1


print(timeit("list_extend(list_1)", globals=globals(), number=1000))  # 0.21735469999999998
print(timeit("deque_extend(deque_1)", globals=globals(), number=1000))  # 0.11559010000000003 - немного быстрее, чем list


# 2) сравнить операции
# appendleft, popleft, extendleft дека и соответствующих им операций списка


def deque_appendleft(deque_1):
    for i in range(1000):
        deque_1.appendleft(i)
    return deque_1


def list_insert(list_1):
    for i in range(1000):
        list_1.insert(0, i)
    return list_1


print(timeit("deque_appendleft(deque_1)", globals=globals(),
             number=10))  # 0.00036290000000005485 - существенно быстрее, чем insert
print(timeit("list_insert(list_1)", globals=globals(), number=10))  # 73.1648253


def deque_popleft(deque_1):
    for i in range(1000):
        deque_1.popleft()
    return deque_1


def list_pop_2(list_1):
    for i in range(1000):
        list_1.pop(i)
    return list_1


print(timeit("deque_popleft(deque_1)", globals=globals(),
             number=10))  # 0.00029489999999998684 - существенно быстрее, чем list
print(timeit("list_pop_2(list_1)", globals=globals(), number=10))  # 58.4558373


def deque_extendleft(deque_1):
    for i in range(1000):
        deque_1.extendleft(lst)
    return deque_1


def list_ins(list_1):
    for i in range(1000):
        list_1.insert(0, lst)
    return list_1


# print(timeit("deque_extendleft(deque_1)", globals=globals(),
#              number=10))  # 0.0011176000000000519 - существенно быстрее, чем list
# print(timeit("list_ins(list_1)", globals=globals(), number=10))  # 72.6376191


# 3) сравнить операции получения элемента списка и дека
# и сделать выводы что и где быстрее

def list_index(list_1):
    random_index = sample(list_1, 50)
    return random_index


def deque_index(deque_1):
    random_index = sample(deque_1, 50)
    return random_index


print(timeit("list_index(list_1)", globals=globals(),
             number=10))  # 0.00036720000000001196 - быстрее, чем deque
print(timeit("deque_index(deque_1)", globals=globals(), number=10))  # 0.9974212000000001
