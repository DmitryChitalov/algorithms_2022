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

my_lst = []
my_deq = deque()


# Часть 1
# append, pop, extend списка и дека
def fill_lst(lst):
    for i in range(1100):
        lst.append(i)
    return lst


def fill_deq(deq):
    for i in range(1100):
        deq.append(i)
    return deq


fill_lst(my_lst)
fill_deq(my_deq)
print(f'append для списка: {timeit("fill_lst(my_lst)", globals=globals(), number=1000)}')
print(f'append для deque: {timeit("fill_deq(my_deq)", globals=globals(), number=1000)}')
"""
append для списка: 0.15198090000194497
append для deque: 0.08521330001531169
Заполнение Deque происходит быстрее
"""


def lst_pop(lst):
    for i in range(10):
        lst.pop()
    return lst


def deq_pop(deq):
    for i in range(10):
        deq.pop()
    return deq


# print(timeit("lst_pop(my_lst)", globals=globals(), number=100))
# print(timeit("deq_pop(my_deq)", globals=globals(), number=100))
"""
0.00019079999765381217
0.00017129999469034374
Метод pop для Deque работает быстрее
"""


def lst_extend(lst):
    for i in range(10):
        lst.extend('abcd')
    return lst


def deq_extend(deq):
    for i in range(10):
        deq.extend('abcd')
    return deq


# print(timeit("lst_extend(my_lst)", globals=globals(), number=100))
# print(timeit("deq_extend(my_deq)", globals=globals(), number=100))
"""
0.00023950000468175858
0.0004481000069063157
Добавдение элементов в начало для Deque быстрее
"""


# Часть 2:
# appendleft, popleft, extendleft
def deq_app_left(deq):
    for i in range(5):
        deq.appendleft(i)
    return deq


def lst_app_left(lst):
    for i in range(5):
        lst.insert(0, i)
    return lst


# print(timeit("deq_app_left(my_deq)", globals=globals(), number=100))
# print(timeit("lst_app_left(my_lst)", globals=globals(), number=100))
"""
0.0001353999978164211
0.0006766000005882233
append left для Deque быстрее, чем insert для списка
"""


def deq_popleft(deq):
    for i in range(10):
        deq.popleft()
    return deq


def lst_popleft(lst):
    for i in range(10):
        lst.pop(0)
    return lst


# print(timeit("deq_popleft(my_deq)", globals=globals(), number=100))
# print(timeit("lst_popleft(my_lst)", globals=globals(), number=100))
"""
0.0001171000039903447
0.0004616000078385696
Deque.Popleft быстрее
"""


def deq_ext_left(deq, seq):
    for i in range(2):
        deq.extendleft(seq)
    return deq


def lst_ext_left_insert(lst, seq):
    for i in range(2):
        for el in seq:
            lst.insert(0, el)
    return lst


# print(timeit("deq_ext_left(my_deq, 'abcd')", globals=globals(), number=100))
# print(timeit("lst_ext_left_insert(my_lst, 'abcd')", globals=globals(), number=100))
"""
0.00012670000432990491
0.0007976999913807958
Deque.extendleft - быстрее
"""


# Часть 3:
# сравнить операции получения элемента списка и дека
def get_lst_el(lst, val):
    for i in range(len(lst)):
        if lst[i] == val:
            el = lst.pop(i)
            return el


def get_deq_el(deq, val):
    for i in range(len(deq)):
        if deq[i] == val:
            el = deq[i]
            del deq[i]
            return el


# print(timeit("get_deq_el(my_deq, 15)", globals=globals(), number=100))
# print(timeit("get_lst_el(my_lst, 15)", globals=globals(), number=100))
"""
0.013715599998249672
0.01096299999335315
Получение произвольного элемента списка работает быстрее.
"""
