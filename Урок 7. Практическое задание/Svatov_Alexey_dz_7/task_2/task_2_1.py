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


def array_gen(m):
    return [randint(-100, 100) for _ in range(2 * m + 1)]


def median_shell_sort(lst):
    last_index = len(lst) - 1
    step = len(lst) // 2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and lst[delta] > lst[j]:
                lst[delta], lst[j] = lst[j], lst[delta]
                j = delta
                delta = j - step
        step //= 2
    return f'Медиана списка = {lst[len(lst) // 2]}'


test_list_11 = array_gen(5)
test_list_101 = array_gen(50)
test_list_1001 = array_gen(500)

print(timeit("median_shell_sort(test_list_11[:])", globals=globals(), number=1000))
print(timeit("median_shell_sort(test_list_101[:])", globals=globals(), number=1000))
print(timeit("median_shell_sort(test_list_1001[:])", globals=globals(), number=1000))

"""
0.0038569370008190162
0.0729822579996835
1.2109952939990762
"""
