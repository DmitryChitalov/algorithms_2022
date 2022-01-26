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


def shell(my_lst):
    inc = len(my_lst) // 2
    while inc:
        for i, el in enumerate(my_lst):
            while i >= inc and my_lst[i - inc] > el:
                my_lst[i] = my_lst[i - inc]
                i -= inc
            my_lst[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return my_lst


def get_mediane(my_lst):
    sorted_lst = shell(my_lst)
    return sorted_lst[int((len(sorted_lst) - 1) / 2)]


my_list = [randint(-100, 100) for x in range(11)]
print(my_list)
print(shell(my_list))
print(get_mediane(my_list))

s = """\
my_list = [randint(-100, 100) for x in range(11)]
get_mediane(my_list[:])
"""

print('11 elements ',
      timeit(s, globals=globals(), number=100), ' seconds ')

s = """\
my_list = [randint(-100, 100) for x in range(101)]
get_mediane(my_list[:])
"""

print('101 elements ',
      timeit(s, globals=globals(), number=100), ' seconds ')

s = """\
my_list = [randint(-100, 100) for x in range(1001)]
get_mediane(my_list[:])
"""

print('1001 elements ',
      timeit(s, globals=globals(), number=100), ' seconds ')

# C увелчением числа элементов увеличивается и время выполнения , что логично
# 11 elements  0.0027558059999999995  seconds
# 101 elements  0.032566748000000006  seconds
# 1001 elements  0.457357425  seconds
