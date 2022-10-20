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

# Замеры 10
m = 5

random_list = [randint(-100, 100) for _ in range(2 * m + 1)]


def func_median(some_list):
    copy_some_list = some_list
    for _ in range(len(some_list) // 2):
        copy_some_list.remove(max(copy_some_list))
    return f"Медианой списка является число: {max(copy_some_list)}"


print(random_list)
print(func_median(random_list))

print(
    timeit(
        "func_median(random_list)",
        globals=globals(),
        number=1000))

# Замеры 100
m = 50

random_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(random_list)
print(func_median(random_list))

print(
    timeit(
        "func_median(random_list)",
        globals=globals(),
        number=1000))

# Замеры 1000
m = 500

random_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(random_list)
print(func_median(random_list))

print(
    timeit(
        "func_median(random_list)",
        globals=globals(),
        number=1000))

"""
Время выполнения:

Массив из 10 элементов - 0.0004962000530213118
Массив из 100 элементов - 0.0005220999009907246
Массив из 1000 элементов - 0.003393700113520026
"""
