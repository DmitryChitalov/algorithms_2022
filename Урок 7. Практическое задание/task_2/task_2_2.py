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

def median(l, half):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]

    pivot = l[0]

    less = []
    more = []
    pivots = []
    for item in l:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            more.append(item)
        else:
            pivots.append(item)

    if len(less) > half:
        return median(less, half)
    elif len(less) + len(pivots) > half:
        return pivots[0]
    else:
        return median(more, half - len(more) - len(pivots))


n = 6
object = [randint(-100, 100) for _ in range(2 * n + 1)]
print(f'Исходный массив {object}')
print(f'Медиана {median(object, n)}')
