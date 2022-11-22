from random import randint
from timeit import timeit


def sort(lst):
    res = lst[:]
    for i in range(len(lst) // 2):
        res.remove(min(res))
    return min(res)


m = int(input('Введите число: '))
ls = [randint(-100, 100) for _ in range(2 * m + 1)]
print(sort(ls[:]))
print(timeit("sort(ls[:])", globals=globals(), number=1000))

'''
10 элементов:   0.007395400000000052
100 элементов:  0.3244064999999998
1000 элементов: 29.4120623
'''

