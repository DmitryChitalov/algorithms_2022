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
import math
import timeit


def get_median_1(m):  # O(n**2)
    """
    С сортировкой Шелла.
    """
    n = [randint(-100, 100) for _ in range(2 * m + 1)]
    n_cp = n.copy()
    length = len(n_cp)
    k = int(math.log2(length))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, length):
            temp = n_cp[i]
            j = i
            while j >= interval and n_cp[j - interval] > temp:
                n_cp[j] = n_cp[j - interval]
                j -= interval
            n_cp[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return f'Медиана: {n_cp[m]}\n' \
           f'в массиве: {n}'


if __name__ == '__main__':
    print(get_median_1(5))
    print(timeit.timeit(stmt="get_median_1(5)", globals=globals(), number=1000))
    print(timeit.timeit(stmt="get_median_1(50)", globals=globals(), number=1000))
    print(timeit.timeit(stmt="get_median_1(500)", globals=globals(), number=1000))


# Медиана: -19
# в массиве: [94, 1, -82, 88, -28, -39, 12, -79, 94, -90, -19]
# отсортированный список: [-90, -82, -79, -39, -28, -19, 1, 12, 88, 94, 94]
# 0.0128881
# 0.1448699
# 2.2143148
