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

test = [34, 786, 56, 9, 234, 65, 33, 925, 17, 3]
test_d = deque(test)


def app_list(ls):
    for i in range(20):
        ls.append(i)
    return ls


def pop_list(ls):
    for i in range(8):
        ls.pop()
    return ls


def ext_list(ls):
    l1 = [74, 56, 8]
    for i in range(8):
        ls.extend(l1)
    return ls


print(test)
print(test_d)
print('Операция append')
print(timeit("app_list(test)", setup='from __main__ import app_list, test', number=100000))
print(timeit("app_list(test_d)", setup='from __main__ import app_list, test_d', number=100000))
print('Операция pop')
print(timeit("pop_list(test)", setup='from __main__ import pop_list, test', number=100000))
print(timeit("pop_list(test_d)", setup='from __main__ import pop_list, test_d', number=100000))
print('Операция extend')
print(timeit("ext_list(test)", setup='from __main__ import ext_list, test', number=100000))
print(timeit("ext_list(test_d)", setup='from __main__ import ext_list, test_d', number=100000))
"""Данные операции выполняются приблизительно за одно и тоже время"""


test = [34, 786, 56, 9, 234, 65, 33, 925, 17, 3]
test_d = deque(test)


def ins_list(ls):
    for i in range(10):
        ls.insert(0, i)
    return ls


def pop_list2(ls):
    for i in range(8):
        ls.pop(0)
    return ls


def ext_list(ls):
    l1 = [74, 56, 8]
    for i in range(8):
        ls.insert(0, l1)
    return ls


def appl_d(ls):
    for i in range(10):
        ls.appendleft(i)
    return ls


def popl_d(ls):
    for i in range(8):
        ls.popleft()
    return ls


def extl_d(ls):
    l1 = [74, 56, 8]
    for i in range(8):
        ls.extendleft(l1)
    return ls


print('Операция insert и appendleft')
print(timeit("ins_list(test)", setup='from __main__ import ins_list, test', number=1000))
print(timeit("appl_d(test_d)", setup='from __main__ import appl_d, test_d', number=1000))
print('Операция pop[0] и popleft')
print(timeit("pop_list2(test)", setup='from __main__ import pop_list2, test', number=1000))
print(timeit("popl_d(test_d)", setup='from __main__ import popl_d, test_d', number=1000))
print('Операция extend и extend left')
print(timeit("ext_list(test)", setup='from __main__ import ext_list, test', number=1000))
print(timeit("extl_d(test_d)", setup='from __main__ import extl_d, test_d', number=1000))
"""Данные операции выполняются выполняются значительно быстрее для  deque"""


test = [34, 786, 56, 9, 234, 65, 33, 925, 17, 3]
test_d = deque(test)


def get_el(ls):
    for i in range(10):
        a = ls[i]
    return


print('Взятие i-го элемента')
print(timeit("get_el(test)", setup='from __main__ import get_el, test', number=1000000))
print(timeit("get_el(test_d)", setup='from __main__ import get_el, test_d', number=1000000))
"""Данные операции выполняются приблизительно за одно и тоже время"""
