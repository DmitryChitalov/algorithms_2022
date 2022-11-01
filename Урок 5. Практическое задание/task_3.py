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
from random import randint
from timeit import timeit

numbers = [randint(0, 10 ** 5) for _ in range(10 ** 5)]

rand_lst = numbers
rand_dq = deque(numbers)
n = 10 ** 4


def lst_app(lst):
    for el in range(n):
        lst.append(randint(0, n))
    return lst


def dq_app(dq):
    for el in range(n):
        dq.append(randint(0, n))
    return dq


def lst_pop(lst):
    for _ in range(n):
        lst.pop()
    return lst


def dq_pop(dq):
    for _ in range(n):
        dq.pop()
    return dq


def lst_ex(lst):
    for _ in range(n):
        lst.extend([1, 2, 3, 4, 5])
    return lst


def dq_ex(dq):
    for _ in range(n):
        dq.extend([1, 2, 3, 4, 5])
    return dq


print('Append list vs deque:')
print(timeit('lst_app(rand_lst.copy())', globals=globals(), number=1000))
print(timeit('dq_app(rand_dq.copy())', globals=globals(), number=1000))

print('Pop list vs deque:')
print(timeit('lst_pop(rand_lst.copy())', globals=globals(), number=1000))
print(timeit('dq_pop(rand_dq.copy())', globals=globals(), number=1000))

print('Extend list vs deque:')
print(timeit('lst_ex(rand_lst.copy())', globals=globals(), number=1000))
print(timeit('dq_ex(rand_dq.copy())', globals=globals(), number=1000))

'''
Append list vs deque:
5.182345199998963
5.121244999998453
Pop list vs deque:
0.4919440999983635
0.7624708000003011
Extend list vs deque:
1.2295844000000216
1.3428409000007377
'''

"""
Операции добавления, удаления и замены элементов списка и дека по времени примерно равны с небольшой погрешностью.
"""


def lst_app_left(lst):
    for i in range(n):
        lst.insert(0, i)
    return lst


def dq_app_left(dq):
    for i in range(n):
        dq.appendleft(i)
    return dq


def lst_pop_left(lst):
    for i in range(n):
        lst.pop(i)
    return lst


def dq_pop_left(dq):
    for _ in range(n):
        dq.popleft()
    return dq


def lst_ex_left(lst):
    for i in range(n):
        lst.insert(0, [randint(0, n) for _ in range(3)])
    return lst


def dq_ex_left(dq):
    for i in range(n):
        dq.extendleft([randint(0, n) for _ in range(3)])
    return dq


print('Left append list vs deque:')
print(timeit('lst_app_left(rand_lst.copy())', globals=globals(), number=100))
print(timeit('dq_app_left(rand_dq.copy())', globals=globals(), number=100))

print('Left pop list vs deque:')
print(timeit('lst_pop_left(rand_lst.copy())', globals=globals(), number=100))
print(timeit('dq_pop_left(rand_dq.copy())', globals=globals(), number=100))

print('Left extend list vs deque:')
print(timeit('lst_ex_left(rand_lst.copy())', globals=globals(), number=100))
print(timeit('dq_ex_left(rand_dq.copy())', globals=globals(), number=100))

'''
Left append list vs deque:
24.74177160000181
0.0882117000001017
Left pop list vs deque:
10.048870499998884
0.07147169999734615
Left extend list vs deque:
27.518280100000993
1.7631137000025774
'''

"""
Операции добавления, удаления и замены элементов дека быстрее, чем у списка.
"""


def lst_get(lst):
    for i in range(n):
        lst[i] = i
    return lst


def dq_get(dq):
    for i in range(n):
        dq[i] = i
    return dq


print('Get element list vs deque:')
print(timeit('lst_get(rand_lst.copy())', globals=globals(), number=1000))
print(timeit('dq_get(rand_dq.copy())', globals=globals(), number=1000))

'''
Get element list vs deque:
0.39533680000022287
1.4922249999981432
'''

"""
Операции получения элемента из списка быстрее, чем из дека, так как элемент определяется в списке по индексу,
а в деке перебором каждого элемента.
"""