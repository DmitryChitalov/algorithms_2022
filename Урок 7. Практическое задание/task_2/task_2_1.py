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
from timeit import timeit


def median_search(value: list) -> int:
    i = 0
    index = 1
    while i < len(value) - 1:
        if value[i] <= value[i + 1]:
            i, index = index, index + 1
        else:
            value[i], value[i + 1] = value[i + 1], value[i]
            i = i - 1
            if i < 0:
                i, index = index, index + 1
    return value[len(value) // 2]


if __name__ == '__main__':
    m = int(input('Введите число: '))
    my_list = [randint(-100, 100) for _ in range(2 * m + 1)]
    print(f'Неотсортированный список {my_list}')
    print(f'Медиана: {median_search(my_list)}')
    print(f'Отсортированный список: {my_list}')

    print('Замер на массив 10 эл.', timeit('median_search([randint(-100, 100) for _ in range(11)])',
                                           globals=globals(), number=1000))

    print('Замер на массив 100 эл.', timeit('median_search([randint(-100, 100) for _ in range(101)])',
                                            globals=globals(), number=1000))

    print('Замер на массив 1000 эл.', timeit('median_search([randint(-100, 100) for _ in range(1001)])',
                                             globals=globals(), number=1000))

"""
Замер на массив 10 эл. 0.014164400025038049
Замер на массив 100 эл. 0.5979630000074394
Замер на массив 1000 эл. 72.20550969999749
"""