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

'''
Результаты замеров:
0.0014348000986501575 => 11
0.7920447000069544 => 101
83.07762359990738 => 1001
'''

arr = [1, 3, 2, 4, 7, 6, 5]  # список для проверки


def gnome_sort(list_to_sort):
    n = 1
    while n < len(list_to_sort):
        if list_to_sort[n - 1] <= list_to_sort[n]:
            n += 1
        else:
            list_to_sort[n - 1], list_to_sort[n] = list_to_sort[n], list_to_sort[n - 1]
            if n > 1:
                n -= 1  # идея гномьей сортировки, что мы будем двигаться на 1 шаг назад, если есть обмен позиций
    return list_to_sort[len(list_to_sort) // 2]


print(gnome_sort(arr))  # => 4

orig_list = [randint(-100, 100) for _ in range(11)]

print(
    timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(101)]

print(
    timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1001)]

print(
    timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=1000))
