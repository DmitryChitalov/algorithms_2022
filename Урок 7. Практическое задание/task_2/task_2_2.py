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


def find_median(m):
    lst = [randint(-100, 100) for i in range(2 * m + 1)]
    # print(f'Исходный список: {lst}')
    for i in range(m):
        lst.remove(max(lst))
    return max(lst)


# замер 11
print(timeit("find_median(5)", globals=globals(), number=1000))

# замер 101
print(timeit("find_median(50)", globals=globals(), number=1000))

# замер 1001
print(timeit("find_median(500)", globals=globals(), number=1000))

'''
0.008505499921739101
0.16149620013311505
6.507513299817219
'''
