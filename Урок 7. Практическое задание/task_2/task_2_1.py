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

import random
from timeit import timeit


def heap_sort(lst):
    """Сортировка кучей"""
    for start in range(int((len(lst) - 2) / 2), -1, -1):
        heap_sift(lst, start, len(lst) - 1)

    for end in range(len(lst) - 1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        heap_sift(lst, 0, end - 1)
    return lst


def heap_sift(lst, start, end):
    root = start

    while True:
        child = root * 2 + 1
        if child > end:
            break

        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1

        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break


m = 5
test_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(test_list)
print(f'Медиана: {heap_sort(test_list[:])[m]}')

# Замеры
for m in [10, 100, 1000]:
    test_list = [random.randint(-100, 100) for _ in range(m)]
    print(f'Сортировка списка из {m} элементов: ', end=' ')
    print(timeit('heap_sort(test_list[:])', globals=globals(), number=1000))
