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


def test_list(m):
    return [randint(1, 10) for _ in range(2 * m + 1)]


def median_search(lst):
    return f'Медиана: {sorted(lst)[len(lst) // 2]}'


test_list_10 = test_list(5)
test_list_100 = test_list(50)
test_list_1000 = test_list(500)

print(timeit("median_search(test_list_10[:])", globals=globals(), number=10000))
print(timeit("median_search(test_list_100[:])", globals=globals(), number=10000))
print(timeit("median_search(test_list_1000[:])", globals=globals(), number=10000))

"""
Самым эффективным, как и ожидалось, оказался встроенный метод.
Вторым по времени исполнения был метод без сортировки(якобы) из задания 2_2
Самым медленным оказаля алгоритм гномьей сортировки.
"""
