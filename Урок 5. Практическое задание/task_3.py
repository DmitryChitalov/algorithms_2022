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
Результат анализа подтверждает данные в документации - добавление элементов слева в разы быстрее в деке,
тогда как доступ к случайному элементу - быстрее в списке
"""

from collections import deque
from timeit import timeit

simple_list = []
simple_deque = deque()

number = 100

"""
1) append, pop, extend списка и дека:
append list/deque
0.0006038000000000016
0.0009190999999999991
pop list/deque
0.0004778999999999964
0.00046750000000000264
extend list/deque
0.0012336000000000014
0.001547800000000002
"""
print("------------------------------------------------------------------------------------")


def lst_append(lst):
    for i in range(number):
        lst.append(i)
    return lst


def deq_append(deq):
    for i in range(number):
        deq.append(i)
    return deq


print("append list/deque")
lst_append(simple_list)
deq_append(simple_deque)
print(timeit("lst_append(simple_list)", setup="from __main__ import lst_append, simple_list", number=100))
print(timeit('deq_append(simple_deque)', setup="from __main__ import deq_append, simple_deque", number=100))


def lst_pop(lst):
    for i in range(number):
        lst.pop()
    return lst


def deq_pop(deq):
    for i in range(number):
        deq.pop()
    return deq


print("pop list/deque")
lst_pop(simple_list)
deq_pop(simple_deque)
print(timeit('lst_pop(simple_list)', setup="from __main__ import lst_pop, simple_list", number=100))
print(timeit('deq_pop(simple_deque)', setup="from __main__ import deq_pop, simple_deque", number=100))


def lst_extend(lst):
    for i in range(number):
        lst.extend([i, i + 1])
    return lst


def deq_extend(deq):
    for i in range(number):
        deq.extend([i, i + 1])
    return deq


print("extend list/deque")
lst_extend(simple_list)
deq_extend(simple_deque)
print(timeit('lst_extend(simple_list)', setup="from __main__ import lst_extend, simple_list", number=100))
print(timeit('deq_extend(simple_deque)', setup="from __main__ import deq_extend, simple_deque", number=100))

"""
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка:
appendleft list/deque
0.20140909999999998
0.0006578000000000417
popleft list/deque
0.06771159999999998
0.0004065999999999792
extendleft list/deque
0.17533709999999997
0.0013032000000000044
"""
print("------------------------------------------------------------------------------------")


def lst_appendleft(lst):
    for i in range(number):
        lst.insert(0, i)
    return lst


def deq_appendleft(deq):
    for i in range(number):
        deq.appendleft(i)
    return deq


print("appendleft list/deque")
lst_appendleft(simple_list)
deq_appendleft(simple_deque)
print(timeit("lst_appendleft(simple_list)", setup="from __main__ import lst_appendleft, simple_list", number=100))
print(timeit('deq_appendleft(simple_deque)', setup="from __main__ import deq_appendleft, simple_deque", number=100))


def lst_popleft(lst):
    for i in range(number):
        lst.pop(i)
    return lst


def deq_popleft(deq):
    for i in range(number):
        deq.popleft()
    return deq


print("popleft list/deque")
lst_popleft(simple_list)
deq_popleft(simple_deque)
print(timeit('lst_popleft(simple_list)', setup="from __main__ import lst_popleft, simple_list", number=100))
print(timeit('deq_popleft(simple_deque)', setup="from __main__ import deq_popleft, simple_deque", number=100))


def lst_extendleft(lst):
    for i in range(number):
        lst.insert(0, [i, i + 1])
    return lst


def deq_extendleft(deq):
    for i in range(number):
        deq.extend([i, i + 1])
    return deq


print("extendleft list/deque")
lst_extendleft(simple_list)
deq_extendleft(simple_deque)
print(timeit('lst_extendleft(simple_list)', setup="from __main__ import lst_extendleft, simple_list", number=100))
print(timeit('deq_extendleft(simple_deque)', setup="from __main__ import deq_extendleft, simple_deque", number=100))

"""
3) сравнить операции получения элемента списка и дека и сделать выводы что и где быстрее
take_el list/deque
0.00026809999999999334
0.0004280999999999868
"""
print("------------------------------------------------------------------------------------")


def lst_take_el(lst):
    for i in range(number):
        lst[i] = i
    return lst


def deq_take_el(deq):
    for i in range(number):
        deq[i] = i
    return deq


print("take_el list/deque")
lst_take_el(simple_list)
deq_take_el(simple_deque)
print(timeit('lst_take_el(simple_list)', setup="from __main__ import lst_take_el, simple_list", number=100))
print(timeit('deq_take_el(simple_deque)', setup="from __main__ import deq_take_el, simple_deque", number=100))
