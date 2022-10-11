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

numbers = [i for i in range(10 ** 5)]

rand_lst = numbers
rand_dq = deque(numbers)
n = 10 ** 3


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


print('Append list', timeit('lst_app(rand_lst.copy())', globals=globals(), number=100))
print('Append deque', timeit('dq_app(rand_dq.copy())', globals=globals(), number=100))

print('Pop list', timeit('lst_pop(rand_lst.copy())', globals=globals(), number=100))
print('Pop deque', timeit('dq_pop(rand_dq.copy())', globals=globals(), number=100))

print('Extend list', timeit('lst_ex(rand_lst.copy())', globals=globals(), number=100))
print('Extend deque', timeit('dq_ex(rand_dq.copy())', globals=globals(), number=100))

"""
Append list 0.26195760001428425
Append deque 0.24207250005565584
Pop list 0.07207849994301796
Pop deque 0.1513703998643905
Extend list 0.15590170002542436
Extend deque 0.14658010005950928

Операции append, pop, extend элементов списка и дека по времени примерно равны по скорости.
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


print('List insert', timeit('lst_app_left(rand_lst.copy())', globals=globals(), number=100))
print('Appendleft deque', timeit('dq_app_left(rand_dq.copy())', globals=globals(), number=100))

print('List pop', timeit('lst_pop_left(rand_lst.copy())', globals=globals(), number=100))
print('Left pop deque', timeit('dq_pop_left(rand_dq.copy())', globals=globals(), number=100))

print('List insert', timeit('lst_ex_left(rand_lst.copy())', globals=globals(), number=100))
print('Extendleft deque', timeit('dq_ex_left(rand_dq.copy())', globals=globals(), number=100))

"""
List insert 6.057441200129688
Appendleft deque 0.11702460004016757
List pop 3.961691399803385
Left pop deque 0.11550670000724494
List insert 6.7274346998892725
Extendleft deque 0.5069385999813676

Операции добавления, удаления и замены элементов дека существенно быстрее, чем у списка.
"""


def lst_get(lst):
    for i in range(n):
        lst[i] = i
    return lst


def dq_get(dq):
    for i in range(n):
        dq[i] = i
    return dq


print('Get element from the list', timeit('lst_get(rand_lst.copy())', globals=globals(), number=1000))
print('Get element from the dequ', timeit('dq_get(rand_dq.copy())', globals=globals(), number=1000))

"""
Get element from the list 0.5127256000414491
Get element from the dequ 1.298525799997151

Операции получения элемента из списка быстрее, чем из дека, так как элемент определяется в списке по индексу,
а в деке перебором каждого элемента.
"""
