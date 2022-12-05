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

def get_median(item: int) -> int:
    # Вернуть медианное значение списка.
    array: list = sorted_Shell([randint(-100, 100) for _ in range(2*item+1)])
    return array[item]

def sorted_Shell(array: list[int]) -> list[int]:
    # Отсортировать список методом Шелла.
    last_index: int = len(array)
    step: int = len(array)//2
    while step > 0:
        for i in range(step, last_index, 1):
            j: int = i
            delta: int = j - step
            while delta >= 0 and array[delta] > array[j]:
                array[delta], array[j] = array[j], array[delta]
                j = delta
                delta = j - step
        step //= 2
    return array

if __name__ == "__main__":
    m: int = 5
    print(f"Время нахождения медианы списка из 11 элементов с сортировкой Шелла: {timeit('get_median(m)', globals=globals(), number=1000)} секунды.")
    m: int = 50
    print(f"Время нахождения медианы списка из 101 элементов с сортировкой Шелла: {timeit('get_median(m)', globals=globals(), number=1000)} секунды.")
    m: int = 500
    print(f"Время нахождения медианы списка из 1001 элементов с сортировкой Шелла: {timeit('get_median(500)', globals=globals(), number=1000)} секунды.")

    """"
        Время нахождения медианы списка из 11 элементов с сортировкой Шелла: 0.009192555909976363 секунды.
        Время нахождения медианы списка из 101 элементов с сортировкой Шелла: 0.12052624498028308 секунды.
        Время нахождения медианы списка из 1001 элементов с сортировкой Шелла: 1.570420908043161 секунды.
    """