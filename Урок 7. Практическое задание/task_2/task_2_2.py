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

m = 10

arr_origin = [randint(-100, 100) for _ in range(2*m + 1)]
print(arr_origin)
print(sorted(arr_origin[:]))
med = remove_max(arr_origin[:])  # Вычисление медианы массива.
print(med)

#замеры 21
print(
    timeit(
        "remove_max(arr_origin[:])",
        globals=globals(),
        number=1000))

m = 100

arr_origin = [randint(-100, 100) for _ in range(2*m + 1)]
print(arr_origin)
print(sorted(arr_origin[:]))
med = remove_max(arr_origin[:])  # Вычисление медианы массива.
print(med)

# замеры 201
print(
    timeit(
        "remove_max(arr_origin[:])",
        globals=globals(),
        number=1000))

m = 1000

arr_origin = [randint(-100, 100) for _ in range(2*m + 1)]
print(arr_origin)
print(sorted(arr_origin[:]))
med = remove_max(arr_origin[:])  # Вычисление медианы массива.
print(med)

# замеры 2001
print(
    timeit(
        "remove_max(arr_origin[:])",
        globals=globals(),
        number=1000))

"""
Скорость вычисления медианы массива увеличилась примерно на порядок в сравнении с использованием Гномьей сортировки в 
предыдущем задании!

0.009377799928188324 - 21 элементов
0.43131569994147867 - 201 элементов
47.21707590005826 - 2001 элементов
"""
