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

import random
from timeit import timeit


def min_method(lst: list):
    temp_list = lst[:]
    return [temp_list.pop(temp_list.index(min(temp_list))) for _ in range(len(lst) // 2 + 1)][-1]


m = 5
test_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(test_list)
print(f'Медиана: {min_method(test_list[:])}')

# Замеры
for m in [10, 100, 1000]:
    test_list = [random.randint(-100, 100) for _ in range(m)]
    print(f'Поиск медианы в списке из {m} элементов: ', end=' ')
    print(timeit('min_method(test_list[:])', globals=globals(), number=1000))
