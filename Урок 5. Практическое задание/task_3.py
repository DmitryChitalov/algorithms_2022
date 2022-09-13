from collections import deque
from timeit import timeit

lst = [i for i in range(10000)]
deq = deque(lst)
# 1) сравнить операции
# append, pop, extend списка и дека и сделать выводы что и где быстрее
# lst.append('i')
# deq.append('q')
# lst.pop()
# deq.pop()
# lst.extend(['z', 'g', 'u'])
# deq.extend(['y', 'm', 'j'])


def appnd_lst():
    for i in range(1000):
        lst.append(i)


def deq_appnd():
    for i in range(1000):
        deq.append(i)


def pop_lst():
    for i in range(1000):
        lst.pop()


def pop_deq():
    for i in range(1000):
        deq.pop()


def lst_extend():
    ext = [i for i in range(1000)]
    lst.extend(ext)


def deq_extend():
    ext = [i for i in range(1000)]
    deq.extend(ext)


print(timeit("appnd_lst()", globals=globals(), number=1000))
print(timeit("deq_appnd()", globals=globals(), number=1000))
print(timeit("pop_lst()", globals=globals(), number=1000))
print(timeit("pop_deq()", globals=globals(), number=1000))
print(timeit("lst_extend()", globals=globals(), number=1000))
print(timeit("deq_extend()", globals=globals(), number=1000))
"""
0.07474700012244284
0.0578724998049438
0.07589720003306866
0.05802160012535751
0.058881100034341216
0.03922059992328286
"""