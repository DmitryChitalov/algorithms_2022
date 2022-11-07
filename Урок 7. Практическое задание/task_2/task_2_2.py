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

"""
Результат:
[-70, -64, -97, 39, 8, -59, 27, -83, 3, 96, -42, -82, 35, 88, -18, -21, -22, 25, 16, -22, -94, 65, 42, 37, -43, -14, -29, 9, -67, 90, 72, -67, -29, 74, -21, -21, -97, -98, 67, -70, -52]
Медиана списка -21
0.0018230000000000052
0.0576604
5.5150752

"""

from random import randint
from timeit import timeit

def my_median(lst):
    a = len(lst) // 2
    while len(lst) > a:
        lst.remove(max(lst))
    return f"Медиана списка {max(lst)}"

m = randint(3, 100)
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(orig_list)
print(my_median(orig_list[:]))

# замеры 10
orig_list = [randint(-100, 100) for _ in range(10)]

print(
    timeit(
        "my_median(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "my_median(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "my_median(orig_list[:])",
        globals=globals(),
        number=1000))
