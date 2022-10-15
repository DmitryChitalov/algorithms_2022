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

test_lst = [i for i in range(10 ** 5)]
test_deque = deque([i for i in range(10 ** 5)])
num = 50

""" 1) append, pop, extend списка и дека """

# append

def append_to_lst(test_lst):
    for i in range(num):
        test_lst.append(i)
    return test_lst

def append_to_deq(test_deque):
    for i in range(num):
        test_deque.append(i)
    return test_deque

# pop

def pop_from_lst(lst_test):
    for i in range(num):
        lst_test.pop()
    return lst_test

def pop_from_deq(test_deque):
    for i in range(num):
        test_deque.pop()
    return test_deque

# extend

def extend_lst(test_lst):
    for i in range(num):
        test_lst.extend([1, 9])
    return test_lst

def extend_deq(test_deque):
    for i in range(num):
        test_deque.extend([1, 9])
    return test_deque


print(timeit("append_to_lst(test_lst)", globals=globals()))
print(timeit("append_to_deq(test_deque)", globals=globals()))
print(timeit("pop_from_lst(test_lst)", globals=globals()))
print(timeit("pop_from_deq(test_deque)", globals=globals()))
print(timeit("extend_lst(test_lst)", globals=globals()))
print(timeit("extend_deq(test_deque)", globals=globals()))

# Вывод: Операции append, pop, extend элементов списка и дека по времени примерно равны по скорости.


# 2
test_lst = [5, 15, 25, 35, 45, 55, 65, 75]
test_deque = deque('515253545556575')

num = 50

def insert_to_lst(test_lst):
    for i in range(num):
        test_lst.insert(0, i)
    return test_lst

def append_to_dq(test_deque):
    for i in range(num):
        test_deque.appendleft(i)
    return test_deque

# 2

def pop_from_lst(test_lst):
    for i in range(30):
        test_lst.pop(i)
    return test_lst

def pop_from_dq(test_deque):
    for i in range(num):
        test_deque.popleft()
    return test_deque

# 3

def extend_lst(test_lst):
    for i in range(30):
        test_lst.insert(0, [1, 9])
    return test_lst

def extend_dq(test_deque):
    for i in range(num):
        test_deque.extendleft([1, 9])
    return test_deque


print(timeit("insert_to_lst(test_lst)", globals=globals(), number=1000))
print(timeit("append_to_dq(test_deque)", globals=globals(), number=1000))
print(timeit("pop_from_lst(test_lst)", globals=globals(), number=1000))
print(timeit("pop_from_dq(test_deque)", globals=globals(), number=1000))
print(timeit("extend_lst(test_lst)", globals=globals(), number=1000))
print(timeit("extend_dq(test_deque)", globals=globals(), number=1000))

""" Замеры времени:
0.8613812000257894
0.005335499998182058
0.4254142999998294
0.006692899973131716
0.9146547000273131
0.01137720001861453

Вывод: операции с деком выполняются существенно быстрее"""

# 3
test_lst = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
test_deque = deque('5152535455565758595105')

num = 5

def get_from_lst(test_lst):
    for i in range(num):
        j = test_lst[i]

def get_from_dq(test_deque):
    for i in range(num):
        j = test_deque[i]


print(timeit("get_from_lst(test_lst)", globals=globals()))
print(timeit("get_from_dq(test_deque)", globals=globals()))

"""
0.7082617999985814
0.8606643999810331
Вывод: получение элемента из списка быстрее, чем из дека"""

