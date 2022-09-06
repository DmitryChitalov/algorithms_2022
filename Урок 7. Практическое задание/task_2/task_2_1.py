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


def shell_sort(lst):
    """
    Сортировка Шелла
    """
    step = len(lst) // 2
    while step > 0:
        for i in range(step, len(lst)):
            j = i
            pos = j - step
            while pos >= 0 and lst[pos] > lst[j]:
                lst[pos], lst[j] = lst[j], lst[pos]
                j = pos
                pos = j - step
        step //= 2
    return lst


m = 5
list_in = [randint(-100, 100) for _ in range(2 * m + 1)]
# замеры 10
print(f'10 элементов - {timeit("shell_sort(list_in[:])", globals=globals(), number=1000)}')
print(f'медиана = {shell_sort(list_in[:])[m]}')

m = 50
list_in = [randint(-100, 100) for _ in range(2 * m + 1)]
# замеры 100
print(f'100 элементов - {timeit("shell_sort(list_in[:])", globals=globals(), number=1000)}')
print(f'медиана = {shell_sort(list_in[:])[m]}')

m = 500
list_in = [randint(-100, 100) for _ in range(2 * m + 1)]
# замеры 1000
print(f'1000 элементов - {timeit("shell_sort(list_in[:])", globals=globals(), number=1000)}')
print(f'медиана = {shell_sort(list_in[:])[m]}')


"""
Результаты замеров

10 элементов - 0.02456039999378845
медиана = 23
100 элементов - 0.4309606999740936
медиана = -19
1000 элементов - 6.518632100021932
медиана = -1

"""