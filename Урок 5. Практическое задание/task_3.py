"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

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
(append, pop и т.д.) проводить в циклах
"""

from timeit import timeit
from collections import deque
from random import randint


def check_list_append(my_lst):
    for i in range(0, 10000):
        my_lst.append(i)


def check_deque_append(my_deque):
    for i in range(0, 10000):
        my_deque.append(i)


def check_list_pop(my_lst):
    for i in range(0, 10000):
        my_lst.pop()


def check_deque_pop(my_deque):
    for i in range(0, 10000):
        my_deque.pop()


def check_list_extend(my_lst):
    add_lst = list(randint(0, 10000) for i in range(10))
    for i in range(0, 1000):
        my_lst.extend(add_lst)


def check_deque_extend(my_deque):
    add_deque = deque(randint(0, 10000) for i in range(10))
    for i in range(0, 1000):
        my_deque.extend(add_deque)


def check_list_insert(my_lst):
    for i in range(0, 1000):
        my_lst.insert(0, i)


def check_deque_appendleft(my_deque):
    for i in range(0, 1000):
        my_deque.appendleft(i)


def check_list_popleft(my_lst):
    for i in range(1, 10):
        my_lst.pop(i)


def check_deque_popleft(my_deque):
    for i in range(1, 10):
        my_deque.popleft()


def check_list_extendleft(my_lst):
    add_lst = list(randint(0, 10000) for i in range(10))
    for i in range(0, 1000):
        my_lst.insert(0, add_lst)


def check_deque_extendleft(my_deque):
    add_deque = deque(randint(0, 10000) for i in range(10))
    for i in range(0, 1000):
        my_deque.extendleft(add_deque)


def list_get(my_lst, idx):
    return my_lst[idx]


def deque_get(my_deque, idx):
    return my_deque[idx]


def check_list_get(my_lst):
    for i in range(0, 10000):
        list_get(my_lst, 5)


def check_deque_get(my_deque):
    for i in range(0, 10000):
        deque_get(my_deque, 5)


new_lst = list(randint(0, 10000) for i in range(1000))
new_deque = deque(randint(0, 10000) for j in range(1000))
print("list append", timeit("check_list_append(new_lst)", number=2000, globals=globals()), "seconds")
print("deque append", timeit("check_deque_append(new_deque)", number=2000, globals=globals()), "seconds")

# В результате 4х проходов, list append незначительно медленнее
# list append 2.115750741 seconds
# deque append 1.7006729270000003 seconds

# list append 2.1505018799999998 seconds
# deque append 1.6311090680000002 seconds

# list append 2.115640122 seconds
# deque append 1.591039914 seconds

# list append 2.173480568 seconds
# deque append 1.601812796 seconds

print("-------------------------------------------------------------------------------------")
print("list pop", timeit("check_list_pop(new_lst)", number=2000, globals=globals()), "seconds")
print("deque pop", timeit("check_deque_pop(new_deque)", number=2000, globals=globals()), "seconds")

# В результате 4х проходов, list pop незначительно медленнее
# list pop 2.2226102789999995 seconds
# deque pop 1.8161810469999997 seconds

# list pop 2.3396283009999994 seconds
# deque pop 1.8594533270000007 seconds

# list pop 2.2224737139999995 seconds
# deque pop 1.864917031 seconds

# list pop 2.2311733309999995 seconds
# deque pop 1.8315574779999997 seconds

print("-------------------------------------------------------------------------------------")
print("list extend", timeit("check_list_extend(new_lst)", number=2000, globals=globals()), "seconds")
print("deque extend", timeit("check_deque_extend(new_deque)", number=2000, globals=globals()), "seconds")

# За четыре прохода,  list extend выполняется в среднем в два раза медленне.
# Сделать большее количество повтрений ( как и увеличть массивы для добавления не представляется возможным, возникает Memory Error)

# list extend 0.736774881 seconds
# deque extend 0.42801091700000005 seconds

# list extend 0.7688722859999999 seconds
# deque extend 0.40176951699999996 seconds

# list extend 0.740372874 seconds
# deque extend 0.40924832499999997 seconds

# list extend 0.7437162700000001 seconds
# deque extend 0.4190350370000001 seconds

new_lst = list(randint(0, 10000) for i in range(1000))
new_deque = deque(randint(0, 10000) for j in range(1000))
print("-------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------")
print("list insert", timeit("check_list_insert(new_lst)", number=200, globals=globals()), "seconds")
print("deque appendleft", timeit("check_deque_appendleft(new_deque)", number=200, globals=globals()), "seconds")

# За 4 прохода list insert ощутимо медленнее
# list insert 7.410647322 seconds
# deque appendleft 0.017128385000000357 seconds

# list insert 7.646397117999999 seconds
# deque appendleft 0.016565308000000556 seconds

# list insert 7.737764756 seconds
# deque appendleft 0.01643644199999983 seconds

# list insert 7.34050385 seconds
# deque appendleft 0.015951482000000183 seconds

print("-------------------------------------------------------------------------------------")
print("list popleft", timeit("check_list_popleft(new_lst)", number=20000, globals=globals()), "seconds")
print("deque popleft", timeit("check_deque_popleft(new_deque)", number=20000, globals=globals()), "seconds")
# За четыре прохода  list popleft значительно медленнее
# list popleft 3.971813061 seconds
# deque popleft 0.00023720599999776937 seconds

# list popleft 4.391337903 seconds
# deque popleft 0.000226371000000114 seconds

# list popleft 3.498286392 seconds
# deque popleft 0.00022352099999878305 seconds

# list popleft 3.836609493 seconds
# deque popleft 0.00024005600000265304 seconds


print("-------------------------------------------------------------------------------------")
print("list extendleft", timeit("check_list_extendleft(new_lst)", number=200, globals=globals()), "seconds")
print("deque extendleft", timeit("check_deque_extendleft(new_deque)", number=200, globals=globals()), "seconds")

# list extendleft 7.503493503 seconds
# deque extendleft 0.03978234100000044 seconds
#
# list extendleft 7.3521961870000005 seconds
# deque extendleft 0.04031662299999983 seconds

# list extendleft 7.416697766 seconds
# deque extendleft 0.0418715719999998 seconds

# list extendleft 8.291434297 seconds
# deque extendleft 0.04488082899999846 seconds

print("-------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------")
print("list get", timeit("check_list_get(new_lst)", number=2000, globals=globals()), "seconds")
print("deque get", timeit("check_deque_get(new_deque)", number=2000, globals=globals()), "seconds")

# За 4 прохода время обращения по индексу примерно одинаковое
# list get 2.787052984 seconds
# deque get 2.9590267850000003 seconds

# list get 2.834062958 seconds
# deque get 2.7729954369999996 seconds

# list get 2.806539452 seconds
# deque get 2.7502907340000005 seconds
# list get 2.8312156400000004 seconds
# deque get 2.951112911 seconds
