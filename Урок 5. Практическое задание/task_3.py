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

"""1) операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
"""


def append_lst(lst):
    for i in range(1000):
        lst.append(i)
    return lst


def pop_lst(lst):
    for i in range(1000):
        lst.pop()
    return lst


def extend_lst(lst):
    lst.extend([i for i in range(100)])
    return lst


def append_dq(dq):
    for i in range(1000):
        dq.append(i)
    return dq


def pop_dq(dq):
    for i in range(1000):
        dq.pop()
    return dq


def extend_dq(dq):
    dq.extend([i for i in range(100)])
    return dq


"""2) операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
"""


def appendleft_lst(lst):
    for i in range(100):
        lst.insert(0, i)
    return lst


def popleft_lst(lst):
    for i in range(100):
        lst.pop(0)
    return lst


def extendleft_lst(lst):
    lst.insert(0, [i for i in range(100)])
    return lst


def appendleft_dq(dq):
    for i in range(100):
        dq.appendleft(i)
    return dq


def popleft_dq(dq):
    for i in range(100):
        dq.popleft()
    return dq


def extendleft_dq(dq):
    dq.extendleft([i for i in range(100)])
    return dq


"""3) операции получения элемента списка и дека
и сделать выводы что и где быстрее
"""


def get_index_lst(lst):
    el = 0
    for i in range(1000):
        el = lst[i]
    return lst


def get_index_dq(dq):
    el = 0
    for i in range(1000):
        el = dq[i]
    return dq


temp_list = [i for i in range(10 ** 5)]
temp_deque = deque(temp_list)

print('append_lst: ', timeit("append_lst(temp_list)", globals=globals(), number=1000))
print('append_dq: ', timeit("append_dq(temp_deque)", globals=globals(), number=1000))
"""
append_lst:  0.051886399975046515
append_dq:  0.04188299999805167

deque показала лучшие результаты. Разница незначительная.
"""

print('pop_lst: ', timeit("pop_lst(temp_list)", globals=globals(), number=1000))
print('pop_dq: ', timeit("pop_dq(temp_deque)", globals=globals(), number=1000))
"""
pop_lst:  0.050993299984838814
pop_dq:  0.045641700009582564

deque показала лучшие результаты. Разница незначительная.
"""
print('extend_lst: ', timeit("extend_lst(temp_list)", globals=globals(), number=1000))
print('extend_dq: ', timeit("extend_dq(temp_deque)", globals=globals(), number=1000))
"""
extend_lst:  0.0037580000062007457
extend_dq:  0.002816799998981878

deque показала лучшие результаты. Разница незначительная.
"""

print('appendleft_lst: ', timeit("appendleft_lst(temp_list)", globals=globals(), number=100))
print('appendleft_dq: ', timeit("appendleft_dq(temp_deque)", globals=globals(), number=100))
"""
appendleft_lst:  0.808130399993388
appendleft_dq:  0.000606699992204085

deque показала лучшие результаты. Разница более чем в тысячу раз.
"""

print('popleft_lst: ', timeit("popleft_lst(temp_list)", globals=globals(), number=100))
print('popleft_dq: ', timeit("popleft_dq(temp_deque)", globals=globals(), number=100))
"""
popleft_lst:  1.391946599993389
popleft_dq:  0.00036880001425743103

deque показала лучшие результаты. Разница более чем в две тысячи.
"""

print('extendleft_lst: ', timeit("extendleft_lst(temp_list)", globals=globals(), number=100))
print('extendleft_dq: ', timeit("extendleft_dq(temp_deque)", globals=globals(), number=100))
"""
extendleft_lst:  0.007147399999666959
extendleft_dq:  0.00028169999131932855

deque показала лучшие результаты. Разница в 37 раз.
"""

print('get_index_lst: ', timeit("get_index_lst(temp_list)", globals=globals(), number=1000))
print('get_index_dq: ', timeit("get_index_dq(temp_deque)", globals=globals(), number=1000))
"""
get_index_lst:  0.029028699995251372
get_index_dq:  0.03419269999722019

list справился не много лучше, как и написано в документации.
"""
