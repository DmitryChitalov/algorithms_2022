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

object = [2, 8, 5, 1, 4, 10, 0]


def median(obj):
    half = len(obj) // 2
    obj.sort()
    if not len(obj) % 2:
        return (obj[half - 1] + obj[half]) / 2
    return obj[half]

print('Исходный массив:', object)
print('Медиана:', median(object[:]))

def shell(obj):
    inc = len(obj) // 2
    while inc:
        for i, el in enumerate(obj):
            while i >= inc and obj[i - inc] > el:
                obj[i] = obj[i - inc]
                i -= inc
            obj[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
        
shell(object)
print(object) 

object = [randint(-100, 100) for _ in range(10)]
print(timeit('shell(object[:])', globals=globals, number=1000))

object = [randint(-100, 100) for _ in range(100)]
print(timeit('shell(object[:])', globals=globals, number=1000))

object = [randint(-100, 100) for _ in range(1000)]
print(timeit('shell(object[:])', globals=globals, number=1000))
