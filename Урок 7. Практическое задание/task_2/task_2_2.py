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


def search_median(value: list) -> int:
    middle_list = len(value) // 2
    for _ in range(middle_list):
        value.remove(max(value))
    return max(value)


if __name__ == '__main__':
    m = int(input('Введите число: '))
    my_list = [randint(-100, 100) for _ in range(2 * m + 1)]
    print(search_median(my_list))

print('Замер на массив 10 эл.', timeit('search_median([randint(-100, 100) for _ in range(11)])',
                                       globals=globals(), number=1000))

print('Замер на массив 100 эл.', timeit('search_median([randint(-100, 100) for _ in range(101)])',
                                        globals=globals(), number=1000))

print('Замер на массив 1000 эл.', timeit('search_median([randint(-100, 100) for _ in range(1001)])',
                                         globals=globals(), number=1000))

"""
Замер на массив 10 эл. 0.020952499995473772
Замер на массив 100 эл. 0.1697553000121843
Замер на массив 1000 эл. 8.453153000009479
"""