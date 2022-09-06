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

'''
Результаты замеров:
0.00185960007365793 => 11
0.046954400022514164 => 101
4.370190999936312 => 1001
'''

arr = [3, 1, 5, 4, 2, 6, 7]  # список для проверки


def med_no_sort(some_list):
    n = 0
    while n <= len(some_list) / 2:
        some_list.remove(max(some_list))
        n += 1
    return max(some_list)


print(med_no_sort(arr[:]))  # => 4

orig_list = [randint(-100, 100) for _ in range(11)]
print(
    timeit(
        "med_no_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(101)]

print(
    timeit(
        "med_no_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1001)]
print(
    timeit(
        "med_no_sort(orig_list[:])",
        globals=globals(),
        number=1000))
