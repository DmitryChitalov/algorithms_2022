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
import timeit


deq_l = deque([el for el in range(100000)])
smp_lst = [el for el in range(100000)]
n = 10000


def deq_append(deq_l):
    for i in range(n):
        deq_l.append(i)
    return deq_l


def smp_append(smp_lst):
    for i in range(n):
        smp_lst.append(i)
    return smp_lst


def deq_pop(deq_l):
    for i in range(n):
        deq_l.pop()
    return deq_l


def smpl_pop(smp_lst):
    for i in range(n):
        smp_lst.pop()
    return smp_lst


def deq_ext(deq_l):
    for i in range(n):
        deq_l.extend([1, 1, 1])
    return deq_l


def smpl_ext(smp_lst):
    for i in range(n):
        smp_lst.extend([1, 1, 1])
    return smp_lst


print(timeit.timeit('deq_append(deq_l.copy())', globals=globals(), number=1000))
print(timeit.timeit('smp_append(smp_lst.copy())', globals=globals(), number=1000))
print(timeit.timeit('deq_pop(deq_l.copy())', globals=globals(), number=1000))
print(timeit.timeit('smpl_pop(smp_lst.copy())', globals=globals(), number=1000))
print(timeit.timeit('deq_ext(deq_l.copy())', globals=globals(), number=1000))
print(timeit.timeit('smpl_ext(smp_lst.copy())', globals=globals(), number=1000))

# 4.905618200078607
# 4.45648629963398
# 3.6588973999023438
# 3.225710599683225
# 6.196979399770498
# 6.161977199837565

""" Операции со списком проходят быстрее """