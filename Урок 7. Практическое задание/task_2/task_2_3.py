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

from statistics import median
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
def med_iner(m):
    a = median(gen_int(m*2+1))
    return a

print('Встоенная функция median')
print("Для m=10")
print(f"Получаем массив c медианой {med_iner(10)}")
print("Для m=100")
print(f"Получаем массив c медианой {med_iner(100)}")
print("Для m=1000")
print(f"Получаем массив c медианой {med_iner(1000)}")
"""Встроенная функция оказалась самой быстрой, затем идет функция без сортировки массива (т.к. требует меньшего
 числа проходов) и самая медленная с предварительной сортировкой по "гномьему" алгоритму"""
