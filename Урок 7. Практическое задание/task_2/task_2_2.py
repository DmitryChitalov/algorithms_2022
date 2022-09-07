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

orig_list = [92, 89, 83, -49, -50, -100, 96]

def without_sort(orig_list):
    for i in orig_list:
        item = i
        n = 0
        for j in orig_list:
            if i < j:
                n += 1
        if len(orig_list) == 2 * n + 1:
            return item

print(without_sort(orig_list))
# замеры 10
orig_list = [randint(-100, 100) for _ in range(10)]
print(
    timeit(
        "without_sort(orig_list[:])",
        globals=globals(),
        number=1000))
# замеры 100
orig_list = [randint(-100, 100) for _ in range(100)]
print(
    timeit(
        "without_sort(orig_list[:])",
        globals=globals(),
        number=1000))
# замеры 1000
orig_list = [randint(-100, 100) for _ in range(1000)]
print(
    timeit(
        "without_sort(orig_list[:])",
        globals=globals(),
        number=1000))


"""
0.014296799898147583
0.8178206998854876
74.8700594000984
"""
