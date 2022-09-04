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

lst = [i for i in range(10000)]
deq = deque(lst)


def lst_append():
    for i in range(1000):
        lst.append(i)


def deque():
    for i in range(1000):
        deq.append(i)


def pop_lst():
    for i in range(1000):
        lst.pop()


def pop_deq():
    for i in range(1000):
        deq.pop()


def lst_extend():
    ext = [i for i in range(1000)]
    lst.extend(ext)


def deq_extend():
    ext = [i for i in range(1000)]
    deq.extend(ext)


print(timeit("lst_append()", globals=globals(), number=1000))
print(timeit("deque()", globals=globals(), number=1000))
print(timeit("pop_lst()", globals=globals(), number=1000))
print(timeit("pop_deq()", globals=globals(), number=1000))
print(timeit("lst_extend()", globals=globals(), number=1000))
print(timeit("deq_extend()", globals=globals(), number=1000))


'''
1) Операции append, pop, extend списка и дека занимают примерно одно и то же время
2) Операции lst_append, pop_lst, lst_extend выполняются гораздо быстрее в Деке
3) Операции получения элемента списка выполняются заметно быстрее, чем те же операции в Деке
'''