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


# Ищем медиану путем удаления максимальных элементов
def without_sort(rand_list):
    temp_list = rand_list
    for i in range(len(rand_list) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)


m = 10
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "without_sort(rand_list[:])",
        globals=globals(),
        number=100))

m = 100
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "without_sort(rand_list[:])",
        globals=globals(),
        number=100))

m = 1000
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "without_sort(rand_list[:])",
        globals=globals(),
        number=100))
'''
0.0005048750026617199
0.02455795900459634
1.486662333001732
'''