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


def get_mediana(my_list):
    n = my_list
    for i in range(len(my_list) // 2):
        n.remove(max(n))
    return max(n)


m = 10
my_list = [randint(1, 100) for _ in range(2 * m + 1)]
print('рандомный список ', 'из ', m, ' элементов: \n', my_list)
print('Медиана: ', get_mediana(my_list[:]))
print('время на выполнение составило: ', round(timeit("get_mediana(my_list[:])", globals=globals(), number=1000), 3))

m = 100
my_list = [randint(1, 100) for _ in range(2 * m + 1)]
print('\n рандомный список ', 'из ', m, ' элементов: \n', my_list)
print('Медиана: ', get_mediana(my_list[:]))
print('время на выполнение составило: ', round(timeit("get_mediana(my_list[:])", globals=globals(), number=1000), 3))

m = 1000
my_list = [randint(1, 100) for _ in range(2 * m + 1)]
print('\n рандомный список ', 'из ', m, ' элементов: \n', my_list)
print('Медиана: ', get_mediana(my_list[:]))
print('время на выполнение составило: ', round(timeit("get_mediana(my_list[:])", globals=globals(), number=1000), 3))

