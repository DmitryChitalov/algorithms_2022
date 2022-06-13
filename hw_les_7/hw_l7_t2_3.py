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
import random
from numpy import median
from timeit import timeit
from hw_l7_t2_1 import my_med
from hw_l7_t2_2 import max_med

m1 = 10
m2 = 100
m3 = 1000
my_list1 = list(round(random.random() * 100) for i in range(2 * m1 + 1))
my_list2 = list(round(random.random() * 100) for i in range(2 * m2 + 1))
my_list3 = list(round(random.random() * 100) for i in range(2 * m3 + 1))

print('Через встроенную функцию')
print(median(my_list1), timeit('median(my_list1)', globals=globals(), number=100))
print(median(my_list2), timeit('median(my_list2)', globals=globals(), number=100))
print(median(my_list3), timeit('median(my_list3)', globals=globals(), number=100))
print('Через гномью сортировку')
print(my_med(my_list1, m1), timeit('my_med(my_list1, m1)', globals=globals(), number=100))
print(my_med(my_list2, m2), timeit('my_med(my_list2, m2)', globals=globals(), number=100))
print(my_med(my_list3, m3), timeit('my_med(my_list3, m3)', globals=globals(), number=100))
print('Без сортировки')
print(max_med(my_list1, m1), timeit('max_med(my_list1, m1)', globals=globals(), number=100))
print(max_med(my_list2, m2), timeit('max_med(my_list2, m2)', globals=globals(), number=100))
print(max_med(my_list3, m3), timeit('max_med(my_list3, m3)', globals=globals(), number=100))


