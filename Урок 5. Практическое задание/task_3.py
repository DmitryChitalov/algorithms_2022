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


lst = [i for i in range(1000)]
deq_lst = deque(lst)

# 1) сравнить операции
# append, pop, extend списка и дека и сделать выводы что и где быстрее


def append_lst(lst):
    for i in range(100):
        lst.append(i)
    return lst


def append_deq_lst(deq_lst):
    for i in range(100):
        deq_lst.append(i)
    return deq_lst

def pop_lst(lst):
    for i in range(10000):
        lst.pop(i)
    return lst


def pop_deq_lst(deq_lst):
    for i in range(10000):
        deq_lst.pop()
    return deq_lst


def extend_lst(lst, lst_2):
    for i in range(100):
        lst.extend(lst_2)
    return lst


def extend_deq_lst(deq_lst, deq_lst_2=deque()):
    for i in range(100):
        deq_lst.extend(deq_lst_2)
    return deq_lst

print(f'append_lst: {timeit("append_lst", globals=globals())}')
print(f'append_deq_lst: {timeit("append_deq_lst", globals=globals())}')
print(f'pop_lst: {timeit("pop_lst", globals=globals())}')
print(f'pop_deq_lst: {timeit("pop_deq_lst", globals=globals())}')
print(f'extend_lst: {timeit("extend_lst", globals=globals())}')
print(f'extend_deq_lst: {timeit("extend_deq_lst", globals=globals())}')

def insert_lst(lst):
    for i in range(1000):
        lst.insert(0, i)
    return lst


def appendleft_deq_lst(deq_lst):
    for i in range(1000):
        deq_lst.appendleft(0, i)
    return deq_lst


def popleft_lst(lst):
    for i in range(1000):
        lst.pop(i)
    return lst


def popleft_deq_lst(deq_lst):
    for i in range(1000):
        deq_lst.popleft()
    return deq_lst


def extendleft_lst(lst, lst_2):
    for i in range(100):
        for i in lst_2:
            lst.insert(0, i)
        return lst_2


def extendleft_deq_lst(deq_lst):
    for i in range(100):
        deq_lst.extendleft(i)
    return deq_lst
print('----------------------')
print(f'insert_lst: {timeit("insert_lst", globals=globals())}')
print(f'appendleft_deq_lst: {timeit("appendleft_deq_lst", globals=globals())}')
print(f'popleft_lst: {timeit("popleft_lst", globals=globals())}')
print(f'popleft_deq_lst: {timeit("popleft_deq_lst", globals=globals())}')
print(f'extendleft_lst: {timeit("extendleft_lst", globals=globals())}')
print(f'extendleft_deq_lst: {timeit("extendleft_deq_lst", globals=globals())}')


def el_from_lst(x):
    for i in range(len(lst)):
        lst[i] = x
    return x


def el_from_deq_lst(x):
    for i in range(len(deq_lst)):
        deq_lst[i] = x
    return x

print('----------------------')
print(f'el_from_lst: {timeit("el_from_lst", globals=globals())}')
print(f'el_from_deq_lst: {timeit("el_from_deq_lst", globals=globals())}')

# append_lst: 0.014657800000000006
# append_deq_lst: 0.013068799999999992
# pop_lst: 0.013780100000000003
# pop_deq_lst: 0.014075900000000002
# extend_lst: 0.013974699999999993
# extend_deq_lst: 0.017900100000000002

# Вывод: нет значительных отличий в срокости выволнения
# ----------------------
# insert_lst: 0.026860999999999996
# appendleft_deq_lst: 0.01492099999999999
# popleft_lst: 0.014394400000000002
# popleft_deq_lst: 0.012977500000000003
# extendleft_lst: 0.014417899999999984
# extendleft_deq_lst: 0.012281199999999992

# Вывод: операции left у дека выполняются быстрее

# ----------------------
# el_from_lst: 0.012214799999999998
# el_from_deq_lst: 0.016683999999999977

# Вывод: извлечение быстрее происходит из списка