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

"""
Без сортировки.

10 + 1 элемент: 0.0019228000000000023
100 + 1 элемент: 0.10521279999999997
1000 + 1 элемент: 9.5561949
"""

from random import randint
from timeit import timeit


def find_median(original_array, m):
    for i in range(m):
        original_array.remove(max(original_array))


if __name__ == '__main__':
    m = 5
    original_array = [randint(-100, 99) for i in range(2*m + 1)]
    print(timeit('find_median(array.copy(), m)', setup='array = original_array', number=1000, globals=globals()))

    m = 50
    original_array = [randint(-100, 99) for i in range(2*m + 1)]
    print(timeit('find_median(array.copy(), m)', setup='array = original_array', number=1000, globals=globals()))

    m = 500
    original_array = [randint(-100, 99) for i in range(2*m + 1)]
    print(timeit('find_median(array.copy(), m)', setup='array = original_array', number=1000, globals=globals()))