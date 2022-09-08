from timeit import timeit
from collections import deque

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

lst = [i for i in range(1, 100000)]
deq = deque([i for i in range(1, 100000)])


# 1) Операции append, pop, extend.
# -append

to_lst = []
def lst_append():
    for i in lst:
        to_lst.append(i)
    return to_lst


to_deque = deque([])
def deque_append():
    for i in deq:
        to_deque.append(i)
    return to_deque


# print(timeit('lst_append()', globals=globals(), number=1000))
# print(timeit('deque_append()', globals=globals(), number=1000))

"""При сравнении функции append получаетм примерно одинаковое время выполнения."""



# -pop

def pop_lst():
    for i in to_lst:
        to_lst.pop()
    return to_lst


def pop_deque():
    for i in to_deque:
        to_deque.pop()
    return to_deque

# print(timeit('pop_lst()', globals=globals(), number=1000000))
# print(timeit('pop_deque()', globals=globals(), number=1000000))

"""При сравнении функции pop получаетм примерно одинаковое время выполнения."""

# extend
def extend_lst():
    for i in range(100000):
        to_lst.extend([1, 2, 3])
    return to_lst

def extend_deque():
    for i in range(100000):
        to_deque.extend([1, 2, 3])
    return to_deque


# print(timeit('extend_lst()', globals=globals(), number=100))
# print(timeit('extend_deque()', globals=globals(), number=100))

"""При сравнении функции extend получаем примерно одинаковое время выполнения 
(для списка незначительно меньшее время)."""


#  2) Операции appendleft, popleft, extendleft дека и соответствующие им операций списка
# -apendleft
def appendleft_lst():
    for i in range(1000):
        to_lst.insert(0, i)
    return to_lst


def appendleft_deque():
    for i in range(1000):
        to_deque.appendleft(i)
    return to_deque


# print(timeit('appendleft_lst()', globals=globals(), number=100))
# print(timeit('appendleft_deque()', globals=globals(), number=100))

"""При сравнении функции appedleft получаем значительно более высокую скорость выполнения
у дека."""

#- popleft


def popleft_lst():
    for i in range(100):
        lst.pop(i)
    return lst


def popleft_deque():
    for i in range(100):
        deq.popleft()
    return deq


# print(timeit('popleft_lst()', globals=globals(), number=100))
# print(timeit('popleft_deque()', globals=globals(), number=100))


"""Время выполнения очередью операции popleft значительно меньше, чем у 
соответствующей ей операции списка."""

# -extendleft

def extendleft_lst():
    for i in range(10000):
        to_lst.extend([1, 2, 3])
    return to_lst

def extendleft_deq():
    for i in range(10000):
        to_deque.extendleft([1, 2, 3])
    return to_deque

# print(timeit('extendleft_lst()', globals=globals(), number=1000))
# print(timeit('extendleft_deq()', globals=globals(), number=1000))

"""При сравнении функции extendleft получаем незначительно более высокую скорость выполнения
у дека."""

#  3) Операции доступа к случайным элементам.
lst_2 = [i for i in range(1, 100000)]
deq_2 = deque([i for i in range(1, 100000)])

def get_elem_lst():
    for i in range(2):
        lst_2[i] = i
    return lst_2
#
#
def get_elem_deque():
    for i in range(2):
        deq_2[i] = i
    return deq_2

print(timeit('get_elem_lst()', globals=globals(), number=1000))
print(timeit('get_elem_deque()', globals=globals(), number=1000))


""" Список гораздо быстрее осуществляет операции доступа к случайным элементам
по сравнению с очередью. """