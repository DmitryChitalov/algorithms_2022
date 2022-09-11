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


a_list_obj = []
a_deque_obj = deque()


# 1)
def fill_list(a_list):
    for i in range(100000):
        a_list.append(i)


def fill_deque(a_deque):
    for i in range(100000):
        a_deque.append(i)


def pop_list_el(a_list):
    for i in range(100000):
        a_list.pop()


def pop_deque_el(a_deque):
    for i in range(100000):
        a_deque.pop()


def extend_list(a_list):
    for i in range(100000):
        a_list.extend([i])


def extend_deque(a_deque):
    for i in range(100000):
        a_deque.extend([i])


# 2)
def insert_in_list(a_list):
    for i in range(10):
        a_list.insert(0, i)


def appendleft_deque(a_deque):
    for i in range(10):
        a_deque.appendleft(i)


def del_el_list(a_list):
    for i in range(10):
        del a_list[0]


def popleft_deque(a_deque):
    for i in range(10):
        a_deque.popleft()


def insert_list_in_list(a_list):
    for i in range(10):
        a_list.insert(0, [i])


def extendleft_deque(a_deque):
    for i in range(10):
        a_deque.extendleft([i])


# 3)
def get_list_el(a_list):
    for i in range(100000):
        return a_list[i]


def get_deque_el(a_deque):
    for i in range(100000):
        return a_deque[i]


# 1)
print(f'Время выполнения функции {fill_list.__name__}: ',
      timeit('fill_list(a_list_obj)', 'from __main__ import fill_list, a_list_obj', number=100))
print(f'Время выполнения функции {fill_deque.__name__}: ',
      timeit('fill_deque(a_deque_obj)', 'from __main__ import fill_deque, a_deque_obj', number=100))
print(f'Время выполнения функции {pop_list_el.__name__}: ',
      timeit('pop_list_el(a_list_obj)', 'from __main__ import pop_list_el, a_list_obj', number=100))
print(f'Время выполнения функции {pop_deque_el.__name__}: ',
      timeit('pop_deque_el(a_deque_obj)', 'from __main__ import pop_deque_el, a_deque_obj', number=100))
print(f'Время выполнения функции {extend_list.__name__}: ',
      timeit('extend_list(a_list_obj)', 'from __main__ import extend_list, a_list_obj', number=100))
print(f'Время выполнения функции {extend_deque.__name__}: ',
      timeit('extend_deque(a_deque_obj)', 'from __main__ import extend_deque, a_deque_obj', number=100))


# Время выполнения функции fill_list:  4.05198539999401
# Время выполнения функции fill_deque:  3.299800900000264
# Время выполнения функции pop_list_el:  3.5015201000060188
# Время выполнения функции pop_deque_el:  3.235117900003388
# Время выполнения функции extend_list:  5.2230666000032215
# Время выполнения функции extend_deque:  6.135172100002819
#
# Время выполнения операций append, pop, extend списка и дека
# отличается незначительно.


# 2)
print(f'Время выполнения функции {insert_in_list.__name__}: ',
      timeit('insert_in_list(a_list_obj)', 'from __main__ import insert_in_list, a_list_obj', number=100))
print(f'Время выполнения функции {appendleft_deque.__name__}: ',
      timeit('appendleft_deque(a_deque_obj)', 'from __main__ import appendleft_deque, a_deque_obj', number=100))
print(f'Время выполнения функции {del_el_list.__name__}: ',
      timeit('del_el_list(a_list_obj)', 'from __main__ import del_el_list, a_list_obj', number=100))
print(f'Время выполнения функции {popleft_deque.__name__}: ',
      timeit('popleft_deque(a_deque_obj)', 'from __main__ import popleft_deque, a_deque_obj', number=100))
print(f'Время выполнения функции {insert_list_in_list.__name__}: ',
      timeit('insert_list_in_list(a_list_obj)', 'from __main__ import insert_list_in_list, a_list_obj', number=100))
print(f'Время выполнения функции {extendleft_deque.__name__}: ',
      timeit('extendleft_deque(a_deque_obj)', 'from __main__ import extendleft_deque, a_deque_obj', number=100))


# Время выполнения функции insert_in_list:  30.95677369999612
# Время выполнения функции appendleft_deque:  0.0010163999977521598
# Время выполнения функции del_el_list:  33.06783649999852
# Время выполнения функции popleft_deque:  0.0008711999980732799
# Время выполнения функции insert_list_in_list:  35.93880160000117
# Время выполнения функции extendleft_deque:  0.0005908000021008775
#
# Операции appendleft, popleft, extendleft выполняются гораздо быстрее
# аналогичных операций для списка.


# 3)
print(f'Время выполнения функции {get_list_el.__name__}: ',
      timeit('get_list_el(a_list_obj)', 'from __main__ import get_list_el, a_list_obj', number=10000000))
print(f'Время выполнения функции {get_deque_el.__name__}: ',
      timeit('get_deque_el(a_deque_obj)', 'from __main__ import get_deque_el, a_deque_obj', number=10000000))


# Время выполнения функции get_list_el:  20.91874580000149
# Время выполнения функции get_deque_el:  23.189874199997575
#
# Операция получения элемента списка выполняется быстрее операции
# получения элемента дека.
