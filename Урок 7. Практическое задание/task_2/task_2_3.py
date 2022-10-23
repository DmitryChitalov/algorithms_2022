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

def median(obj):
    n = len(obj)
    index = n // 2
    if n % 2:
        return sorted(obj)[index]

    return sum(sorted(obj)[index - 1:index + 1]) / 2


object = [2, 8, 5, 1, 4, 10, 0]
print('Медиана:', median(object[:]))

object = [randint(-100, 100) for _ in range(10)]
print(timeit('median(object[:])', globals=globals(), number=1000))

object = [randint(-100, 100) for _ in range(100)]
print(timeit('median(object[:])', globals=globals(), number=1000))

object = [randint(-100, 100) for _ in range(1000)]
print(timeit('median(object[:])', globals=globals(), number=1000))

"""
Медиана: 4
0.0006145000000000005
0.0032323000000000005
0.0699606

не смогла на второе упражнение составить время, но из первого и третьего
по времени лучшим оказалось третье - встроенная функция.
"""
