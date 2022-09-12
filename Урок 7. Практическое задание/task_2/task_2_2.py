"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit


def median_wo_sort(lst, m):
    while m > 0:
        lst.pop(lst.index(max(lst)))
        m -= 1
    return lst.pop(lst.index(max(lst)))


m = 10
list1 = [randint(-100, 100) for _ in range(2*m + 1)]
print(timeit("median_wo_sort(list1[:], m)", globals=globals(), number=1000))
print(list1[m])

m = 100
list2 = [randint(-100, 100) for _ in range(2*m + 1)]
print(timeit("median_wo_sort(list2[:], m)", globals=globals(), number=1000))
print(list2[m])

m = 1000
list3 = [randint(-100, 100) for _ in range(2*m + 1)]
print(timeit("median_wo_sort(list3[:], m)", globals=globals(), number=1000))
print(list3[m])

"""
10 элементов:
0.0162152
-84
100 элементов:
0.5677012
-12
1000 элементов:
60.507899
-26
"""
