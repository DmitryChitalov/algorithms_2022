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


def find_median(m):
    lst = [randrange(-100, 100) for _ in range(2 * m + 1)]
    work_lst = lst.copy()
    for _ in range(m):
        work_lst.remove(max(work_lst))
    return lst, max(work_lst)


print(find_median(2))

print(timeit('find_median(10)', globals=globals(), number=1000))  # 0.015245799999999997
print(timeit('find_median(100)', globals=globals(), number=1000))  # 0.3195213
print(timeit('find_median(1000)', globals=globals(), number=1000))  # 23.6803932
