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
def med_nosort(m):
    arr = gen_int(2 * m + 1)
    for el in arr:
        left = []
        right = []
        mid = []
        while len(left) <= m and len(right) <= m:
            for i in range (2*m+1):
                if el > arr[i]: left.append(arr[i])
                elif el < arr[i]: right.append(arr[i])
                else: mid.append(arr[i])
            if len(left) == len(right):
                return el


print("Поиск без сортировки")
print("Для m=10")
print(f"Получаем массив c медианой {med_nosort(10)}")
print("Для m=100")
print(f"Получаем массив c медианой {med_nosort(100)}")
print("Для m=1000")
print(f"Получаем массив c медианой {med_nosort(1000)}")
