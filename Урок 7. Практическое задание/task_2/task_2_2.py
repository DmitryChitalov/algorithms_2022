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

m = 5
origin_list_11 = [randint(-100, 100) for _ in range(2*m + 1)]
print(origin_list_11)

m = 50
origin_list_101 = [randint(-100, 100) for _ in range(2*m + 1)]

m = 500
origin_list_1001 = [randint(-100, 100) for _ in range(2*m + 1)]


def mediana(lst_obj):
    for i in range(int(len(lst_obj) / 2)):
        lst_obj.remove(max(lst_obj))
    return max(lst_obj)


# замеры для 11
print(
    timeit(
        "mediana(origin_list_11[:])",
        globals=globals(),
        number=1000))

# замеры для 101
print(
    timeit(
        "mediana(origin_list_101[:])",
        globals=globals(),
        number=1000))

# замеры для 1001
print(
    timeit(
        "mediana(origin_list_1001[:])",
        globals=globals(),
        number=1000))

# 0.0011356660106685013
# 0.05656762499711476
# 4.102964791003615