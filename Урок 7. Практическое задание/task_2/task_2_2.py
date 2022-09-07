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


def unsorted_mediana(list_m: list, middle: int):
    """Функция """
    while len(list_m) > middle+1:
        list_m.remove(max(list_m))
    return max(list_m)


m = 10
orig_list = [randint(-100, 100) for _ in range(2*m+1)]
print(f'Исходный список: {orig_list}')
print(f'Отсортированная копия для проверки: {sorted(orig_list[:])}')
print(f'Медиана = {unsorted_mediana(orig_list[:], m)}')


# замеры 10
print(
    timeit(
        "unsorted_mediana(orig_list[:], m)",
        globals=globals(),
        number=1000))

m = 100
orig_list = [randint(-100, 100) for _ in range(2*m+1)]


# замеры 100
print(
    timeit(
        "unsorted_mediana(orig_list[:], m)",
        globals=globals(),
        number=1000))

m = 1000
orig_list = [randint(-100, 100) for _ in range(2*m+1)]


# замеры 1000
print(
    timeit(
        "unsorted_mediana(orig_list[:], m)",
        globals=globals(),
        number=1000))
