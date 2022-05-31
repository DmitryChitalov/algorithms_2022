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

n = 10 ** 4
somedata1 = [i for i in range(n)]
somedata2 = deque([i for i in range(n)])


def append_list(some_lst):
    for i in range(n):
        some_lst.append(i)
    return some_lst


def append_deque(some_deque):
    for i in range(n):
        some_deque.append(i)
    return some_deque


def append_deque_left(some_deque):
    for i in range(n):
        some_deque.appendleft(i)
    return some_deque


print(timeit('append_list(somedata1.copy())', globals=globals(), number=100))
print(timeit('append_deque(somedata2.copy())', globals=globals(), number=100))
print("append_deque_left %f" % (timeit('append_deque_left(somedata2.copy())', globals=globals(), number=100)))
"""

"""


def pop_list(some_lst):
    for i in range(n):
        some_lst.pop()
    return some_lst


def pop_deque(some_deque):
    for i in range(n):
        some_deque.pop()
    return some_deque


def pop_deque_left(some_deque):
    for i in range(n):
        some_deque.popleft()
    return some_deque


print(timeit('pop_list(somedata1.copy())', globals=globals(), number=100))
print(timeit('pop_deque(somedata2.copy())', globals=globals(), number=100))
print("pop_deque_left %f" % (timeit('pop_deque_left(somedata2.copy())', globals=globals(), number=100)))
"""

"""


def extend_list(some_lst):
    for i in range(n):
        some_lst.extend([1])
    return some_lst


def extend_deque(some_deque):
    for i in range(n):
        some_deque.extend([1])
    return some_deque


def extend_deque_left(some_deque):
    for i in range(n):
        some_deque.extendleft([1])
    return some_deque


print(timeit('extend_list(somedata1.copy())', globals=globals(), number=100))
print(timeit('extend_deque(somedata2.copy())', globals=globals(), number=100))
print("extend_deque_left %f" % (timeit('extend_deque_left(somedata2.copy())', globals=globals(), number=100)))


def get_list(some_lst):
    for i in range(n):
        x = some_lst[i]
    return some_lst


def get_deque(some_deque):
    for i in range(n):
        x = some_deque[i]
    return some_deque

print(timeit('get_list(somedata1.copy())', globals=globals(), number=100))
print(timeit('get_deque(somedata2.copy())', globals=globals(), number=100))

"""
[append]
0.14784370000000002
0.185425
append_deque_left 0.177558
Самый быстрый список, потом appendleft и самый медленный append.

[pop]
0.12604100000000007
0.1284938000000001
pop_deque_left 0.128439
Самый быстрый опять же список, потом popleft и pop.

[extend]
0.17137979999999997
0.1878761
extend_deque_left 0.210228
Самый быстрый список, extend, extendleft.

[get item]
0.03490939999999998 (index)
0.06899759999999999 (deque pop)
0.0863893 (deque index)

append и extend примерно одинаковы
extendleft работает медленнее чем appendleft
список лучше чем всё, во всём
"""
