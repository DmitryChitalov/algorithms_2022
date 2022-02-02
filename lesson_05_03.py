from collections import deque
from random import randint
from timeit import timeit
# создайте простой список (list) и очередь (deque)
simple_list = []
deque_list = deque()
# 1) сравнить операции
# append, pop, extend списка и дека и сделать выводы что и где быстрее


def append_list(my_list=simple_list):
    for i in range(1000):
        my_list.append(i)


def append_deque(my_deque=deque_list):
    for i in range(1000):
        my_deque.appendleft(i)


def pop_list(my_list):
    for i in range(1000):
        my_list.pop(i)


def pop_deque(my_deque=deque_list):
    for i in range(1000):
        my_deque.pop(i)


def extend_list(list_1, list_2):
    for i in range(1000):
        list_1.extend(list_2)


def extend_deque(deque_1=deque(), deque_2=deque()):
    for i in range(1000):
        deque_1.extend(deque_2)


# append
print(f'Append_list: {timeit("append_list", "from __main__ import append_list", number=1000)}')
print(f'Append_deque: {timeit("append_deque", "from __main__ import append_deque", number=1000)}')
# pop
print(f'Pop_list: {timeit("pop_list", "from __main__ import pop_list", number=1000)}')
print(f'Pop_deque: {timeit("pop_deque", "from __main__ import pop_deque", number=1000)}')
# extend
print(f'Extend_list: {timeit("extend_list", "from __main__ import extend_list", number=1000)}')
print(f'Extend_deque: {timeit("extend_deque", "from __main__ import extend_deque", number=1000)}')

"""
Операции append, pop, extend списка и дека выполняются с примерно одинаковым временем
Append_list: 1.1000000000000593e-05
Append_deque: 1.1000000000000593e-05
Pop_list: 1.1000000000000593e-05
Pop_deque: 1.0900000000001187e-05
Extend_list: 1.0900000000001187e-05
Extend_deque: 1.1000000000000593e-05
"""

# 2) сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее


def appendleft_deque(my_deque=deque()):
    for i in range(1000):
        my_deque.appendleft(i)


def insert_list_left(my_list):
    for i in range(1000):
        my_list.insert(0, i)


def popleft_deque(my_deque=deque()):
    for i in range(1000):
        my_deque.popleft()


def pop_list_left(my_list):
    for i in range(1000):
        my_list.pop(0)


def extendleft_deque(deque_1=deque(), deque_2=deque()):
    for i in range(1000):
        deque_1.extendleft(deque_2)


def extendleft_list(list_1, list_2):
    for i in range(1000):
        for item in list_2:
            list_1.insert(0, item)


# append
print('*' * 20)
print(f'Insert_list_left: {timeit("insert_list_left", "from __main__ import insert_list_left", number=1000)}')
print(f'Appendleft_deque: {timeit("appendleft_deque", "from __main__ import appendleft_deque", number=1000)}')
# pop
print(f'Pop_list_left: {timeit("pop_list_left", "from __main__ import pop_list_left", number=1000)}')
print(f'Popleft_deque: {timeit("popleft_deque", "from __main__ import popleft_deque", number=1000)}')
# extend
print(f'Extendleft_list: {timeit("extendleft_list", "from __main__ import extendleft_list", number=1000)}')
print(f'Extendleft_deque: {timeit("extendleft_deque", "from __main__ import extendleft_deque", number=1000)}')

"""
Операции списка и дека так же выполняются с примерно одинаковым временем
Insert_list_left: 1.1000000000000593e-05
Appendleft_deque: 1.0900000000001187e-05
Pop_list_left: 1.1000000000000593e-05
Popleft_deque: 1.1000000000000593e-05
Extendleft_list: 1.0900000000001187e-05
Extendleft_deque: 1.0899999999997717e-05
"""

# 3) сравнить операции получения элемента списка и дека и сделать выводы что и где быстрее

from_list = [randint(1, 100) for i in range(20)]
from_deque = deque(from_list)


def take_from_list(lst=from_list):
    idx = randint(1, len(lst))
    return lst[idx]


def take_from_deque(dq=from_deque):
    idx = randint(1, len(dq))
    return dq[idx]


print(f'Take from list: {timeit("take_from_list", "from __main__ import take_from_list", number=1000)}')
print(f'Take from deque: {timeit("take_from_deque", "from __main__ import take_from_deque ", number=1000)}')

"""
Получение из дека немного быстрее, чем из списка
Take from list: 1.1000000000000593e-05
Take from deque: 1.0900000000001187e-05
"""
