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


def lst_median(lst):
    temp_lst = lst
    for i in range(len(lst) // 2):
        temp_lst.remove(min(temp_lst))
    return min(temp_lst)


m = 10
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]

print(lst_median(orig_list))
print(timeit('lst_median(orig_list[:])', globals=globals(), number=1000))
# a = sorted(orig_list)
# print(a)
m = 100
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(lst_median(orig_list))
print(timeit('lst_median(orig_list[:])', globals=globals(), number=1000))
m = 1000
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(lst_median(orig_list))
print(timeit('lst_median(orig_list[:])', globals=globals(), number=1000))
