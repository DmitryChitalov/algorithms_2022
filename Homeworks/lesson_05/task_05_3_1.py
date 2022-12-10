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

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from collections import deque
from timeit import timeit


def lst_append(lst, n):
    for i in range(n):
        lst.append(i)


def dq_append(dq, n):
    for i in range(n):
        dq.append(i)


def lst_pop(lst, n):
    for i in range(n):
        lst.pop(-1)


def dq_pop(dq, n):
    for i in range(n):
        dq.pop()


def lst_extend(lst, n):
    for i in range(n):
        lst.extend([i])


def dq_extend(dq, n):
    for i in range(n):
        dq.extend([i])


if __name__ == '__main__':
    lst_test = []
    dq_test = deque()
    n_test = 10000000

    print('Время выполнения метода append')
    print(f"Для списка: {timeit('lst_append(lst_test, n_test)', globals=globals(), number=1)}")
    print(f"Для дека: {timeit('dq_append(dq_test, n_test)', globals=globals(), number=1)}")
    print('Время выполнения метода pop')
    print(f"Для списка: {timeit('lst_pop(lst_test, n_test)', globals=globals(), number=1)}")
    print(f"Для дека: {timeit('dq_pop(dq_test, n_test)', globals=globals(), number=1)}")
    print('Время выполнения метода extend')
    print(f"Для списка: {timeit('lst_extend(lst_test, n_test)', globals=globals(), number=1)}")
    print(f"Для дека: {timeit('dq_extend(dq_test, n_test)', globals=globals(), number=1)}")

# Методы append, pop, extend для списка и дека выполняются за примерно одинаковое время.
