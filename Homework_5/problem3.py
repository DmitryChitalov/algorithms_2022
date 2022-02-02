from timeit import timeit
from collections import deque

lst = []
deq = deque()

def func_1_lst():
    return lst.append(1)
def func_1_deq():
    return deq.append(1)

def func_2_lst():
    return lst.pop()
def func_2_deq():
    return deq.pop()

def func_3_lst():
    return lst.extend('a')
def func_3_deq():
    return deq.extend('a')

def func_11_lst():
    return lst.insert(1, 0)
def func_11_deq():
    return deq.appendleft(1)

def func_22_lst():
    return lst.pop(-1)
def func_22_deq():
    return deq.popleft()

def func_33_lst():
    return lst.insert(0, 'a')
def func_33_deq():
    return deq.extendleft('a')

def func_111_lst():
    return lst[0]
def func_111_deq():
    return deq[0]

print(timeit('func_1_lst()', number=100000, globals=globals()) - timeit('func_1_deq()', number=100000, globals=globals()))
print(timeit('func_2_lst()', number=100000, globals=globals()) - timeit('func_2_deq()', number=100000, globals=globals()))
print(timeit('func_3_lst()', number=100000, globals=globals()) - timeit('func_3_deq()', number=100000, globals=globals()))

print(timeit('func_11_lst()', number=100000, globals=globals()) - timeit('func_11_deq()', number=100000, globals=globals()))
print(timeit('func_22_lst()', number=100000, globals=globals()) - timeit('func_22_deq()', number=100000, globals=globals()))
print(timeit('func_33_lst()', number=100000, globals=globals()) - timeit('func_33_deq()', number=100000, globals=globals()))

print(timeit('func_111_lst()', number=100000, globals=globals()) - timeit('func_111_deq()', number=100000, globals=globals()))

# Существенно отличаются по времени только insert и appendleft и insert и extendleft, всё это так, потому что
# insert имеет сложность O(n), а соответствующие функции в dec только О(1).
