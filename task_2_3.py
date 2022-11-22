from random import randint
from timeit import timeit
from statistics import median

def sort(lst):
    return median(lst[:])


m = int(input('Введите число: '))
ls = [randint(-100, 100) for _ in range(2 * m + 1)]
print(sort(ls[:]))
print(timeit("sort(ls[:])", globals=globals(), number=1000))

'''
10 элементов:   0.0013278999999999375
100 элементов:  0.012989400000000373
1000 элементов: 0.19796350000000018
Вывод: Самый эффективный способ поиска медианы третий, с использованием
встроенной функцией!
'''

