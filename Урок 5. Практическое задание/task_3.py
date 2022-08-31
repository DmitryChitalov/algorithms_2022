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

lst = [i for i in range(10000)]
deq = deque(lst)


def appnd_lst():
    for i in range(1000):
        lst.append(i)


def deq_appnd():
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


print(timeit("appnd_lst()", globals=globals(), number=1000))
print(timeit("deq_appnd()", globals=globals(), number=1000))
print(timeit("pop_lst()", globals=globals(), number=1000))
print(timeit("pop_deq()", globals=globals(), number=1000))
print(timeit("lst_extend()", globals=globals(), number=1000))
print(timeit("deq_extend()", globals=globals(), number=1000))

"""
Вывод: операции примерно равны по скорости. Есть небольшая погрешность
"""

def lst_left():
    for i in range(1):
        lst.insert(0, i)


def deq_left():
    for i in range(1):
        deq.appendleft(i)


def lst_pop_left():
    for i in range(1):
        lst.pop(0)


def deq_pop_left():
    for i in range(1):
        deq.popleft()


def ext_left_lst():
    ext = [i for i in range(1)]
    lst.insert(0, ext)


def ext_left_deq():
    ext = [i for i in range(1)]
    deq.extendleft(ext)


print(timeit("lst_left()", globals=globals(), number=1000))
print(timeit("deq_left()", globals=globals(), number=1000))
print(timeit("lst_pop_left()", globals=globals(), number=1000))
print(timeit("deq_pop_left()", globals=globals(), number=1000))
print(timeit("ext_left_lst()", globals=globals(), number=1000))
print(timeit("ext_left_deq()", globals=globals(), number=1000))

"""
Вывод: в этих случаях операции с деком значительно быстрее!
"""

def get_from_lst():
    for i in range(1000):
        lst[i]


def get_from_deq():
    for i in range(1000):
        deq[i]


print(timeit("get_from_lst()", globals=globals(), number=1000))
print(timeit("get_from_deq()", globals=globals(), number=1000))

"""
Вывод: в этих случаях операции со списком значительно быстрее!
"""

