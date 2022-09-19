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


def my_median(arr):
    arr = arr[:]
    for _ in range(len(arr) // 2):
        arr.remove(max(arr))
    return max(arr)


m = int(input('Введите m: '))
ARRAY = [randint(-m, m) for _ in range(2 * m + 1)]
print('Создан массив длинной 2m + 1:', ARRAY)
print()

print(f'поиск медианы массива длинной {len(ARRAY)}:', timeit('my_median(ARRAY)', globals=globals(), number=1000))
print('Медиана массива', my_median(ARRAY))
print()

ARRAY *= 9
print(f'поиск медианы массива длинной {len(ARRAY)}:', timeit('my_median(ARRAY)', globals=globals(), number=1000))
print('Медиана массива', my_median(ARRAY))
print()

ARRAY *= 11
print(f'поиск медианы массива длинной {len(ARRAY)}:', timeit('my_median(ARRAY)', globals=globals(), number=1000))
print('Медиана массива', my_median(ARRAY))

"""
Введите m: 5
Создан массив длинной 2m + 1: [-5, -4, 5, 2, 5, 3, -2, 5, 0, -1, -5]

поиск медианы массива длинной 11: 0.0028669260000242502
Медиана массива 0

поиск медианы массива длинной 99: 0.08225013300034334
Медиана массива 0

поиск медианы массива длинной 1089: 8.403464218999943
Медиана массива 0
"""