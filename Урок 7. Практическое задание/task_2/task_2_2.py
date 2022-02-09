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


def medi_search(lst):
    for i in range(len(lst) // 2):
        lst.pop(lst.index(max(lst)))
    return max(lst)


m = 26
my_array = [randint(-100, 100) for _ in range(2 * m + 1)]
print(my_array)
print(f'Медиана ряда: {medi_search(my_array)}')

# замеры 10
print(
    timeit(
        "medi_search(my_array)",
        globals=globals(),
        number=1000))

# замеры 100
m = 126
my_array = [randint(-100, 100) for _ in range(2 * 100 + 1)]
print(
    timeit(
        "medi_search(my_array)",
        globals=globals(),
        number=1000))

# замеры 1000
my_array = [randint(-100, 100) for _ in range(2 * 1000 + 1)]
print(
    timeit(
        "medi_search(my_array)",
        globals=globals(),
        number=1000))

"""
0.00040699999999999764
0.0006743000000000027
0.0430266
"""