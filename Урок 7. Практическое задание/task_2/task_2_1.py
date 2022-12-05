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
import math


def shell_sort(lst):
    n = len(lst)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = lst[i]
            j = i
            while j >= interval and lst[j - interval] > temp:
                lst[j] = lst[j - interval]
                j -= interval
            lst[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return lst


def get_lst(m):
    return [randint(-100, 100) for i in range(2 * m + 1)]


my_m = 50
my_lst = get_lst(my_m)
print(f'Исходный массив: {my_lst}')

print(f'Отсортированный массив: {shell_sort(my_lst[:])}')
print('медиана: ', shell_sort(my_lst[:])[my_m])

# замер 11
print(timeit("shell_sort(get_lst(5))", globals=globals(), number=1000))

# замер 101
print(timeit("shell_sort(get_lst(50))", globals=globals(), number=1000))

# замер 1001
print(timeit("shell_sort(get_lst(500))", globals=globals(), number=1000))

'''
0.014538699993863702
0.17460980010218918
2.703181599965319
'''
