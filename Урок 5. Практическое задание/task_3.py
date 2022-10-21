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


lst = [randint(0,100) for i in range(0, 20000)]
deq = deque(lst)
lst_2 = [randint(0,100) for i in range(0, 700000)]
#----------------------------------------------------------------------------------------

#1  Добавление, удаление (в конце)

def add_lst():
    for el in lst_2:
        lst.append(el)

def add_deq():
    for el in lst_2:
            deq.append(el)

# print('add_lst: ', timeit('add_lst', 'from __main__ import add_lst', default_timer, 100000))
# print('add_deq: ',timeit('add_deq', 'from __main__ import add_deq', default_timer, 100000))
print('add_lst: ', min(repeat('add_lst', 'from __main__ import add_lst', default_timer,2, 1000000)))
print('add_deq: ',min(repeat('add_deq', 'from __main__ import add_deq', default_timer,2, 1000000)))

# - операция добавления  в конец для deque время меньше
# add_lst:  0.02338079991750419 сек
# add_deq:  0.014863599906675518 сек

def pop_lst():
    for i in range(0, len(lst)):
        lst.pop()

def pop_deq():
    for i in range(0, len(deq)):
        deq.pop()

# print('pop_lst: ', timeit('pop_lst', 'from __main__ import pop_lst', default_timer, 1000000))
# print('pop_deq: ', timeit('pop_deq', 'from __main__ import pop_deq', default_timer, 1000000))
print('pop_lst: ', min(repeat('pop_lst', 'from __main__ import pop_lst', default_timer,2, 1000000)))
print('pop_deq: ', min(repeat('pop_deq', 'from __main__ import pop_deq', default_timer, 2, 1000000)))

# - операция удаления с конца для deque время меньше
# pop_lst:  0.02066549996379763 сек
# pop_deq:  0.016505899955518544 сек

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

print('ext_lst: ', min(repeat('ext_lst', 'from __main__ import ext_lst', default_timer, 2, 1000000)))
print('ext_deq: ', min(repeat('ext_deq', 'from __main__ import ext_deq', default_timer, 2, 1000000)))
# - операция объединения - для list и deque время одинаковое
# ext_lst:  0.04052300006151199 сек
# ext_deq:  0.04016950004734099 сек

#-------------------------------------------------------------------------------------------
#2 Добавление, удаление (в начале)

def ins_lst():
    for el in lst_2:
        lst.insert(0, el)

def ins_deq():
    for el in lst_2:
        deq.appendleft(el)

print('ins_lst: ', min(repeat('ins_lst', 'from __main__ import ins_lst', default_timer, 5, 1000000)))
print('ins_deq: ', min(repeat('ins_deq', 'from __main__ import ins_deq', default_timer, 5, 1000000)))
# - операция добавления элемента в начале для deque время меньше
# ins_lst:  0.013985500088892877 сек
# ins_deq:  0.013045200030319393 сек

def pop_front_lst():
    for i in range(0, len(lst)):
        lst.pop(0)

def pop_front_deq():
    for i in range(0, len(deq)):
        deq.popleft()

print('pop_front_lst: ', min(repeat('pop_front_lst', 'from __main__ import pop_front_lst', default_timer, 3, 100000)))
print('pop_front_deq: ', min(repeat('pop_front_deq', 'from __main__ import pop_front_deq', default_timer, 3, 100000)))

# - операция удаление элемента в начале для deque время меньше
# pop_front_lst:  0.0013569999719038606
# pop_front_deq:  0.0012800999684259295


# добавление нескольких списков
def ext_front_lst():
    i = 0
    while i < 10:
        for el in lst_2:
            lst.insert(0, el)
        i += 1

# добавление нескольких списков в начало

def ext_front_deq():
    i = 0
    while i < 10:
        deq.extendleft(lst_2)
        i += 1

print('ext_front_lst: ', min(repeat('ext_front_lst', 'from __main__ import ext_front_lst', default_timer, 3, 100000)))
print('ext_front_deq: ', min(repeat('ext_front_deq', 'from __main__ import ext_front_deq', default_timer, 3, 100000)))

# - операция вставка массива в начале для deque время меньше
# ext_front_lst:  0.0015180000336840749 сек
# ext_front_deq:  0.0012955000856891274 сек

#3 Получение элемента

def get_el_lst():
    for i in lst:
        el = lst[i]

def get_el_deq():
    for i in deq:
        el = deq[i]

print('get_el_lst: ', min(repeat('get_el_lst', 'from __main__ import get_el_lst', default_timer, 3, 1000000)))
print('get_el_deq: ', min(repeat('get_el_deq', 'from __main__ import get_el_deq', default_timer, 3, 1000000)))

# - операция получения значения элемента для deque время меньше
# get_el_lst:  0.017076499992981553 сек
# get_el_deq:  0.013623000006191432 сек




# ________________________________________________________________________
# без циклов
# lst = ['computers', 'lamps', 'mouses', 'tables', 'chairs']
# deq = deque(lst)
# ext_lst = ['monitors', 'pencils', 'paints']


# #1  Добавление, удаление (конец)
#
# lst.append('books')
# lst.append('papers')
# deq.append('books')
# deq.append('papers')
#
# lst.pop()
# deq.pop()
#
# lst.extend(ext_lst)
# deq.extend(ext_lst)
#
# print(lst)
# print(deq)
#
# #2 Добавление, удаление (в начало)
#
# lst.insert(0, 'notebooks')
# deq.appendleft('notebooks')
#
# lst.pop(0)
# deq.popleft()
#
# new_lst = lst
# for i in ext_lst:
#     new_lst.insert(0, i)
#
# deq.extendleft(ext_lst)
#
# # print(lst)
# print(new_lst)
# print(deq)
#
#
# #3 Получение элемента
# el = lst[2]
# el_deq = deq[2]
#
#
# print(el)
# print(el_deq)
#
#
