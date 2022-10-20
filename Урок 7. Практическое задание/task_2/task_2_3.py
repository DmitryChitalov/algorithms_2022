"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randint
from timeit import timeit
from statistics import median

# Замеры 10
m = 5

random_list = [randint(-100, 100) for _ in range(2 * m + 1)]


def func_median(some_list):
    return f"Медианой списка {some_list} является число: {median(some_list)}"


print(func_median(random_list))

print(
    timeit(
        "func_median(random_list)",
        globals=globals(),
        number=1000))

# Замеры 100
m = 50
random_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(func_median(random_list))
print(
    timeit(
        "func_median(random_list)",
        globals=globals(),
        number=1000))

# Замеры 1000
m = 500
random_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(func_median(random_list))
print(
    timeit(
        "func_median(random_list)",
        globals=globals(),
        number=1000))

"""
Время выполнения:

Массив из 10 элементов - 0.001744000008329749
Массив из 100 элементов - 0.010640599997714162
Массив из 1000 элементов - 0.12514459993690252

Второй вариант поиска медианы (без сортировки) отрабатывает быстрее всего, т.к. не приходится сортировать массив.
"""
