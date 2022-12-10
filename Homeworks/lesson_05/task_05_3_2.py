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
соответствует действительности.

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from collections import deque
from timeit import timeit


def lst_insert_left(lst, n):
    for i in range(n-1, -1, -1):
        lst.insert(0, i)


def dq_appendleft(dq, n):
    for i in range(n-1, -1, -1):
        dq.appendleft(i)


def lst_pop_left(lst, n):
    for i in range(n):
        lst.pop(0)


def dq_popleft(dq, n):
    for i in range(n):
        dq.popleft()


def lst_extend_left(lst, n):
    for i in range(n):
        lst.insert(0, [i])


def dq_extendleft(dq, n):
    for i in range(n):
        dq.extendleft([i])


if __name__ == '__main__':
    lst_test = []
    dq_test = deque()
    n_test = 200000

    print('Время выполнения методов insert (слева) и appendleft')
    print(f"insert для списка: {timeit('lst_insert_left(lst_test, n_test)', globals=globals(), number=1)}")
    print(f"appendleft для дека: {timeit('dq_appendleft(dq_test, n_test)', globals=globals(), number=1)}")
    print('Время выполнения методов pop (слева) и popdleft')
    print(f"pop для списка: {timeit('lst_pop_left(lst_test, n_test)', globals=globals(), number=1)}")
    print(f"popleft для дека: {timeit('dq_popleft(dq_test, n_test)', globals=globals(), number=1)}")
    print('Время выполнения аналога метода extendleft для списка и extendleft')
    print(f"Аналог ля списка: {timeit('lst_extend_left(lst_test, n_test)', globals=globals(), number=1)}")
    print(f"extendleft для дека: {timeit('dq_extendleft(dq_test, n_test)', globals=globals(), number=1)}")

# Методы appendleft, popleft, extendleft дека выполняются быстрее, чем аналогичные методы для списка,
# потому что сложность выполнения методов дека О(1).
