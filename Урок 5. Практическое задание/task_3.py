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

import random
from collections import deque
from timeit import timeit

some_list = []
some_deq = deque()

test_num = random.randint(-100, 100)


def list_append(some_list, test_num):
    for i in range(1000):
        some_list.append(test_num)


def deq_append(some_deq, test_num):
    for i in range(1000):
        some_deq.append(test_num)


def list_pop(some_list):
    for i in range(500):
        some_list.pop(len(some_list) - 1)


def deq_pop(some_deq):
    for i in range(500):
        some_deq.pop()


def list_extend(some_list):
    for i in range(1000):
        some_list.extend(['A', 'B', 'C', 'D'])


def deq_extend(some_deq):
    for i in range(1000):
        some_deq.extend(['A', 'B', 'C', 'D'])


print('list_append')
print(timeit("list_append(some_list, test_num)", globals=globals(), number=10000))

print('deq_append')
print(timeit("deq_append(some_deq, test_num)", globals=globals(), number=10000))

print('list_pop')
print(timeit("list_pop(some_list)", globals=globals(), number=10000))

print('deq_pop')
print(timeit("deq_pop(some_deq)", globals=globals(), number=10000))

print('list_extend')
print(timeit("list_extend(some_list)", globals=globals(), number=10000))

print('deq_extend')
print(timeit("deq_extend(some_deq)", globals=globals(), number=10000))

print('-------------------------------------------------------------')

some_list = []
some_deq = deque()


def list_insertleft(some_list, test_num):
    for i in range(10):
        some_list.insert(0, test_num)


def deq_appendleft(some_deq, test_num):
    for i in range(10):
        some_deq.appendleft(test_num)


def list_popleft(some_list):
    for i in range(5):
        some_list.pop(0)


def deq_popleft(some_deq):
    for i in range(5):
        some_deq.popleft()


# не уверен, что это верная альтернатива extendleft, очевидно, быстродействие катастрофически плохое
def list_extendleft(some_list):
    for i in range(10):
        for j in ['A', 'B', 'C', 'D']:
            some_list.insert(0, j)


def deq_extendleft(some_deq):
    for i in range(10):
        some_deq.extendleft(['A', 'B', 'C', 'D'])


print('list_insertleft')
print(timeit("list_insertleft(some_list, test_num)", globals=globals(), number=10000))

print('deq_appendleft')
print(timeit("deq_appendleft(some_deq, test_num)", globals=globals(), number=10000))

print('list_popleft')
print(timeit("list_popleft(some_list)", globals=globals(), number=10000))

print('deq_popleft')
print(timeit("deq_popleft(some_deq)", globals=globals(), number=10000))

print('list_extendleft')
print(timeit("list_extendleft(some_list)", globals=globals(), number=10000))

print('deq_extendleft')
print(timeit("deq_extendleft(some_deq)", globals=globals(), number=10000))

print('----------------------------------------------')

some_list = []
some_deq = deque()
for i in range(1000):
    some_list.append(i)
    some_deq.append(i)


def list_search(some_list):
    for i in range(200, 600):
        a = some_list[i]


def deq_search(some_deq):
    for i in range(200, 600):
        a = some_deq[i]


print('list_search')
print(timeit("list_search(some_list)", globals=globals(), number=100000))

print('deq_search')
print(timeit("deq_search(some_deq)", globals=globals(), number=100000))

# Вывод: deque дает от существенного до огромного выигрыша в быстродействии при работе с "краями списка",
# но при обращении к случайным элементам проигрывает.
