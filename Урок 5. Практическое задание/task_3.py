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
# в списке и деке - append, pop, extend


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


# print('list:', timeit('append_list(some_lst.copy())', globals=globals(), number=100))
# print('deque:', timeit('append_deque(some_deque.copy())', globals=globals(), number=100))
# list: 0.2861059997230768
# deque: 0.2439724998548627
# Список и дека заполняются практически одинаково по времени, дека чуть быстрее.

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


# print('list:', timeit('pop_list(some_lst.copy())', globals=globals(), number=100))
# print('deque:', timeit('pop_deque(some_deque.copy())', globals=globals(), number=100))
# list: 0.1972974999807775
# deque: 0.31218399992212653
# В операции с удалением через pop список опережает деку практически на 30%.

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


# print('list:', timeit('extend_list(some_lst.copy())', globals=globals(), number=100))
# print('deque:', timeit('extend_list(some_deque.copy())', globals=globals(), number=100))
# list: 0.35137549974024296
# deque: 0.3942803000099957
# Операция вставки через extend у списка идёт чуть быстрее, примерно на 15%.

# 2. операции, равные по смыслу, но отличающиеся по выражениям:
# в деке - appendleft, popleft, extendleft
# в списке - соответствующие им операции списка

# insert
def appendleft_list(some_lst):
    for i in range(n):
        some_lst.insert(0, i)
    return some_lst


# appendleft
def appendleft_deque(some_deque):
    for i in range(n):
        some_deque.appendleft(i)
    return some_deque


# print('list:', timeit('appendleft_list(some_lst.copy())', globals=globals(), number=100))
# print('deque:', timeit('appendleft_deque(some_deque.copy())', globals=globals(), number=100))
# list: 66.48087750002742
# deque: 0.2529855999164283
# Здесь операция insert списка более чем на 2 порядка превышает работу appendleft деки!!!
# Потрясающий результат.

# pop
def popleft_list(some_lst):
    for i in range(n):
        some_lst.pop(i)
    return some_lst


# popleft
def popleft_deque(some_deque):
    for i in range(n):
        some_deque.popleft()
    return some_deque


# print('list:', timeit('popleft_list(some_lst.copy())', globals=globals(), number=100))
# print('deque:', timeit('popleft_deque(some_deque.copy())', globals=globals(), number=100))
# list: 31.948576199822128
# deque: 0.23869509994983673
# Результат тоже на 2 с лишним порядка выше у popleft деки, чем у pop по индексу.
# Тоже потрясающий результат!!!


# insert
def extendleft_list(some_lst):
    for i in range(n):
        some_lst.insert(0, [1, 2, 3])
    return some_lst


# extendleft
def extendleft_deque(some_deque):
    for i in range(n):
        some_deque.extendleft([1, 2, 3])
    return some_deque


# print('list:', timeit('extendleft_list(some_lst.copy())', globals=globals(), number=100))
# print('deque:', timeit('extendleft_deque(some_deque.copy())', globals=globals(), number=100))
# list: 66.2548140999861
# deque: 0.33869760017842054
# Результат примерно тот же, на 2 с лишним порядка выше у insert для списка, чем extendleft для деки.
# Тоже потрясающий результат!!!


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


# print('list:', timeit('get_elem_list(some_lst.copy())', globals=globals(), number=100))
# print('deque:', timeit('get_elem_deque(some_deque.copy())', globals=globals(), number=100))
# list: 0.2049099998548627
# deque: 0.47843110002577305
# Операции получения элемента по индексу примерно в два раза быстрее у списка, чем у деки.

# Вывод: операции общие для списка и деки работают быстрее у списка, а операции присутствующие только для деки на
# порядки быстрее выполняются для неё, по сравнению с аналогичными  у списка.