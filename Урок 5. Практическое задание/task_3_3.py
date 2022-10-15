"""3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее"""

from collections import deque
from timeit import timeit

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