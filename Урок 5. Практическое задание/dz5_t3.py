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

from timeit import timeit

import collections


my_list = []

my_deque = collections.deque()


def my_l(my):
    return my.append(i for i in range(100000))


def my_d(my):
    return my.appendleft(i for i in range(100000))


def my_l_2(my):
    return my.insert(0, (i for i in range(100000)))



print(f"{timeit('my_l(my_list)', 'from __main__ import my_l, my_list', number=100000)}")
print(f"{timeit('my_l(my_deque)', 'from __main__ import my_l, my_deque', number=100000)}")

"""
0.04701670000000002 -list
0.06131160000000002 -deque
Функция append в обычном списке работает быстрее, чем в деке
"""

print(f"{timeit('my_l_2(my_list)', 'from __main__ import my_l_2, my_list', number=100000)}")
print(f"{timeit('my_d(my_deque)', 'from __main__ import my_d, my_deque', number=100000)}")

"""
5.5481667 - list
0.04535059999999991 - deque
Вставка в начало в деке работает намного быстрее, чем в списке
"""
