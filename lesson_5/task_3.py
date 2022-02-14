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

# Пункт 1 ----------------------------------------------------------------------------------------


def list_append():
    for i in range(100):
        test_list.append(i)
    return test_list


def list_pop():
    for i in range(100):
        test_list.pop()
    return test_list


def list_extend():
    test_list.extend(test_list)
    return test_list


def deque_append():
    for i in range(100):
        test_deque.append(i)
    return test_deque


def deque_pop():
    for i in range(100):
        test_deque.pop()
    return test_deque


def deque_extend():
    test_deque.extend(test_deque)
    return test_deque


test_list = []
test_deque = deque()

print(f'list_append() = {timeit("list_append()", globals=globals(), number=100000)}')
print(f'list_pop() = {timeit("list_pop()", globals=globals(), number=100000)}')
print(f'list_extend() = {timeit("list_extend()", globals=globals(), number=100000)}')
print(f'deque_append() = {timeit("deque_append()", globals=globals(), number=100000)}')
print(f'deque_pop() = {timeit("deque_pop()", globals=globals(), number=100000)}')
print(f'deque_extend() = {timeit("deque_extend()", globals=globals(), number=100000)}')
""" 
list_append = 0.8254544
list_pop = 0.5448222
list_extend = 0.021934200000000006
deque_append() = 0.7325800000000001
deque_pop() = 0.5418468000000001
deque_extend() = 0.022877400000000048

Замеры приблизительно совпадают по времени
"""

# Пункт 2 -------------------------------------------------------------------------------------------


def list_append_left():
    for i in range(100):
        test_list_2.insert(0, i)
    return test_list_2


def list_pop_left():
    for i in range(100):
        del test_list_2[0]
    return test_list_2


def list_extend_left_():
    for i in range(100):
        test_list_2.insert(0, test_list_2)
    return test_list_2


def deque_append_left():
    for i in range(100):
        test_deque_2.appendleft(i)
    return test_deque_2


def deque_pop_left():
    for i in range(100):
        test_deque_2.popleft()
    return test_deque_2


def deque_extend_left():
    for i in range(100):
        test_deque_2.extendleft(test_deque_2)
    return test_deque_2


test_list_2 = []
test_deque_2 = deque()

print(f'list_append_left = {timeit("list_append_left()", globals=globals(), number=100)}')
print(f'list_pop_left() = {timeit("list_pop_left()", globals=globals(), number=100)}')
print(f'list_extend_left_() = {timeit("list_extend_left_()", globals=globals(), number=100)}')
print(f'deque_append_left() = {timeit("deque_append_left()", globals=globals(), number=100)}')
print(f'deque_pop_left() = {timeit("deque_pop_left()", globals=globals(), number=100)}')
print(f'deque_extend_left() = {timeit("deque_extend_left()", globals=globals(), number=100)}')

"""
list_append_left = 0.0352424
list_pop_left() = 0.014940099999999998
list_extend_left_() = 0.03514510000000001
deque_append_left() = 0.0006743999999999917
deque_pop_left() = 0.0006062000000000012
deque_extend_left() = 0.0016401000000000054

В deque данные операции быстрее(из-за константной сложности), 
чем в обычном списке(у которого линейная сложность).
"""

# Пункт 3 -------------------------------------------------------------------------------------------


def list_3_append():
    for i in range(100):
        test_list_3.append(i)
    return test_list_3


def deque_3_append():
    for i in range(100):
        test_deque_3.append(i)
    return test_deque_3


def list_get():
    for i in range(100):
        test_list_3[i] = i


def deque_get():
    for i in range(100):
        test_deque_3[i] = i


test_list_3 = []
list_3_append()
test_deque_3 = deque()
deque_3_append()

print(f'list_get() = {timeit("list_get()", globals=globals(), number=100000)}')
print(f'deque_get() = {timeit("deque_get()", globals=globals(), number=100000)}')

"""
list_get() = 0.4034311
deque_get() = 0.5066318000000001

Время выполнения функции у обычного списка быстрее.
"""
