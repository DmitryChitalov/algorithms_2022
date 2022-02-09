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


def shell_sort(data):
    last_index = len(data) - 1
    step = len(data)//2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data


m = 26
my_array = [randint(-100, 100) for _ in range(2 * m + 1)]
print(my_array)
print(f'Медиана ряда: {shell_sort(my_array[:])[m]}')


# # замеры 10
print(
    timeit(
        "shell_sort(my_array[:])[m]",
        globals=globals(),
        number=1000))

my_array = [randint(-100, 100) for _ in range(100 * 2 + 1)]

# замеры 100
print(
    timeit(
        "shell_sort(my_array[:])[m]",
        globals=globals(),
        number=1000))

my_array = [randint(-100, 100) for _ in range(1000 * 2 + 1)]

# замеры 1000
print(
    timeit(
        "shell_sort(my_array[:])[m]",
        globals=globals(),
        number=1000))


"""
0.0451825
0.2540887
3.7879927
"""
