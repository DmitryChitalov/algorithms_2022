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
from collections import deque

my_lst = [i for i in range(1001)]
my_deq = deque(my_lst)


# 1)
# append
def lst_append():
    for i in range(1001):
        my_lst.append(i)
    return my_lst

def deq_append():
    for i in range(1001):
        my_deq.append(i)
    return my_deq


# pop
def lst_pop():
    for i in range(1001):
        my_lst.pop()
    return my_lst

def deq_pop():
    for i in range(1001):
        my_deq.pop()
    return my_deq


# extend
def lst_extend():
    for i in range(1001):
        my_lst.extend([1, 2, 3])
    return my_lst

def deq_extend():
    for i in range(1001):
        my_deq.extend([1, 2, 3])
    return my_deq


print('-append-')
print('lst', timeit('lst_append()', globals=globals(), number=1000))
print('deq', timeit('deq_append()', globals=globals(), number=1000), '\n')
print('-pop-')
print('lst', timeit('lst_pop()', globals=globals(), number=1000))
print('deq', timeit('deq_pop()', globals=globals(), number=1000), '\n')
print('-extend-')
print('lst', timeit('lst_extend()', globals=globals(), number=1000))
print('deq', timeit('deq_extend()', globals=globals(), number=1000), '\n')

'''
Резльтат замеров следущий: время выполнения операций практически совпадает, очередь незначительно быстрее.
'''


# 2)
# appendleft
def lst_appendleft():
    for i in range(101):
        my_lst.insert(0, i)
    return my_lst

def deq_appendleft():
    for i in range(101):
        my_deq.appendleft(i)
    return my_deq


# popleft
def lst_popleft():
    for i in range(1):
        my_lst.pop()
    return my_lst

def deq_popleft():
    for i in range(1):
        my_deq.popleft()
    return my_deq


# extendleft
def lst_extendleft():
    for i in range(1001):
        my_lst.extend([1, 2, 3])
    return my_lst

def deq_extendleft():
    for i in range(1001):
        my_deq.extendleft([1, 2, 3])
    return my_deq


print('-appendleft-')
print('lst', timeit('lst_appendleft()', globals=globals(), number=1000))
print('deq', timeit('deq_appendleft()', globals=globals(), number=1000), '\n')
print('-popleft-')
print('lst', timeit('lst_popleft()', globals=globals(), number=1000))
print('deq', timeit('deq_popleft()', globals=globals(), number=1000), '\n')
print('-extend-')
print('lst', timeit('lst_extendleft()', globals=globals(), number=1000))
print('deq', timeit('deq_extendleft()', globals=globals(), number=1000), '\n')

'''
Резльтат замеров следущий: время выполнения операций очередью намного меньше!
'''


# 3)
def lst_index():
    for i in range(1001):
        my_lst[i] = i
    return my_lst


def deq_index():
    for i in range(1001):
        my_deq[i] = i
    return my_deq


print('-index-')
print('lst', timeit('lst_index()', globals=globals(), number=1000))
print('deq', timeit('deq_index()', globals=globals(), number=1000), '\n')

'''
Резльтат замеров следущий: списко значительно быстрее получает доступ к случайному элементу.
'''
