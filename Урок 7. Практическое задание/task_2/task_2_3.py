from numpy import median
from random import randint
from timeit import timeit
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


def numpy_median(lst_obj):
    return median(lst_obj[:])


m = 10
orig_list_10 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'При m = {m}: '
      f'{timeit("numpy_median(orig_list_10[:])", globals=globals(), number=1000)}')

m = 100
orig_list_100 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'При m = {m}: '
      f'{timeit("numpy_median(orig_list_100[:])", globals=globals(), number=1000)}')

m = 1000
orig_list_1000 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'При m = {m}: '
      f'{timeit("numpy_median(orig_list_1000[:])", globals=globals(), number=1000)}')


"""
При m = 10: 0.0354651000816375
При m = 100: 0.05158049985766411
При m = 1000: 0.244003799976781

Вывод:
Всироенная функция самая еффективная
"""