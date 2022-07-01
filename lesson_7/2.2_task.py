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


def src_median(lst, m):
    my_list = lst[:]
    while m > 0:
        my_list.pop(my_list.index(max(my_list)))
        m -= 1
    return my_list.pop(my_list.index(max(my_list)))


m = 10
fst_lst = [randint(-1000, 1000) for _ in range(2 * m + 1)]
print(timeit('src_median(fst_lst, m)', globals=globals(), number=1000)) # 0.006

m = 100
sec_lst = [randint(-1000, 1000) for _ in range(2 * m + 1)]
print(timeit('src_median(sec_lst, m)', globals=globals(), number=1000)) # 0.354

m = 1000
thrd_lst = [randint(-1000, 1000) for _ in range(2 * m + 1)]
print(timeit('src_median(thrd_lst, m)', globals=globals(), number=1000)) # 34.386
