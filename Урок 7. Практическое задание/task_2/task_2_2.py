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
# Поиск медианы осуществим путем удаления max элементов
from random import randint
from timeit import timeit


def delete_sort(rand_list):
    temp_list = rand_list
    for i in range(len(rand_list) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)


m = 10
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "delete_sort(rand_list[:])",
        globals=globals(),
        number=100))

m = 100
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "delete_sort(rand_list[:])",
        globals=globals(),
        number=100))

m = 1000
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "delete_sort(rand_list[:])",
        globals=globals(),
        number=100))

'''
для 10:
0.0011353000300005078
для 100:
0.0706582999555394
для 1000:
2.7149939000373706
'''