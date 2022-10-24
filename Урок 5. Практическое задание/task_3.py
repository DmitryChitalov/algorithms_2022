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
соответствует действительности.

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
from timeit import timeit, default_timer, repeat

lst = [randint(0, 100) for i in range(0, 20000)]
deq = deque(lst)
lst_2 = [randint(0, 100) for i in range(0, 700000)]


# 1  Добавление, удаление (в конце)

def add_lst():
    for el in lst_2:
        lst.append(el)

def add_deq():
    for el in lst_2:
        deq.append(el)

def pop_lst():
    for i in range(0, len(lst)):
        lst.pop()

def pop_deq():
    for i in range(0, len(deq)):
        deq.pop()

def ext_lst():
    count = 0
    while count < 10:
        lst.extend(lst_2)
        count += 1

def ext_deq():
    count = 0
    while count < 10:
        deq.extend(lst_2)
        count += 1



print('add_lst: ', min(repeat('add_lst', 'from __main__ import add_lst', default_timer, 2, 1000000)))
print('add_deq: ', min(repeat('add_deq', 'from __main__ import add_deq', default_timer, 2, 1000000)))
print('pop_lst: ', min(repeat('pop_lst', 'from __main__ import pop_lst', default_timer, 2, 1000000)))
print('pop_deq: ', min(repeat('pop_deq', 'from __main__ import pop_deq', default_timer, 2, 1000000)))
print('ext_lst: ', min(repeat('ext_lst', 'from __main__ import ext_lst', default_timer, 2, 1000000)))
print('ext_deq: ', min(repeat('ext_deq', 'from __main__ import ext_deq', default_timer, 2, 1000000)))


# - операция добавления, удаления (с конца), объединения - для списка и для deque - время примерно одинаковое
# add_lst:  0.01319359999615699
# add_deq:  0.012689399998635054
# pop_lst:  0.014489199966192245
# pop_deq:  0.012763800099492073
# ext_lst:  0.012958599952980876
# ext_deq:  0.012953600031323731

# -------------------------------------------------------------------------------------------
# 2 Добавление, удаление (в начале)

def ins_lst():
    for el in lst_2:
        lst.insert(0, el)

def appendleft_deq():
    for el in lst_2:
        deq.appendleft(el)

def popleft_lst():
    for i in range(0, len(lst)):
        lst.pop(0)

def popleft_deq():
    for i in range(0, len(deq)):
        deq.popleft()

def extendleft_lst():
    i = 0
    while i < 10000:
        for el in lst_2:
            lst.insert(0, el)
        i += 1

def extendleft_deq():
    i = 0
    while i < 10000:
        deq.extendleft(lst_2)
        i += 1


print('ins_lst: ', timeit('ins_lst', 'from __main__ import ins_lst', default_timer, 10000000))
print('appendleft_deq: ', timeit('appendleft_deq', 'from __main__ import appendleft_deq', default_timer, 10000000))
print('popleft_lst: ', timeit('popleft_lst', 'from __main__ import popleft_lst', default_timer, 10000000))
print('popleft_deq: ', timeit('popleft_deq', 'from __main__ import popleft_deq', default_timer, 10000000))
print('extendleft_lst: ', timeit('extendleft_lst', 'from __main__ import extendleft_lst', default_timer, 10000000))
print('extendleft_deq: ', timeit('extendleft_deq', 'from __main__ import extendleft_deq', default_timer, 10000000))

# - операция добавления элемента в начале для deque время меньше, чем для списка
# ins_lst:  0.21234619989991188
# appendleft_deq:  0.15289070003200322
# popleft_lst:  0.2599057999905199
# popleft_deq:  0.1726323999464512
# extendleft_lst:  0.17215700005181134
# extendleft_deq:  0.15585819992702454


# 3 Получение элемента

def get_el_lst():
    for i in lst:
        el = lst[i]

def get_el_deq():
    for i in deq:
        el = deq[i]


print('get_el_lst: ', timeit('get_el_lst', 'from __main__ import get_el_lst', default_timer, 10000000))
print('get_el_deq: ', timeit('get_el_deq', 'from __main__ import get_el_deq', default_timer, 10000000))

# - операция получения значения элемента для списка время меньше чем для deq
# get_el_lst:  0.1438501999946311
# get_el_deq:  0.19496260001324117