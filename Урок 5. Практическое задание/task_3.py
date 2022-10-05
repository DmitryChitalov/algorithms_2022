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


"""
append, pop, extend - результаты практически одинаковы, но список работает быстрее в extend

appendleft, popleft, extendleft - дек в данном случае работает быстрее, кроме extendleft/ я так понял, что extendleft для списка работает также как extend, только слева. Поэтому я поменял местами используемые списки местами. 

сравнить операции получения элемента списка и дека - спиоок работает быстрее
"""

import collections
import timeit


# 1 append, pop, extend

def lst_append():
    res = []
    for i in range(1000):
        res.append(i)
    return res


def deque_append():
    res = collections.deque()
    for i in range(1000):
        res.append(i)
    return res


def lst_pop(lst_in):
    for i in range(len(lst_in)):
        lst_in.pop()
    return lst_in


def deque_pop(deque_in):
    for i in range(len(deque_in)):
        deque_in.pop()
    return deque_in


def lst_ext(lst1, lst2):
    lst1.extend(lst2)
    return lst1


def deque_ext(deq1, deq2):
    deq1.extend(deq2)
    return deq1


print('--append--')
print(timeit.timeit("lst_append()", globals=globals(), number=1000))
print(timeit.timeit("deque_append()", globals=globals(), number=1000))

print('--pop--')
lst1 = lst_append()
deque1 = deque_append()
print(timeit.timeit("lst_pop(lst1)", globals=globals(), number=100000))
print(timeit.timeit("deque_pop(deque1)", globals=globals(), number=100000))

print('--extend--')
lst1 = lst_append()
lst2 = lst_append()
deque1 = deque_append()
deque2 = deque_append()
print(timeit.timeit("lst_ext(lst1, lst2)", globals=globals(), number=100000))
print(timeit.timeit("deque_ext(deque1, deque2)", globals=globals(), number=100000))


# 2  appendleft, popleft, extendleft

def lst_appendleft(lst1):
    for i in range(1000):
        lst1.insert(0, i)
    return lst1


def deque_appendleft(deque1):
    for i in range(1000):
        deque1.appendleft(i)
    return deque1


def lst_popleft(lst1):
    for i in range(len(lst1)):
        lst1.pop(0)
    return lst1


def deque_popleft(deque1):
    for i in range(len(deque1)):
        deque1.popleft()
    return deque1


def lst_extleft(lst1, lst2):
    lst2.extend(lst1)
    return lst1


def deque_extleft(deq1, deq2):
    deq1.extendleft(deq2)
    return deq1


print('--appendleft--')
lst1 = lst_append()
lst2 = lst_append()
lst3 = lst_append()
deque1 = deque_append()
deque2 = deque_append()
deque3 = deque_append()

print(timeit.timeit("lst_appendleft(lst1)", globals=globals(), number=10))
print(timeit.timeit("deque_appendleft(deque1)", globals=globals(), number=10))

print('--popleft--')
print(timeit.timeit("lst_popleft(lst1)", globals=globals(), number=10000))
print(timeit.timeit("deque_popleft(deque1)", globals=globals(), number=10000))

print('--extendleft--')
print(timeit.timeit("lst_extleft(lst2, lst3)", globals=globals(), number=10000))
print(timeit.timeit("deque_extleft(deque2, deque3)", globals=globals(), number=10000))

print('--сравнить операции получения элемента списка и дека--')


def get_el(iter):
    for i in range(len(iter)):
        a = iter[i]

print(timeit.timeit("get_el(lst2)", globals=globals(), number=10))
print(timeit.timeit("get_el(deque3)", globals=globals(), number=10))


