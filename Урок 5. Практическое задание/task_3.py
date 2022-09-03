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
from timeit import timeit
from collections import deque

# Создание простого списка
simple_lst = [i for i in range(10 ** 5)]

# Создание простой очереди
simple_deq = deque([i for i in range(10 ** 5)])

# Количество итераций в цикле
count = 10 ** 4


# 1. Операции append, pop, extend списка и дека
def append_list(some_list):
    for i in range(count):
        some_list.append(i)
    return some_list


def append_deque(some_deque):
    for i in range(count):
        some_deque.append(i)
    return some_deque


print('-' * 80)
print("сравнение  операции 'append' для list и deque")
print(timeit('append_list(simple_lst.copy())', globals=globals(), number=100))
print(timeit('append_deque(simple_deq.copy())', globals=globals(), number=100))
print('-' * 80)
"""
--------------------------------------------------------------------------------
сравнение  операции 'append' для list и deque
0.168113285
0.169102357
--------------------------------------------------------------------------------
Время выполнения практически совпадает.
"""


def pop_list(some_list):
    for i in range(count):
        some_list.pop()
    return some_list


def pop_deque(some_deque):
    for i in range(count):
        some_deque.pop()
    return some_deque


print('-' * 80)
print("сравнение  операции 'pop' для list и deque")
print(timeit('pop_list(simple_lst.copy())', globals=globals(), number=100))
print(timeit('pop_deque(simple_deq.copy())', globals=globals(), number=100))
print('-' * 80)
"""
--------------------------------------------------------------------------------
сравнение  операции 'pop' для list и deque
0.10021949399999996
0.148273166
--------------------------------------------------------------------------------
Время выполнения практически совпадает.
"""


def extend_list(some_list):
    for i in range(count):
        some_list.extend([1, 2, 3])
    return some_list


def extend_deque(some_deque):
    for i in range(count):
        some_deque.extend([1, 2, 3])
    return some_deque


print('-' * 80)
print("сравнение  операции 'extend' для list и deque")
print(timeit('extend_list(simple_lst.copy())', globals=globals(), number=100))
print(timeit('extend_deque(simple_deq.copy())', globals=globals(), number=100))
print('-' * 80)
"""
--------------------------------------------------------------------------------
сравнение  операции 'extend' для list и deque
0.19849195399999997
0.2596351079999999
--------------------------------------------------------------------------------
Время выполнения операции 'extend' для списка незначительно
меньше, чем у очереди.
"""


# 2. Операции appendleft, popleft, extendleft дека
# и соответствующие им операций списка
def appendleft_list(some_list):
    for i in range(count):
        some_list.insert(0, i)
    return some_list


def appendleft_deque(some_deque):
    for i in range(count):
        some_deque.appendleft(i)
    return some_deque


print('<' * 80)
print("сравнение  операции 'appendleft' для list и deque")
print(timeit('appendleft_list(simple_lst.copy())', globals=globals(), number=100))
print(timeit('appendleft_deque(simple_deq.copy())', globals=globals(), number=100))
print('<' * 80)
"""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
сравнение  операции 'appendleft' для list и deque
62.637138735
0.16679676799999754
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Время выполнения очередью операции 'appendleft' значительно меньше, 
чем у соответствующих ей операций списка.
"""


def popleft_list(some_list):
    for i in range(count):
        some_list.pop(i)
    return some_list


def popleft_deque(some_deque):
    for i in range(count):
        some_deque.popleft()
    return some_deque


print('<' * 80)
print("сравнение  операции 'popleft' для list и deque")
print(timeit('popleft_list(simple_lst.copy())', globals=globals(), number=100))
print(timeit('popleft_deque(simple_deq.copy())', globals=globals(), number=100))
print('<' * 80)
"""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
сравнение  операции 'popleft' для list и deque
33.68706183
0.14237561799998844
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Время выполнения очередью операции 'popleft' значительно меньше, 
чем у соответствующих ей операций списка.
"""


def extendleft_list(some_list):
    for i in range(count):
        some_list.extend([1, 2, 3])
        # some_list.sort()
    return some_list


def extendleft_deque(some_deque):
    for i in range(count):
        some_deque.extendleft([1, 2, 3])
    return some_deque


print('<' * 80)
print("сравнение  операции 'extendleft' для list и deque")
print(timeit('extendleft_list(simple_lst.copy())', globals=globals(), number=100))
print(timeit('extendleft_deque(simple_deq.copy())', globals=globals(), number=100))
print('<' * 80)
"""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
сравнение  операции 'extendleft' для list и deque
0.2038792510000036
0.2554001250000084
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Время выполнения очередью операции 'extendleft' незначительно больше, 
чем у соответствующих ей операций списка. 
"""


# 3. Операции доступа к случайным элементам.
def get_item_list(some_list):
    for i in range(count):
        some_list[i] = i
    return some_list


def get_item_deque(some_deque):
    for i in range(count):
        some_deque[i] = i
    return some_deque


print('~' * 80)
print("сравнение  операций доступа к случайным элементам для list и deque")
print(timeit('get_item_list(simple_lst.copy())', globals=globals(), number=100))
print(timeit('get_item_deque(simple_deq.copy())', globals=globals(), number=100))
print('~' * 80)
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
сравнение  операций доступа к случайным элементам для list и deque
0.09605474700001082
0.2623043819999964
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Список ощутимо быстрее осуществляет доступ к случайному элементу
по сравнению с очередью.
"""
