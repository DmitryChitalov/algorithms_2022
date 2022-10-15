"""2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее"""

from collections import deque
from timeit import timeit

test_lst = [5, 15, 25, 35, 45, 55, 65, 75]
test_deque = deque('515253545556575')

num = 50

# 1

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