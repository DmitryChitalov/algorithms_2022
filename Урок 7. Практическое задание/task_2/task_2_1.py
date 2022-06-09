"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randrange
from timeit import timeit


def gnome_sort_median(array):
    i, length = 1, len(array)
    while i < length:
        if array[i - 1] <= array[i]:
            i += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            if i > 1:
                i -= 1
    return array, f'Медиана - {array[m]}'


m = int(input('Введите m:'))

arr = [randrange(100) for x in range(2 * m + 1)]
print(arr)
print(*gnome_sort_median(arr))

print('10: ', timeit('gnome_sort_median([randrange(100) for x in range(10)])', globals=globals(), number=100))
print('100: ', timeit('gnome_sort_median([randrange(100) for x in range(100)])', globals=globals(), number=100))
print('1000: ', timeit('gnome_sort_median([randrange(100) for x in range(1000)])', globals=globals(), number=100))

"""
10:  0.0016391000244766474
100:  0.09056790010072291
1000:  9.537067199824378
"""