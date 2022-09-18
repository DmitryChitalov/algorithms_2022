"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
import statistics
from random import randint
from timeit import timeit

m = 10
my_list = [randint(1, 100) for _ in range(2 * m + 1)]
print('рандомный список ', 'из ', m, ' элементов: \n', my_list)
print('Медиана: ', statistics.median(my_list[:]))
print('время на выполнение составило: ',
      round(timeit("statistics.median(my_list[:])", globals=globals(), number=1000), 3))

m = 100
my_list = [randint(1, 100) for _ in range(2 * m + 1)]
print('рандомный список ', 'из ', m, ' элементов: \n', my_list)
print('Медиана: ', statistics.median(my_list[:]))
print('время на выполнение составило: ',
      round(timeit("statistics.median(my_list[:])", globals=globals(), number=1000), 3))

m = 1000
my_list = [randint(1, 100) for _ in range(2 * m + 1)]
print('рандомный список ', 'из ', m, ' элементов: \n', my_list)
print('Медиана: ', statistics.median(my_list[:]))
print('время на выполнение составило: ',
      round(timeit("statistics.median(my_list[:])", globals=globals(), number=1000), 3))

# Самый эффективный способом является применение встроенной функции
# Лучше использавать встроенные функции сортировки, т.к. они реализованы