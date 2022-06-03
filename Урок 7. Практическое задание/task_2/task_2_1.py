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

"""
Время выполнения:
При длине массива (2m + 1), где m = 5: 0.001645099837332964 сек.
При длине массива (2m + 1), где m = 50: 0.03460709983482957 сек.
При длине массива (2m + 1), где m = 500: 0.5130623001605272 сек.
"""

from timeit import timeit
from random import randint


def shellsort(a, m):
    def new_increment(a):
        i = int(len(a) / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(round(i / 2.2))
            yield i

    for increment in new_increment(a):
        for i in range(increment, len(a)):
            for j in range(i, increment - 1, -increment):
                if a[j - increment] < a[j]:
                    break
                a[j], a[j - increment] = a[j - increment], a[j]
    return f'медиана равна: {a[m]}'


m = 5
array_11 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(shellsort(array_11[:], m))
print(f"Время выполнения со списком из {2 * m + 1} 'элементов: "
      f"{timeit(f'shellsort(array_11[:], m)', globals=globals(), number=100)} сек.\n")

m = 50
array_101 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(shellsort(array_101[:], m))
print(f"Время выполнения со списком из {2 * m + 1} 'элементов: "
      f"{timeit(f'shellsort(array_101[:], m)', globals=globals(), number=100)} сек.\n")

m = 500
array_1001 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(shellsort(array_1001[:], m))
print(f"Время выполнения со списком из {2 * m + 1} 'элементов: "
      f"{timeit(f'shellsort(array_1001[:], m)', globals=globals(), number=100)} сек.")
