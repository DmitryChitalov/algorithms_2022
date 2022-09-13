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


def append_dq(count):
    my_dq = deque()
    for i in range(count):
        my_dq.append(f'{i}-й элемент')
    return my_dq


def append_list(count):
    my_list = []
    for i in range(count):
        my_list.append(f'{i}-й элемент')
    return my_list


counts = 1000
new_dq = append_dq(counts)
new_list = append_list(counts)
print(f"append deque: {timeit('append_dq(counts)', globals=globals())}")
print(f"append list: {timeit('append_list(counts)',globals=globals())}")
"""
append deque: 35.42088380001951
append list: 34.31696809999994
добавление элементов в конец списка и дека происходит примерно одинаково по времени.
но добавление в список немного быстрее
"""


def pop_dq(count):
    my_dq = new_dq.copy()
    for _ in range(count):
        my_dq.pop()


def pop_list():
    my_list = new_list.copy()
    for _ in enumerate(new_list):
        my_list.pop()


print(f'pop deque: {timeit("pop_dq(counts)",globals=globals())}')
print(f'pop list: {timeit("pop_list()",globals=globals())}')
"""
pop deque: 7.9709023000032175
pop list: 14.15626279998105
удаление последнего элемента в деке происходит почти в два раза быстрее
"""


def extend_dq(count):
    my_dq = deque()
    for i in range(count):
        my_dq.extend([i, i ** i])


def extend_list(count):
    my_list = []
    for i in range(count):
        my_list.extend([i, i ** i])


print(f'extend deque: {timeit("extend_dq(counts)",globals=globals())}')
print(f'extend list: {timeit("extend_list(counts)",globals=globals())}')
"""
extend deque: 118.00637300001108
extend list: 134.80544260001625
Добавление списка в конец дека происходит значительно быстрее
"""


def appendleft_dq(count):
    my_dq = deque()
    for i in range(count):
        my_dq.appendleft(i)


def ins_list(count):
    my_list = []
    for i in range(count):
        my_list.insert(0, f'{i}-й элемент')


def popleft_dq(count):
    my_dq = new_dq.copy()
    for _ in range(count):
        my_dq.popleft()


def popleft_list(count):
    my_list = new_list.copy()
    for _ in range(count):
        my_list.pop(0)


print(f'appendleft deque: {timeit("appendleft_dq(counts)",globals=globals())}')
print(f'insert list: {timeit("ins_list(counts)",globals=globals())}')
"""
appendleft deque: 8.150470399996266
insert list: 43.404609999997774
добавление в начало дека происходит намного быстрее, чем добавление элемента в начало списка
"""

print(f'popleft deque: {timeit("popleft_dq(counts)",globals=globals())}')
print(f'pop(0) list: {timeit("popleft_list(counts)",globals=globals())}')
"""
popleft deque: 9.111108899989631
pop(0) list: 19.238804099994013
Удаление из начала дека происходит значительно быстрее, чем удаление из начала списка
"""


def elem_dq():
    elem = 0
    for el in new_dq:
        elem = el
    return elem


def elem_list():
    elem = 0
    for el in new_list:
        elem = el
    return elem


print(f'element deque: {timeit("elem_dq()",globals=globals())}')
print(f'element list: {timeit("elem_list()",globals=globals())}')
"""
element deque: 2.900947799993446
element list: 2.5145664000010584
Получение элемента дека происходит немного медленнее, чем получение элемента списка
"""
