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


def get_median(list_):
    if len(list_) % 2 == 0:
        raise ValueError('Need list with odd number of elements')
    dict_ = {}
    for i, element in enumerate(list_):
        dict_[i] = element
    m = int((len(list_)-1)/2)
    min_el_ = min(list_)
    for _ in range(m+1):
        max_el = min_el_
        for current_index, element in dict_.items():
            if element > max_el:
                index_max_element = current_index
                max_el = element
        median = dict_.pop(index_max_element)
    return median


m=10
list_1 = [i for i in random.choices(range(-100, 100), k=2*m + 1)]
m=100
list_2 = [i for i in random.choices(range(-100, 100), k=2*m + 1)]
m=1000
list_3 = [i for i in random.choices(range(-100, 100), k=2*m + 1)]

for list_, m in [('list_1', 10), ('list_2', 100), ('list_3', 1000)]:
    time_ = timeit(stmt=f'get_median({list_})', globals=globals(), number=1)
    print(f'For {m = } execution time = {time_}')
