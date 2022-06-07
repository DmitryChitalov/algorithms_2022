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

"""
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
"""


def my_list_app(i_list):
    for i in range(coun_num):
        i_list.append(i)
    return i_list


def my_deque_app(i_deque):
    for i in range(coun_num):
        i_deque.append(i)
    return i_deque


my_list = []
my_deque = deque()
coun_num = 100
print(timeit("my_list_app(my_list)", globals=globals(), number=100))
print(timeit("my_deque_app(my_deque)", globals=globals(), number=100))
#Время выполенения 0.0009531001560389996
#Время выполенения 0.000821300083771348


def my_list_pop(i_list):
    for i in range(coun_num):
        i_list.pop()
    return i_list


def my_deque_pop(i_deque):
    for i in range(coun_num):
        i_deque.pop()
    return i_deque



print(timeit('my_list_pop(my_list)', globals=globals(), number=100))
print(timeit('my_deque_pop(my_deque)', globals=globals(), number=100))
#Время выполенения 0.0022369001526385546
#Время выполенения 0.008816900197416544

def my_list_extend(i_list):
    for i in range(coun_num):
        i_list.extend(['e', 'x', 't', 'e', 'n', 'd'])
    return i_list


def my_deque_extend(i_deque):
    for i in range(coun_num):
        i_deque.extend(['e', 'x', 't', 'e', 'n', 'd'])
    return i_deque


print(timeit('my_list_extend(my_list)', globals=globals(), number=100))
print(timeit('my_deque_extend(my_deque)', globals=globals(), number=100))
#Время выполенения 0.0011622998863458633
#Время выполенения 0.0017238999716937542
"""
append, pop, extend без какого либо временного приемущества
"""


"""
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
"""


def my_list_insert(i_list):
    for i in range(coun_num):
        i_list.insert(0,i)
    return i_list


def my_deque_appleft(i_deque):
    for i in range(coun_num):
        i_deque.appendleft(i)
    return i_deque


print(timeit('my_list_insert(my_list)', globals=globals(), number=100))
print(timeit('my_deque_appleft(my_deque)', globals=globals(), number=100))
#Время выполенения 0.3946362000424415
#Время выполенения 0.0004992000758647919

def my_deque_popleft(i_deque):
    for i in range(coun_num):
        i_deque.popleft()
    return i_deque


print(timeit('my_list_pop(my_list)', globals=globals(), number=100))
print(timeit('my_deque_popleft(my_deque)', globals=globals(), number=100))
#Время выполенения 0.00044279987923800945
#Время выполенения 0.00037420005537569523

def my_deque_extendleft(i_deque):
    for i in range(coun_num):
        i_deque.extendleft(['e', 'x', 't', 'e', 'n', 'd'])
    return i_deque


print(timeit('my_list_extend(my_list)', globals=globals(), number=100))
print(timeit('my_deque_extendleft(my_deque)', globals=globals(), number=100))
#Время выполенения 0.002443999983370304
#Время выполенения 0.001704599941149354

"""
вставка элемента в начало дека значительно быстрее чем в лист
"""
"""
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
"""

def my_list_get_elem(i_list):
    for i in range(coun_num):
        elem = i_list[i]
    return elem


def my_deque_get_elem(i_deque):
    for i in range(coun_num):
        elem = i_deque[i]
    return elem


print(timeit('my_list_get_elem(my_list)', globals=globals(), number=100))
print(timeit('my_deque_get_elem(my_deque)', globals=globals(), number=100))
#Время выполенения 0.00034680007956922054
#Время выполенения 0.00043329992331564426

"""
получение элемента из листа чуть быстрее чем из дека
"""