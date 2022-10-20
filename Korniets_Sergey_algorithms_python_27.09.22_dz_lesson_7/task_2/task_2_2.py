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


def med(arr, m):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[m]
    less = []
    more = []
    pivots = []

    for x in arr:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            more.append(x)
        else:
            pivots.append(x)

    if len(less) > m:
        return med(less, m)
    elif len(less) + len(pivots) > m:
        return pivots[0]
    else:
        return med(more, m - len(less) - len(pivots))


# замеры 11
m = 5
array = [randint(-100, 100) for _ in range(2 * m + 1)]
print(array)
print(timeit("med(array[:], m)", globals=globals(), number=1000))    # 0.004230300008202903
print(f'Медиана {med(array[:], m)}')

# замеры 101
m = 50
array = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("med(array[:], m)", globals=globals(), number=1000))    # 0.04011069999251049
print(f'Медиана {med(array[:], m)}')

# замеры 1001
m = 500
array = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("med(array[:], m)", globals=globals(), number=1000))    # 0.19584840000607073
print(f'Медиана {med(array[:], m)}')
