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

def median(lists, num):
    for i in range(num):
        lists.remove(max(lists))
    return max(lists)


m = 5
my_list10 = [randint(-100, 100) for i in range(2 * m + 1)]

print('Длина массива 10 элементов', timeit(
        "median(my_list10[:], m)",
        globals=globals(),
        number=100))

m2 = 50
my_list100 = [randint(-100, 100) for _ in range(2 * m2 + 1)]

print('Длина массива 100 элементов', timeit(
        "median(my_list100[:], m)",
        globals=globals(),
        number=100))

m3 = 500
my_list1000 = [randint(-100, 100) for _ in range(2 * m3 + 1)]

print('Длина массива 1000 элементов', timeit(
        "median(my_list1000[:], m)",
        globals=globals(),
        number=100))

'''
Длина массива 10 элементов 0.00032534392084926367
Длина массива 100 элементов 0.001874060952104628
Длина массива 1000 элементов 0.01595569192431867
'''
