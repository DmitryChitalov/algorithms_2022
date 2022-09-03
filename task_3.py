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

##########################################################################
from collections import deque
from timeit import timeit

some_lst = [i for i in range(10 ** 5)]
some_deque = deque([i for i in range(10 ** 5)])

n = 10 ** 4
###########################################################################
""" 1) сравнение операций append, pop, extend """

""" append """


def append_list(some_lst):
    for i in range(n):
        some_lst.append(i)
    return some_lst


def append_deque(some_deque):
    for i in range(n):
        some_deque.append(i)
    return some_deque


print(timeit('append_list(some_lst.copy())', globals=globals(), number=100))        # 0.3206625999882817
print(timeit('append_deque(some_deque.copy())', globals=globals(), number=100))     # 0.24393640004564077

""" pop """


def pop_list(some_lst):
    for i in range(n):
        some_lst.pop()
    return some_lst


def pop_deque(some_deque):
    for i in range(n):
        some_deque.pop()
    return some_deque


print(timeit('pop_list(some_lst.copy())', globals=globals(), number=100))       # 0.1737548999954015
print(timeit('pop_deque(some_deque.copy())', globals=globals(), number=100))    # 0.3495258999755606

""" extend """


def extend_list(some_lst):
    for i in range(n):
        some_lst.extend([1, 2, 3])
    return some_lst


def extend_list(some_deque):
    for i in range(n):
        some_deque.extend([1, 2, 3])
    return some_deque


print(timeit('extend_list(some_lst.copy())', globals=globals(), number=100))    # 0.789507900015451
print(timeit('extend_list(some_deque.copy())', globals=globals(), number=100))  # 0.9448486000765115

""" Операции выполняются примерно за одно и тоже время, так как обе работают с концом списка, 
особой разницы в этих методах нет"""
###########################################################################
""" 2) сравнение операций appendleft, popleft, extendleft """

""" insert and appendleft """


def appendleft_list(some_lst):
    for i in range(n):
        some_lst.insert(0, i)
    return some_lst


def appendleft_deque(some_deque):
    for i in range(n):
        some_deque.appendleft(i)
    return some_deque


print(timeit('appendleft_list(some_lst.copy())', globals=globals(), number=1))        # 2.170305500039831
print(timeit('appendleft_deque(some_deque.copy())', globals=globals(), number=1))     # 0.010382000007666647

""" pop and popleft """


def popleft_list(some_lst):
    for i in range(n):
        some_lst.pop(i)
    return some_lst


def popleft_deque(some_deque):
    for i in range(n):
        some_deque.popleft()
    return some_deque


print(timeit('popleft_list(some_lst.copy())', globals=globals(), number=1))         # 0.9033141999971122
print(timeit('popleft_deque(some_deque.copy())', globals=globals(), number=1))      # 0.0038396999007090926

""" insert and extend """


def extendleft_list(some_lst):
    for i in range(n):
        some_lst.insert(0, [1, 2, 3])
    return some_lst


def extendleft_deque(some_deque):
    for i in range(n):
        some_deque.extendleft([1, 2, 3])
    return some_deque


print(timeit('extendleft_list(some_lst.copy())', globals=globals(), number=1))      # 1.1135680000297725
print(timeit('extendleft_deque(some_deque.copy())', globals=globals(), number=1))   # 0.004619100014679134

""" deque работает быстрее, так как затраты на выполнения операций будут сложности O(1), а у списка сложность - O(n)"""
###########################################################################
""" 3) сравнение операций получения элемента """


def get_elem_list(some_lst):
    for i in range(n):
        some_lst[i] = i
    return some_lst


def get_elem_deque(some_deque):
    for i in range(n):
        some_deque[i] = i
    return some_deque


print(timeit('get_elem_list(some_lst.copy())', globals=globals(), number=100))      # 0.25513569999020547
print(timeit('get_elem_deque(some_deque.copy())', globals=globals(), number=100))   # 0.45678669994231313

""" Список будет быстрее, так как deque – это набор связанных блоков памяти, где в каждом блоке памяти
 хранится более одного элемента. Список представляет собой набор элементов, рассеянных в памяти,
то есть только один элемент хранится в блоке памяти."""