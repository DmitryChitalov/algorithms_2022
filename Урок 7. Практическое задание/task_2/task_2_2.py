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


def get_med(my_lst):
    med_idx = int((len(my_lst) - 1) / 2)
    for i in range(med_idx):
        my_lst.remove(min(my_lst))
    return min(my_lst)


s = """\
my_list = [randint(-100, 100) for x in range(11)]
get_med(my_list[:])
"""

print('11 elements ',
      timeit(s, globals=globals(), number=100), ' seconds ')

s = """\
my_list = [randint(-100, 100) for x in range(101)]
get_med(my_list[:])
"""

print('101 elements ',
      timeit(s, globals=globals(), number=100), ' seconds ')

s = """\
my_list = [randint(-100, 100) for x in range(1001)]
get_med(my_list[:])
"""

print('1001 elements ',
      timeit(s, globals=globals(), number=100), ' seconds ')

# C увеличением числа элементов увеличивается и время выполнения , что логично
# 1001 элемент уже существенно медленнее варианта с сортировкой ( в задании 2_1 )
# 11 elements  0.0028230900000000003  seconds
# 101 elements  0.028974165000000003  seconds
# 1001 elements  1.449167556  seconds
