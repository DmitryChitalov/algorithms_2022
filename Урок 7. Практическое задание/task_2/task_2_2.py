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

mass_10 = [randint(1, 100) for i in range(2 * 5 + 1)]
mass_100 = [randint(1, 100) for j in range(2 * 50 + 1)]
mass_1000 = [randint(1, 100) for k in range(2 * 500 + 1)]


def median(data):
    numbers = data
    for i in numbers:
        if i == 2:
            numbers.remove(i)
        return i


print(timeit('median(mass_10[:])', globals=globals(), number=1000))
print()
print(timeit('median(mass_100[:])', globals=globals(), number=1000))
print()
print(timeit('median(mass_1000[:])', globals=globals(), number=1000))


