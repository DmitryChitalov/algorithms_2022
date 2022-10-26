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
from random import randint
from timeit import timeit


# Через сортировку (Гномья)

def gnome(arr, i=1):
    while i < len(arr):
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
            else:
                i += 1
    return arr


m = 10

arr_origin = [randint(-100, 100) for _ in range(2 * m + 1)]
print(arr_origin)
print(gnome(arr_origin[:])[m])  # Вычисление медианы массива.
print(gnome(arr_origin[:]))

# замеры 21
print(
    timeit(
        "gnome(arr_origin[:])",
        globals=globals(),
        number=1000))

m = 100

arr_origin = [randint(-100, 100) for _ in range(2 * m + 1)]
print(arr_origin)
print(gnome(arr_origin[:])[m])  # Вычисление медианы массива.
print(gnome(arr_origin[:]))

# замеры 201
print(
    timeit(
        "gnome(arr_origin[:])",
        globals=globals(),
        number=1000))

m = 1000

arr_origin = [randint(-100, 100) for _ in range(2 * m + 1)]
print(arr_origin)
print(gnome(arr_origin[:])[m])  # Вычисление медианы массива.
print(gnome(arr_origin[:]))

# замеры 2001
print(
    timeit(
        "gnome(arr_origin[:])",
        globals=globals(),
        number=1000))

"""
Гномья сортировка довольно длительный процесс и она сравнима с пузырьковой при колличестве элементов до 100,
обеспечивает приемлемую скорость! При больших массивах время сортировки довольно большое!

0.10488439991604537 - 21 элементов
6.949105400010012 - 201 элементов
739.5181122999638 - 2001 элементов
"""
