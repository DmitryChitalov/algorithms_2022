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


def median_without_sorting(num, m):
    lst = num[:]
    for el in range(m):
        lst.remove(max(lst))
    return max(lst)


print('----10----')
m = 10
lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(lst)
print(timeit("median_without_sorting(lst, m)", globals=globals(), number=1000))
print(median_without_sorting(lst, m))

print('----100----')
m = 100
lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(lst)
print(timeit("median_without_sorting(lst, m)", globals=globals(), number=1000))
print(median_without_sorting(lst, m))

print('----1000----')
m = 1000
lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(lst)
print(timeit("median_without_sorting(lst, m)", globals=globals(), number=1000))
print(median_without_sorting(lst, m))

"""
----10----
0.0271246

----100----
1.1952006

----1000----
110.7206092
"""