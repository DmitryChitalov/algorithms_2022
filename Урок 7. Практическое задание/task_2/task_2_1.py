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


# Гномья сортировка
def gnome_sort(arr):
    i = 1
    while i < len(arr):
        if not i or arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr


def get_arr(num):
    return [randint(1, 1000) for x in range(2 * num + 1)], num


arr_10 = get_arr(5)
arr_100 = get_arr(50)
arr_1000 = get_arr(500)

print(gnome_sort(arr_10[0]))
print(gnome_sort(arr_10[0])[arr_10[1]])
print(gnome_sort(arr_100[0]))
print(gnome_sort(arr_100[0])[arr_100[1]])
print(gnome_sort(arr_1000[0]))
print(gnome_sort(arr_1000[0])[arr_1000[1]])
print(timeit('gnome_sort(arr_10[0])', globals=globals(), number=1000))
print(timeit('gnome_sort(arr_100[0])', globals=globals(), number=1000))
print(timeit('gnome_sort(arr_1000[0])', globals=globals(), number=1000))

"""
Результат:
0.00192760000936687
0.01756180007942021
0.26707629999145865

Медианы:
429
441
497
"""
