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


# Сортировка Шелла
def shell_sort(array):
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2
    return array


# -----------------------------------------------------------------------------
m = 10
origin_list = [randint(-100, 100) for _ in range(2 * m + 1)]
# print(origin_list)
sorted_list = shell_sort(origin_list[:])
# print(sorted_list)
print(f"Медиана списка из 11 элементов: {sorted_list[m]}")
# Измерение среднего время выполнения куска кода.
time_shell = timeit(stmt="shell_sort(origin_list[:])",
                    number=100,
                    globals=globals())
print(f"{'%.8f' % time_shell} seconds")
del origin_list

# -----------------------------------------------------------------------------
m = 100
origin_list = [randint(-100, 100) for _ in range(2 * m + 1)]
# Измерение среднего время выполнения куска кода.
time_shell = timeit(stmt="shell_sort(origin_list[:])",
                    number=100,
                    globals=globals())
print(f"{'%.8f' % time_shell} seconds")
del origin_list

# -----------------------------------------------------------------------------
m = 1000
origin_list = [randint(-100, 100) for _ in range(2 * m + 1)]
# Измерение среднего время выполнения куска кода.
time_shell = timeit(stmt="shell_sort(origin_list[:])",
                    number=100,
                    globals=globals())
print(f"{'%.8f' % time_shell} seconds")
del origin_list

"""
Медиана списка из 11 элементов: -17
0.00166200 seconds
0.03482970 seconds
0.59892590 seconds
"""
