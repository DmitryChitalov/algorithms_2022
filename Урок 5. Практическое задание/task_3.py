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

n = 10000
my_lst = []
my_deq = deque(my_lst)


def append_lst(some_lst):
    for i in range(n):
        some_lst.append(i)


def append_deq(some_deq):
    for i in range(n):
        some_deq.append(i)


print(timeit('append_lst(my_lst)', globals=globals(), number=100))
print(timeit('append_deq(my_deq)', globals=globals(), number=100))
"""
append быстрее работает в deq, чем в list
"""


def pop_lst(some_lst):
    for i in range(n):
        some_lst.pop()


def pop_deq(some_deq):
    for i in range(n):
        some_deq.pop()


print(timeit('pop_lst(my_lst)', globals=globals(), number=100))
print(timeit('pop_deq(my_deq)', globals=globals(), number=100))

"""
pop работает в deq примерно с такой же скоростью как в list
"""


def extend_lst(some_lst):
    for i in range(n):
        some_lst.extend([1, 2, 3, 4])


def extend_deq(some_deq):
    for i in range(n):
        some_deq.extend([1, 2, 3, 4])


print(timeit('extend_lst(my_lst)', globals=globals(), number=100))
print(timeit('extend_deq(my_deq)', globals=globals(), number=100))

"""
extend в list работает значительно быстрее чем в deq
"""

n = 100


def insert_lst(some_lst):
    for i in range(n):
        some_lst.insert(0, i)


def appendleft_deq(some_deq):
    for i in range(n):
        some_deq.appendleft(i)


print(timeit('insert_lst(my_lst)', globals=globals(), number=50))
print(timeit('appendleft_deq(my_deq)', globals=globals(), number=50))

"""
appendleft в deq работает значительно быстрее чем в list
"""


def popleft_lst(some_lst):
    for i in range(n):
        some_lst.pop(i)


def popleft_deq(some_deq):
    for i in range(n):
        some_deq.popleft()


print(timeit('popleft_lst(my_lst)', globals=globals(), number=100))
print(timeit('popleft_deq(my_deq)', globals=globals(), number=100))

"""
popleft в deq работает значительно быстрее чем в list
"""


def extendleft_lst(some_lst):
    for i in range(n):
        some_lst.extend([1, 2, 3, 4])
        some_lst.sort()


def extendleft_deq(some_deq):
    for i in range(n):
        some_deq.extendleft([1, 2, 3, 4])

#
# print(timeit('extendleft_lst(my_lst)', globals=globals(), number=100))
# print(timeit('extendleft_deq(my_deq)', globals=globals(), number=100))

"""
extendleft в deq работает значительно быстрее чем в list
"""


def get_elem_lst(some_lst):
    for i in range(n):
        some_lst[i] = i
    return some_lst


def get_elem_deq(some_deq):
    for i in range(n):
        some_deq[i] = i
    return some_deq


print(timeit('get_elem_lst(my_lst)', globals=globals(), number=100))
print(timeit('get_elem_deq(my_deq)', globals=globals(), number=100))


"""
получение элемента в списке быстрее чем в деке
"""
