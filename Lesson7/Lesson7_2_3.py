import statistics
from random import randint
from timeit import timeit
import numpy as np


def sort(lst):
    return statistics.median(lst)


m = int(input("Введите любое натуральное число: "))
len = 2 * m + 1
print(f'Нахождение медианы с помощью statistics.median')
lst = [randint(0, 10) for _ in range(len)]
print(timeit("sort(lst)", globals=globals(), number=1000))

lst1 = [randint(0, 100) for _ in range(len)]
print(timeit("sort(lst1)", globals=globals(), number=1000))

lst2 = [randint(0, 1000) for _ in range(len)]
print(timeit("sort(lst2)", globals=globals(), number=1000))


def sort1(lst):
    lst = np.array(lst)
    return np.median(lst)


print(f'Нахождение медианы с помощью numpy')
print(timeit("sort1(lst)", globals=globals(), number=1000))

print(timeit("sort1(lst1)", globals=globals(), number=1000))

print(timeit("sort1(lst2)", globals=globals(), number=1000))

# Анализ скорости выполнения алгоритмов по нахождению медианы показал, что самый быстрый способ это способ с
# помощью цикла (без сортировки). Самым медленным по скорости оказался способ c помощью Numpy
