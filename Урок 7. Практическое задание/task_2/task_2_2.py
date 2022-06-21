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


def middle_elem(lst_obj):
    copy_lst = lst_obj
    for i in range(len(lst_obj) // 2):
        copy_lst.remove(min(copy_lst))
    return min(copy_lst)


m = 10
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Медиана для массива из 10 элементов: {middle_elem(orig_list)}')
print(timeit("middle_elem(orig_list[:])", globals=globals(), number=1000))
print('-' * 50)
m = 100
orig_list_1 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Медиана для массива из 100 элементов: {middle_elem(orig_list_1)}')
print(timeit("middle_elem(orig_list_1[:])", globals=globals(), number=1000))
print('-' * 50)
m = 1000
orig_list_2 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Медиана для массива из 1000 элементов: {middle_elem(orig_list_2)}')
print(timeit("middle_elem(orig_list_2[:])", globals=globals(), number=1000))
