"""
задача 3.
в соответствии с документацией python,
deque – это обобщение стеков и очередей.
вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
если вам нужен быстрый случайный доступ, используйте list

задача: создайте простой список (list) и очередь (deque).
выполните различные операции с каждым из объектов.
сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. для замеров используйте timeit.
"""
import collections
from timeit import timeit


def list_append(ls):
    for i in range(1000):
        ls.append(i)
    return ls


def deq_append(dq):

    for i in range(1000):
        dq.append(i)
    return dq


def list_pop(ls):
    while len(ls) > 0:
        ls.pop()


def deq_pop(dq):
    while len(dq) > 0:
        dq.pop()


def list_extend(ls):
    ls.extend(ls)


def deq_extend(dq, ls):
    dq.extend(ls)


def list_append_left(ls):
    for i in range(1000):
        ls.insert(0, i)
    return ls


def deq_append_left(dq):
    for i in range(1000):
        dq.appendleft(i)
    return dq


def list_pop_left(ls):
    while len(ls) > 0:
        ls.pop(0)


def deq_pop_left(dq):
    while len(dq) > 0:
        dq.popleft()


def list_extend_left(ls):
    ls_rev = ls.copy()
    ls_rev.reverse()
    ls = ls_rev + ls
    return ls


def deq_extend_left(dq, ls):
    dq.extendleft(ls)
    return dq


def list_get_elem(ls):
    for i in range(len(ls)):
        a = ls[i]


def dq_get_elem(dq):
    for i in range(len(dq)):
        a = dq[i]


lst = list_append(list())
deq = deq_append(collections.deque())

print(f'Время работы функции {list_append.__name__} - {timeit("list_append(list())", globals=globals(), number=10000)}')
print(f'Время работы функции {deq_append.__name__} - {timeit("deq_append(collections.deque())", globals=globals(), number=10000)}')
print(f'Время работы функции {list_pop.__name__} - {timeit("list_pop(lst)", globals=globals(), number=10000)}')
print(f'Время работы функции {deq_pop.__name__} - {timeit("deq_pop(deq)", globals=globals(), number=10000)}')
print(f'Время работы функции {list_extend.__name__} - {timeit("list_extend(lst)", globals=globals(), number=10000)}')
print(f'Время работы функции {deq_extend.__name__} - {timeit("deq_extend(deq, lst)", globals=globals(), number=10000)}')
print(f'Время работы функции {list_append_left.__name__} - {timeit("list_append_left(lst)", globals=globals(), number=100)}')
print(f'Время работы функции {deq_append_left.__name__} - {timeit("deq_append_left(deq)", globals=globals(), number=100)}')
print(f'Время работы функции {list_pop_left.__name__} - {timeit("list_pop_left(lst)", globals=globals(), number=10000)}')
print(f'Время работы функции {deq_pop_left.__name__} - {timeit("deq_pop_left(deq)", globals=globals(), number=10000)}')
print(f'Время работы функции {list_extend_left.__name__} - {timeit("list_extend_left(lst)", globals=globals(), number=10000)}')
print(f'Время работы функции {deq_extend_left.__name__} - {timeit("deq_extend_left(deq, lst)", globals=globals(), number=10000)}')
print(f'Время работы функции {list_get_elem.__name__} - {timeit("list_get_elem(lst)", globals=globals(), number=10000)}')
print(f'Время работы функции {dq_get_elem.__name__} - {timeit("dq_get_elem(deq)", globals=globals(), number=10000)}')

"""
ЗАМЕРЫ

Время работы функции list_append - 1.5874207000015303
Время работы функции deq_append - 1.3561554000043543
Время работы функции list_pop - 0.003757500002393499
Время работы функции deq_pop - 0.0028473999991547316
Время работы функции list_extend - 0.004780499992193654
Время работы функции deq_extend - 0.004717899995739572
Время работы функции list_append_left - 5.038497700006701
Время работы функции deq_append_left - 0.012487500003771856
Время работы функции list_pop_left - 2.7888112000073306
Время работы функции deq_pop_left - 0.03243750000547152
Время работы функции list_extend_left - 0.0059403999912319705
Время работы функции deq_extend_left - 0.00532779999775812
Время работы функции list_get_elem - 0.005423299997346476
Время работы функции dq_get_elem - 0.005451999997603707

ВЫВОДЫ

1) метод append в deque работает быстрее
2) метод pop в deque работает быстрее
3) метод extend показал одинаковое время работы
4) метод appendleft в разы быстрее в deque
5) метод popleft в разы быстрее в deque
6) метод extendleft немного быстрее, предполагаю что с увеличением размера будет увеличиваться и разница во времени
7) получение элемента показало одинаковое время работы

"""