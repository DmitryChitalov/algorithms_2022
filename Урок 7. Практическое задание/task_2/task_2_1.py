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

def gnome(arr,i = 1):
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



arr_origin = [randint(-100, 100) for _ in range(11)]
print(arr_origin)
med = gnome(arr_origin[:])[(len(gnome(arr_origin[:])) - 1) // 2]  # Вычисление медианы массива.
print(gnome(arr_origin[:]))
print(med)

#замеры 11
print(
    timeit(
        "gnome(arr_origin[:])",
        globals=globals(),
        number=1000))


arr_origin = [randint(-100, 100) for _ in range(101)]

med = gnome(arr_origin[:])[(len(gnome(arr_origin[:])) - 1) // 2]  # Вычисление медианы массива.
print(gnome(arr_origin[:]))
print(med)

# замеры 101
print(
    timeit(
        "gnome(arr_origin[:])",
        globals=globals(),
        number=1000))


arr_origin = [randint(-100, 100) for _ in range(1001)]

med = gnome(arr_origin[:])[(len(gnome(arr_origin[:])) - 1) // 2]  # Вычисление медианы массива.
print(gnome(arr_origin[:]))
print(med)

# замеры 1001
print(
    timeit(
        "gnome(arr_origin[:])",
        globals=globals(),
        number=1000))


"""
Гномья сортировка довольно длительный процесс и она сравнима с пузырьковой при колличестве элементов до 100,
обеспечивает приемлемую скорость! При больших массивах время сортировки довольно большое!

0.016518699994776398 - 11 элементов
1.4911645000101998 - 101 элементов
145.27000439999392 - 1001 элементов
"""