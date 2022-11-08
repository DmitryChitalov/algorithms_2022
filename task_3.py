from collections import deque
from timeit import timeit


lst = [i for i in range(10 ** 2)]
deq = deque(lst)
"""
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
"""


def append_lst(lst):
    for i in range(100):
        lst.append(i)
    return lst


def append_deq(deq):
    for i in range(100):
        deq.append(i)
    return deq


def pop_lst(lst):
    for i in range(10000):
        lst.pop(i)
    return lst


def pop_deq(deq):
    for i in range(10000):
        deq.pop()
    return deq


def extand_lst(lst, lst_2):
    for i in range(100):
        lst.extand(lst_2)
    return lst


def extand_deq(deq, deq_2=deque()):
    for i in range(100):
        deq.extand(deq_2)
    return deq


print(timeit("append_lst", globals=globals()))
print(timeit("append_deq", globals=globals()))
print(timeit("pop_lst", globals=globals()))
print(timeit("pop_deq", globals=globals()))
print(timeit("extand_lst", globals=globals()))
print(timeit("extand_deq", globals=globals()))

"""
append_lst: 0.021646299999999993
append_deq: 0.021311899999999995
pop_lst:    0.022587300000000005
pop_deq:    0.022980299999999995
extand_lst: 0.017995800000000006
extand_deq: 0.0167514
Вывод: функции append, pop, extend по скорости работают примерно одинакого.
"""

"""
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
"""


def insert_lst(lst):
    for i in range(1000):
        lst.insert(0, i)
    return lst


def appendleft_deq(deq):
    for i in range(1000):
        deq.appendleft(0, i)
    return deq


def popleft_lst(lst):
    for i in range(1000):
        lst.pop(i)
    return lst


def popleft_deq(deq):
    for i in range(1000):
        deq.popleft()
    return deq


def extendleft_lst(lst, lst_2):
    for i in range(1000):
        for i in lst_2:
            lst.insert(0, i)
        return lst_2


def extendleft_deq(deq):
    for i in range(1000):
        deq.extendleft(i)
    return deq


print(timeit("insert_lst", globals=globals()), '--')
print(timeit("appendleft_deq", globals=globals()))
print(timeit("popleft_lst", globals=globals()))
print(timeit("popleft_deq", globals=globals()))
print(timeit("extendleft_lst", globals=globals()))
print(timeit("extendleft_deq", globals=globals()))

"""
insert_lst:     0.03298200000000001 
appendleft_deq: 0.020979199999999976
popleft_lst:    0.020371100000000003
popleft_deq:    0.018925499999999984
extendleft_lst: 0.021589100000000028
extendleft_deq: 0.01603739999999998
Вывод: Скорость исполнения операций дека appendleft, popleft, extendleft немного быстрее,
чем соответствующие операций списка.
"""



"""
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
"""


def from_lst(x):
    for i in range(len(lst)):
        lst[i] = x
    return x


def from_deq(x):
    for i in range(len(deq)):
        deq[i] = x
    return x


print(timeit("from_lst", globals=globals()))
print(timeit("from_deq", globals=globals()))

"""
from_lst: 0.01639299999999999
from_deq: 0.018506199999999973
Вывод: извлечение элемента немного быстрее из списка, чем из дека.
"""