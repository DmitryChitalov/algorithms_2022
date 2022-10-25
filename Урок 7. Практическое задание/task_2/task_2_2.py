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

# Попробуем вычислить медиану массива без сортировки.
def remove_max(lst_obj):
    """ Возвращает медиану путём удаления максимальных элементов."""

    temp_list = lst_obj

    for i in range(len(lst_obj) // 2):
        temp_list.remove(max(temp_list))

    return max(temp_list)


arr_origin = [randint(-100, 100) for _ in range(11)]
print(arr_origin)
print(sorted(arr_origin[:]))
med = remove_max(arr_origin[:])  # Вычисление медианы массива.
print(med)

#замеры 11
print(
    timeit(
        "remove_max(arr_origin[:])",
        globals=globals(),
        number=1000))


arr_origin = [randint(-100, 100) for _ in range(101)]

print(arr_origin)
print(sorted(arr_origin[:]))
med = remove_max(arr_origin[:])  # Вычисление медианы массива.
print(med)

# замеры 101
print(
    timeit(
        "remove_max(arr_origin[:])",
        globals=globals(),
        number=1000))


arr_origin = [randint(-100, 100) for _ in range(1001)]

print(arr_origin)
print(sorted(arr_origin[:]))
med = remove_max(arr_origin[:])  # Вычисление медианы массива.
print(med)

# замеры 1001
print(
    timeit(
        "remove_max(arr_origin[:])",
        globals=globals(),
        number=1000))

"""
Скорость вычисления медианы массива увеличилась примерно на порядок в сравнении с использованием Гномьей сортировки в 
предыдущем задании!

0.006736399955116212 - 11 элементов
0.15793180000036955 - 101 элементов
12.864605900016613 - 1001 элементов
"""
