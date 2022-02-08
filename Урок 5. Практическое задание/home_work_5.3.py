from collections import deque
from timeit import timeit

some_lst = [i for i in range(10 ** 5)]
some_deque = deque([i for i in range(10 ** 5)])
n = 10 ** 4


def append_list(some_lst):
    for i in range(n):
        some_lst.append(i)
    return some_lst


def append_deque(some_deque):
    for i in range(n):
        some_deque.append(i)
    return some_deque


print(timeit('append_list(some_lst.copy())', globals=globals(), number=100))
print(timeit('append_deque(some_deque.copy())', globals=globals(), number=100))


#0.283786087
#0.180927189


def pop_list(some_lst):
    for i in range(n):
        some_lst.pop()
    return some_lst


def pop_deque(some_deque):
    for i in range(n):
        some_deque.pop()
    return some_deque


print(timeit('pop_list(some_lst.copy())', globals=globals(), number=100))
print(timeit('pop_deque(some_deque.copy())', globals=globals(), number=100))


#0.12560069299999999
#0.15177174300000007


def extend_list(some_lst):
    for i in range(n):
        some_lst.extend([1, 2, 3])
    return some_lst


def extend_list(some_deque):
    for i in range(n):
        some_deque.extend([1, 2, 3])
    return some_deque


print(timeit('extend_list(some_lst)', globals=globals(), number=100))
print(timeit('extend_list(some_deque)', globals=globals(), number=100))


#0.119039848
#0.1495039079999999

def appendleft_list(some_lst):
    for i in range(n):
        some_lst.insert(0, i)
    return some_lst


def appendleft_deque(some_deque):
    for i in range(n):
        some_deque.appendleft(i)
    return some_deque


print(timeit('appendleft_list(some_lst.copy())', globals=globals(), number=100))
print(timeit('appendleft_deque(some_deque.copy())', globals=globals(), number=100))


#1959.244647379
#3.826113940999903


def popleft_list(some_lst):
    for i in range(n):
        some_lst.pop(i)
    return some_lst


def popleft_deque(some_deque):
    for i in range(n):
        some_deque.popleft()
    return some_deque


print(timeit('popleft_list(some_lst.copy())', globals=globals(), number=3))
print(timeit('popleft_deque(some_deque.copy())', globals=globals(), number=3))


#42.503722677
#0.11827351799999519


def extendleft_list(some_lst):
    for i in range(n):
        some_lst.insert(0, [1, 2, 3])
    return some_lst


def extendleft_deque(some_deque):
    for i in range(n):
        some_deque.extendleft([1, 2, 3])
    return some_deque


print(timeit('extendleft_list(some_lst.copy())', globals=globals(), number=100))
print(timeit('extendleft_deque(some_deque.copy())', globals=globals(), number=100))


#1978.014829206
#3.913253245000078


def get_elem_list(some_lst):
    for i in range(n):
        some_lst[i] = i
    return some_lst


def get_elem_deque(some_deque):
    for i in range(n):
        some_deque[i] = i
    return some_deque


print(timeit('get_elem_list(some_lst.copy())', globals=globals(), number=100))
print(timeit('get_elem_deque(some_deque.copy())', globals=globals(), number=100))

#1.1310922710001705
#3.759331495999959
