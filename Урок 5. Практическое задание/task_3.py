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

list_x = [i for i in range(7777)]
deque_x = deque([i for i in range(7777)])
n = 999

# 1


def append(x):
    for i in range(n):
        x.append(i)
    return x


def pop(x):
    for i in range(n):
        x.pop()
    return x


def extend(x):
    for i in range(n):
        x.extend([1, 2, 3])
    return x


print(timeit('append(list_x.copy())', globals=globals(), number=100))
print(timeit('append(deque_x.copy())', globals=globals(), number=100))
print(timeit('pop(list_x.copy())', globals=globals(), number=100))
print(timeit('pop(deque_x.copy())', globals=globals(), number=100))
print(timeit('extend(list_x.copy())', globals=globals(), number=100))
print(timeit('extend(deque_x.copy())', globals=globals(), number=100))

# 2


def appendleft_list(x):
    for i in range(n):
        x.insert(0, i)
    return x


def appendleft_deque(x):
    for i in range(n):
        x.appendleft(i)
    return x


def popleft_list(x):
    for i in range(n):
        x.pop(i)
    return x


def popleft_deque(x):
    for i in range(n):
        x.popleft()
    return x


def extendleft_list(x):
    for i in range(n):
        x.insert(0, [1, 2, 3])
    return x


def extendleft_deque(x):
    for i in range(n):
        x.extendleft([1, 2, 3])
    return x


print(timeit('appendleft_list(list_x.copy())', globals=globals(), number=100))
print(timeit('appendleft_deque(deque_x.copy())', globals=globals(), number=100))
print(timeit('popleft_list(list_x.copy())', globals=globals(), number=100))
print(timeit('popleft_deque(deque_x.copy())', globals=globals(), number=100))
print(timeit('extendleft_list(list_x.copy())', globals=globals(), number=100))
print(timeit('extendleft_deque(deque_x.copy())', globals=globals(), number=100))

# 3


def get_elem_list(collections_x):
    for i in range(n):
        collections_x[i] = i
    return collections_x


def get_elem_deque(collections_x):
    for i in range(n):
        collections_x[i] = i
    return collections_x


print(timeit('get_elem_list(list_x.copy())', globals=globals(), number=100))
print(timeit('get_elem_deque(deque_x.copy())', globals=globals(), number=100))