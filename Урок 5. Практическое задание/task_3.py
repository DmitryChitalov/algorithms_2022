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

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
'''
Пункт 1:
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
'''
from collections import deque
from timeit import timeit


some_list = [i for i in range(10000)]
some_deque = deque([i for i in range(10000)])

n = 10000


def append_func(some_list_deque):
    for i in range(n):
        some_list_deque.append(i)
    return some_list_deque


def pop_func(some_list_deque):
    for i in range(n):
        some_list_deque.pop()
    return some_list_deque


def extend_func(some_list_deque):
    for i in range(n):
        some_list_deque.extend([1, 2, 3])
    return some_list_deque


# print('append list: ', timeit('append_func(some_list.copy())', globals=globals(), number=100))
# print('append deque: ', timeit('append_func(some_deque.copy())', globals=globals(), number=100))
#
# print('pop list: ', timeit('pop_func(some_list.copy())', globals=globals(), number=100))
# print('pop deque: ', timeit('pop_func(some_deque.copy())', globals=globals(), number=100))
#
# print('extend list: ', timeit('extend_func(some_list.copy())', globals=globals(), number=100))
# print('extend deque: ', timeit('extend_func(some_deque.copy())', globals=globals(), number=100))


'''
append list:  0.045088207999924634
append deque:  0.03616250000004584
pop list:  0.02704924999989089
pop deque:  0.029140000000097643
extend list:  0.05545908300018709
extend deque:  0.07283116700000392

Замеры отличаются друг от друга незначительно, однако для lis быстрее выполняется append, а для deque - extend
'''

'''
Пункт 2:
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

'''


def appendleft_deque(some_deque):
    for i in range(n):
        some_deque.appendleft(i)
    return some_deque


def popleft_deque(some_deque):
    for i in range(n):
        some_deque.popleft()
    return some_deque


def extendleft_deque(some_deque):
    for i in range(n):
        some_deque.extendleft(['a', 'b', 'c'])
    return some_deque


def appendleft_list(some_list):
    for i in range(n):
        some_list.insert(0, i)
    return some_list


def popleft_list(some_list):
    for i in range(n):
        some_list.pop(0)
    return some_list


def extendleft_list(some_list):
    for i in range(n):
        some_list = ['a', 'b', 'c'] + (some_list)
    return some_list

# print('appendleft list: ', timeit('appendleft_list(some_list.copy())', globals=globals(), number=100))
# print('appendleft deque: ', timeit('appendleft_deque(some_deque.copy())', globals=globals(), number=100))
#
# print('popleft list: ', timeit('popleft_list(some_list.copy())', globals=globals(), number=100))
# print('popleft deque: ', timeit('popleft_deque(some_deque.copy())', globals=globals(), number=100))
#
# print('extendleft list: ', timeit('extendleft_list(some_list.copy())', globals=globals(), number=10))
# print('extendleft deque: ', timeit('extendleft_deque(some_deque.copy())', globals=globals(), number=10))


'''
appendleft list:  7.1287896249996265
appendleft deque:  0.0340425000003961
popleft list:  0.5841240409999955
popleft deque:  0.02938470800017967
extendleft list:  6.874103084000126
extendleft deque:  0.007481707999431819

Очевидно что эти операции выполняются с deque гораздо быстрее
'''
'''
Пункт 3:
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
'''

def element(some_list_deque):
    for i in range(n):
        some_list_deque[i] = i
    return some_list_deque

print('получение элемента list: ', timeit('element(some_list.copy())', globals=globals(), number=100))
print('получение элемента deque: ', timeit('element(some_deque.copy())', globals=globals(), number=100))

'''
получение элемента list:  0.03413370799989934
получение элемента deque:  0.05546441699971183

Время получения элемента списка меньше
'''