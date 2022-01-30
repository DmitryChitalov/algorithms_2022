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
from timeit import timeit
from random import randint
from statistics import median

m = 10
arr_10 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("median(arr_10[:])", globals=globals(), number=1000))

m = 100
arr_100 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("median(arr_100[:])", globals=globals(), number=1000))

m = 1000
arr_1000 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("median(arr_1000[:])", globals=globals(), number=30))


"""
Результаты:
            m = 10 - 0.0024898000000000142
            m = 100 - 0.015809900000000016
            m = 1000 - 0.013713100000000006
            
            Вывод:
                    Самый лучший вариант решения через функцию median из statistics
                    Хуже всех себя показал способ нахождения медианы через сортировку
"""