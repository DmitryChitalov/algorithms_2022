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
from timeit import timeit
from random import randrange


def create_lst(m):
    lst = [randrange(-100, 100) for _ in range(2 * m + 1)]
    return lst


def find_median_cycle(lst, m):
    for _ in range(m):
        lst.remove(max(lst))
    return max(lst)


m1 = 10
lst1 = create_lst(m1)
print(timeit('find_median_cycle(lst1.copy(), m1)', globals=globals(), number=1000))  # 0.004336400000000001

m2 = 100
lst2 = create_lst(m2)
print(timeit('find_median_cycle(lst2.copy(), m2)', globals=globals(), number=1000))  # 0.22498410000000002

m3 = 1000
lst3 = create_lst(m3)
print(timeit('find_median_cycle(lst3.copy(), m3)', globals=globals(), number=1000))  # 22.4307817
