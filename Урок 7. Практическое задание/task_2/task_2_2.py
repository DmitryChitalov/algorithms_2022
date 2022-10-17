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
import statistics


def fn_median(data):
    m = len(data) // 2

    for _ in range(m):
        mx = 0
        poz = 0
        for j in range(len(data)):
            if data[j] > mx:
                mx, poz = data[j], j
        data.pop(poz)

    return max(data)

def run_def(s):
    a, b = 0, 1000
    data = [randint(a, b) for _ in range(s)]
    median_my = fn_median(data[:])
    # print(f' median  {median_my}')
    # print(f' median  {statistics.median(data)}')

# run_def(11)
print(timeit('run_def(11)', globals=globals(), number= 100))
print(timeit('run_def(101)', globals=globals(), number= 100))
print(timeit('run_def(1001)', globals=globals(), number= 100))

# 0.001117900013923645
# 0.022476500016637146
# 1.547357200004626