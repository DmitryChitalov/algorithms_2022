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

"""
Убираем из массива максимальные значения m раз, 
в итоге останется половина массива + медиана в качестве наибольшего значения.
Ее и выводим.
"""


def find_median(lst):
    i = m
    while i != 0:
        lst.remove(max(lst))
        i -= 1
    return max(lst)


m = 5
my_list = [randint(1, 200)for i in range(2 * m + 1)]
print(my_list)
print(find_median(my_list))


"""
Делаем замеры на массивах разной длины
"""


m_1 = 10
my_list_1 = [randint(1, 200) for _ in range(2 * m_1 + 1)]
print(
    timeit(
        "find_median(my_list_1[:])",
        globals=globals(),
        number=100))


m_2 = 100
my_list_2 = [randint(1, 200) for _ in range(2 * m_2 + 1)]

print(
    timeit(
        "find_median(my_list_2[:])",
        globals=globals(),
        number=100))


m_3 = 1000
my_list_3 = [randint(1, 200)for _ in range(2 * m_3 + 1)]

print(
    timeit(
        "find_median(my_list_3[:])",
        globals=globals(),
        number=100))

"""
0.0006163750000000023
0.004217046000000009
0.037459154999999994
"""