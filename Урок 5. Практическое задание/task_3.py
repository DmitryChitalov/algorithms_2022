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

deque_list = deque()
simple_list = []


def append_chk(lists):
    for i in range(0, 100):
        lists.append(i)
    return f''


def pop_chk(lists):
    for i in range(0, 100):
        lists.pop()
    return f''


def extend_chk(lists):
    for i in range(0, 100):
        lists.extend([2])
    return f''


print('*' * 50)
print('Deque append', timeit('append_chk(deque_list)', number=10000, globals=globals()))
print('List append', timeit('append_chk(simple_list)', number=10000, globals=globals()))
print('-' * 50)
print('Deque pop', timeit('pop_chk(deque_list)', number=10000, globals=globals()))
print('List pop', timeit('pop_chk(simple_list)', number=10000, globals=globals()))
print('-' * 50)
print('Deque extend', timeit('extend_chk(deque_list)', number=10000, globals=globals()))
print('List extend', timeit('extend_chk(simple_list)', number=10000, globals=globals()))
print('*' * 50)
# append список немного медленнее, pop список немного быстрее, а вот extend список ощутимо быстрее.
# (делал несколько замеров с разным количеством number)

deque_list2 = deque()
simple_list2 = []


def appendleft_chk():
    for i in range(100):
        deque_list2.appendleft(i)
    return f''


def appendleft_listchk():
    for i in range(100):
        simple_list2.insert(0, i)
    return f''


def popleft_chk():
    for i in range(100):
        deque_list2.popleft()
    return f''


def popleft_listchk():
    for i in range(100):
        simple_list2.pop(0)
    return f''


def extendleft_chk():
    for i in range(100):
        deque_list2.extendleft([1])
    return f''


def extendleft_listchk():
    for i in range(100):
        simple_list2.insert(0, i)
    return f''


print(appendleft_chk())
print(appendleft_listchk())
print('*' * 50)
print('Deque appendleft', timeit('appendleft_chk()', number=100, globals=globals()))
print('List appendleft - insert', timeit('appendleft_listchk()', number=100, globals=globals()))
# appendleft - на несколько порядков быстрее

print(popleft_chk())
print(popleft_listchk())
print('Deque popleft', timeit('popleft_chk()', number=100, globals=globals()))
print('List popleft', timeit('popleft_listchk()', number=100, globals=globals()))
# appendleft - гораздо быстрее

print(extendleft_chk())
print(extendleft_listchk())
print('Deque extendleft', timeit('extendleft_chk()', number=100, globals=globals()))
print('Deque extendleft', timeit('extendleft_listchk()', number=100, globals=globals()))
# и тут список значительно уступает по скорости


def elem_deq_chk(n):
    return deque_list[n]


def elem_chk(n):
    return simple_list[n]


print(elem_deq_chk(10))
print(elem_chk(10))
print('Deque ', timeit('elem_deq_chk(10)', number=1000000, globals=globals()))
print('List ', timeit('elem_chk(10)', number=1000000, globals=globals()))
# получение элемента по индексу - список быстрее
