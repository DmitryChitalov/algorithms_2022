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

num = range(1000)
lst = [i for i in num]
dq = deque(lst)


# 1)


# append

def list_append():
    for i in num:
        lst.append(i)


def deque_append():
    for i in num:
        dq.append(i)


print('append:')
print(f'list: {timeit("list_append()", globals=globals(), number=1000)}')
print(f'deque: {timeit("deque_append()", globals=globals(), number=1000)}')


# pop

def list_pop():
    for _ in num:
        lst.pop()


def deque_pop():
    for _ in num:
        dq.pop()


print('pop:')
print(f'list: {timeit("list_pop()", globals=globals(), number=1000)}')
print(f'deque: {timeit("deque_pop()", globals=globals(), number=1000)}')


# extend

def list_extend():
    for _ in num:
        lst.extend([i for i in range(10)])


def deque_extend():
    for _ in num:
        dq.extend([i for i in range(10)])


print('extend:')
print(f'list: {timeit("list_extend()", globals=globals(), number=1000)}')
print(f'deque: {timeit("deque_extend()", globals=globals(), number=1000)}')


# операции append, pop, extend списка и дека выполняются одинаково по времени


# 2)


# appendleft

def list_appendleft():
    for i in range(100):
        lst.insert(0, i)


def deque_appendleft():
    for i in range(100):
        dq.appendleft(i)


print('appendleft:')
print(f'list: {timeit("list_appendleft()", globals=globals(), number=10)}')
print(f'deque: {timeit("deque_appendleft()", globals=globals(), number=10)}')


# popleft

def list_popleft():
    for _ in range(100):
        lst.pop(0)


def deque_popleft():
    for _ in range(100):
        dq.popleft()


print('popleft:')
print(f'list: {timeit("list_popleft()", globals=globals(), number=10)}')
print(f'deque: {timeit("deque_popleft()", globals=globals(), number=10)}')


# extendleft

def list_extendleft():
    for _ in range(100):
        for i in range(10):
            lst.insert(0, i)


def deque_extendleft():
    for _ in range(100):
        dq.extendleft([i for i in range(10)])


print('extendleft:')
print(f'list: {timeit("list_extendleft()", globals=globals(), number=10)}')
print(f'deque: {timeit("deque_extendleft()", globals=globals(), number=10)}')


# appendleft, popleft, extendleft у дека выполняются гораздо быстрее, чем аналоги у списка


# 3)


def list_set():
    for i in num:
        lst[i] = 0


def deque_set():
    for i in num:
        dq[i] = 0


print('set:')
print(f'list: {timeit("list_set()", globals=globals(), number=1000)}')
print(f'deque: {timeit("deque_set()", globals=globals(), number=1000)}')


# получения элементов у списка выполняются быстрее
