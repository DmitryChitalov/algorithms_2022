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


def median_not_sort(lst, m):
    while m > 0:
        lst.pop(lst.index(max(lst)))
        m -= 1
    return lst.pop(lst.index(max(lst)))


mes = int(input('Введите число: '))
N = 2*mes + 1
orig_list = [randint(-100, 100) for _ in range(N)]

print(median_not_sort(orig_list[:], mes))
print(timeit("median_not_sort(orig_list[:], mes)", globals=globals(), number=100))

"""
10:
0.000519299996085465
100:
0.032702700002118945
1000:
3.021266099996865
"""