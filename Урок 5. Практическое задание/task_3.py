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

"""
1.
"""

"""
list
"""


def app_to_lst(lst: list):
    for i in range(100):
        lst.append(i)
    return lst


def pop_from_lst(lst: list):
    for i in range(100):
        lst.pop()
    return lst


def ext_to_lst(lst: list):
    for i in range(100):
        lst.extend([1, 10])
    return  lst


"""
degue
"""


def app_to_deq(deq: deque):
    for i in range(100):
        deq.append(i)
    return deq


def pop_from_deq(deq: deque):
    for i in range(100):
        deq.pop()
    return deq


def ext_to_deq(deq: deque):
    for i in range(100):
        deq.extend([1, 10])
    return deq


lst_1 = [i for i in range(10 ** 3)]
deque_1 = deque([i for i in range(10 ** 3)])
print(timeit("app_to_lst(lst_1)", globals=globals()))
print(timeit("app_to_deq(deque_1)", globals=globals()))
print(timeit("pop_from_lst(lst_1)", globals=globals()))
print(timeit("pop_from_deq(deque_1)", globals=globals()))
print(timeit("ext_to_lst(lst_1)", globals=globals()))
print(timeit("ext_to_deq(deque_1)", globals=globals()))

"""
4.429315700002917
3.0658401000000595
2.7875725999983842
2.872035099997447
8.78767290000178
7.525394199998118
"""

"""
Разницы практически нет
"""

"""
2.
"""

"""
list
"""


def insert_to_lst(lst: list):
    for i in range(100):
        lst.insert(0, i)
    return lst


def pop_from_lst_2(lst: list):
    for i in range(100):
        lst.pop(i)
    return lst


def extend_lst(lst: list):
    for i in range(100):
        lst.insert(0, [1, 10])
    return lst


"""
deque
"""


def append_left_to_dq(deq: deque):
    for i in range(100):
        deq.appendleft(i)
    return deq


def pop_left_from_dq(deq: deque):
    for i in range(100):
        deq.popleft()
    return deq


def extend_left_dq(deq: deque):
    for i in range(100):
        deq.extendleft([1, 10])
    return deq


lst_2 = [i for i in range(10 ** 3)]
deque_2 = deque([i for i in range(10 ** 3)])
print(timeit("insert_to_lst(lst_2)", globals=globals(), number=1000))
print(timeit("append_left_to_dq(deque_2)", globals=globals(), number=1000))
print(timeit("pop_from_lst_2(lst_2)", globals=globals(), number=1000))
print(timeit("pop_left_from_dq(deque_2)", globals=globals(), number=1000))
print(timeit("extend_lst(lst_2)", globals=globals(), number=1000))
print(timeit("extend_left_dq(deque_2)", globals=globals(), number=1000))


"""
1.4165528000012273
0.003361300001415657
9.658785099996749
0.0030573000003641937
1.3708291000002646
0.006720500001392793
"""

"""
Если в 1 пункте разницы между list и deque  практически не было, то сейчас разница огромна
"""

"""
3.
"""


"""
list
"""


def get_lst(lst):
    for i in range(100):
        num = lst[i]
    return num


"""
deque
"""


def get_deque(deq):
    for i in range(100):
        num = deq[i]
    return num


lst_3 = [i for i in range(10 ** 3)]
deque_3 = deque([i for i in range(10 ** 3)])
print(timeit("get_lst(lst_3)", globals=globals(), number=1000))
print(timeit("get_deque(deque_3)", globals=globals(), number=1000))


"""
0.001985499999136664
0.002621499999804655
"""

"""
Получение элемента из list быстрее чем из deque
"""