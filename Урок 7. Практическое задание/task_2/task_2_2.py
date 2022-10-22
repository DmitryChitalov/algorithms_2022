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
from random import choice
from timeit import timeit
"""
сделайте замеры на массивах длиной 10, 100, 1000 элементов <- ТАК НЕ ПОЛУЧИТСЯ!!!
Так как длина массива 2m + 1, т.е. будет нечетное число.
Сделаем замеры на массивах длиной 11, 101, 1001 элементов
"""

numbers11 = [randint(-100, 100) for _ in range(11)]
numbers101 = [randint(-100, 100) for _ in range(101)]
numbers1001 = [randint(-100, 100) for _ in range(1001)]

"""
--- БЕЗ СОРТИРОВКИ ---
https://habr.com/ru/post/346930/?ysclid=l9jkw5tzka892779383
"""

def quickselect_median(array, pivot_fn=choice):
    if len(array) % 2 == 1:
        return quickselect(array, len(array) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(array, len(array) / 2 - 1, pivot_fn) +
                      quickselect(array, len(array) / 2, pivot_fn))

def quickselect(array, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке array (с нулевой базой)
    :param array: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент array
    """
    if len(array) == 1:
        assert k == 0
        return array[0]

    pivot = pivot_fn(array)

    lows = [el for el in array if el < pivot]
    highs = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


print(f'Исходный массив:\n{numbers11}')
print(f'Медиана: {quickselect_median(numbers11[:])}')

time1 = timeit(f'quickselect_median({numbers11[:]})',
              setup='from __main__ import quickselect_median, quickselect',
              number=1000)
print(f'Время: {time1} сек., Медиана: {quickselect_median(numbers11[:])}')