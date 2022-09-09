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
from memory_profiler import profile
from time import time


def timer1(func):
    def time_mes(*args, **kwargs):
        start = time()
        act = func(*args, **kwargs)
        stop = time()
        res = stop - start
        print(f'Функция выполняется за {res} c')
        return act
    return time_mes


def gen_int(n):
    a = [randint(0, 10000) for _ in range(n)]
    return a


# @profile
@timer1
def gnom(m):
    arr = gen_int(2 * m + 1)
    fl = False
    i = 1
    while i < len(arr):
        for j in range(len(arr) - i):
            while arr[j] > arr[j + 1] and j >= 0:
                fl = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j -= 1
        if fl is False:
            break
        i += 1
    return arr[len(arr) // 2]

print('Гномья сортировка')
print('базовое число 10')
print(f"Получаем массив c медианой {gnom(10)}")# print('базовое число 100')
print('базовое число 100')
print(f"Получаем массив c медианой {gnom(100)}")# print('базовое число 100')
print('базовое число 1000')
print(f"Получаем массив c медианой {gnom(1000)}")# print('базовое число 100')
