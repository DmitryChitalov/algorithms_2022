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

def comparison_list_append():
    my_list = []
    my_list.append(1)

def comparison_list_pop():
    my_list = [1, 2, 3]
    my_list.pop()

def comparison_list_extend():
    my_list = []
    my_list.extend([1, 2, 3])

def comparison_list_getElement():
    my_list = [4, 5]
    elem = my_list[0]

def comparison_deque_appendLeft():
    my_deque = deque()
    my_deque.appendleft(12)

def comparison_deque_popLeft():
    my_deque = deque([1, 3, 14, 8])
    my_deque.popleft()

def comparison_deque_extendLeft():
    my_deque = deque()
    my_deque.extendleft([16, 3, 8])

def comparison_deque_getElement():
    my_deque = deque([4, 5])
    elem = my_deque[0]

if name == 'main':
    print '1) Сравниваем append, pop, extend: '
    print timeit('comparison_list_append()', setup='from main import comparison_list_append', number=10000)
    print timeit('comparison_list_pop()', setup='from main import comparison_list_pop', number=10000)
    print timeit('comparison_list_extend()', setup='from main import comparison_list_extend', number=10000)
    """
    Вывод:
    1) Сравниваем append, pop, extend: 
        0.0022994
        0.0029306
        0.0033971
    Быстрее всех оказалась функция append
    """
    print '2) Сравниваем appendLeft, popLeft, extendLeft: '
    print timeit('comparison_deque_appendLeft()', setup='from main import comparison_deque_appendLeft', number=10000)
    print timeit('comparison_deque_popLeft()', setup='from main import comparison_deque_popLeft', number=10000)
    print timeit('comparison_deque_extendLeft()', setup='from main import comparison_deque_extendLeft', number=10000)
    """
    Вывод:
    2) Сравниваем appendLeft, popLeft, extendLeft: 
        0.0024895
        0.0042715
        0.0039445
    Быстрее оказалась функция append
    Быстрее оказалась функция pop
    Быстрее оказалась функция extend
    """
    print '3) Сравниваем получение элемента из list и deque: '
    print timeit('comparison_list_getElement()', setup='from main import comparison_list_getElement', number=10000)
    print timeit('comparison_deque_getElement()', setup='from main import comparison_deque_getElement', number=10000)
    """
    Вывод:
    3) Сравниваем получение элемента из list и deque: 
        0.0025947
        0.0046612
    Быстрее оказалась  comparison_list_getElement()   
    """
