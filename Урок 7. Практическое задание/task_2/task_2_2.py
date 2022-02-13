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

from random import randint, choice
import timeit


def get_median_2(m):  # O(n)
    """
    Без сортировки.
    """
    n = [randint(-100, 100) for _ in range(2 * m + 1)]

    def select_nth(part, n):
        pivot = choice(n)

        lesser = [el for el in n if el < pivot]
        if len(lesser) > part:
            return select_nth(part, lesser)
        part -= len(lesser)

        numequal = n.count(pivot)
        if numequal > part:
            return pivot
        part -= numequal

        greater = [el for el in n if el > pivot]
        return select_nth(part, greater)

    return f'Медиана: {select_nth(len(n) // 2, n)}\n' \
           f'в массиве: {n}'


if __name__ == '__main__':
    print(get_median_2(5))
    print(timeit.timeit(stmt="get_median_2(5)", globals=globals(), number=1000))
    print(timeit.timeit(stmt="get_median_2(50)", globals=globals(), number=1000))
    print(timeit.timeit(stmt="get_median_2(500)", globals=globals(), number=1000))

# Медиана: -15
# 0.010852899999999999
# 0.0758405
# 0.6877006
