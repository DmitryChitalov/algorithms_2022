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
import statistics


def gnome_sort(data):
    i = 1
    ln = len(data)
    while i < ln:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


def run_def(m):
    a, b = 0, 1000
    s = m * 2 + 1
    data = [randint(a, b) for _ in range(s)]
    data = gnome_sort(data)

    median_my = data[m]
    # print(f' median  {median_my}')
    # print(f' median  {statistics.median(data)}')


# run_def(11)
m = 5
print(timeit('run_def(m)', globals=globals(), number=100))
m = 50
print(timeit('run_def(m)', globals=globals(), number=100))
m = 500
print(timeit('run_def(m)', globals=globals(), number=100))

# 0.002634700038470328
# 0.07996830000774935
# 7.083652600005735
