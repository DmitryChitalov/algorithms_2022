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
import numpy
from random import randint
from timeit import timeit


def median_lib_stat(lst):
    return statistics.median(lst)


def median_lib_numpy(lst):
    return numpy.median(lst)


def median_sorted(lst):  # средний, если len(list_) нечет, или среднее от двух средних значений
    q, r = divmod(len(lst), 2)
    return sorted(lst)[q] if r else sum(sorted(lst)[q - 1:q + 1]) / 2


number = 1000
x = [randint(0, 100) for _ in range(2 * number + 1)]
print(median_lib_stat(x))
print(median_lib_numpy(x))
print(median_sorted(x))

# замеры на массивах длиной 10, 100, 1000 элементов
print('замеры на массиве длиной 10 элементов')
x1 = [randint(-100, 100) for _ in range(10)]
print(timeit("median_lib_stat(x1[:])", globals=globals(), number=1000))  # 0.0006058000000000174
print(timeit("median_lib_numpy(x1[:])", globals=globals(), number=1000))  # 0.017990200000000012
print(timeit("median_sorted(x1[:])", globals=globals(), number=1000))  # 0.0006047000000000136

print('замеры на массиве длиной 100 элементов')
x2 = [randint(-100, 100) for _ in range(100)]
print(timeit("median_lib_stat(x2[:])", globals=globals(), number=1000))  # 0.005032000000000009
print(timeit("median_lib_numpy(x2[:])", globals=globals(), number=1000))  # 0.025376800000000005
print(timeit("median_sorted(x2[:])", globals=globals(), number=1000))  # 0.0006047000000000136

print('замеры на массиве длиной 1000 элементов')
x3 = [randint(-100, 100) for _ in range(1000)]
print(timeit("median_lib_stat(x3[:])", globals=globals(), number=1000))  # 0.06905280000000003
print(timeit("median_lib_numpy(x3[:])", globals=globals(), number=1000))  # 0.08249859999999998
print(timeit("median_sorted(x3[:])", globals=globals(), number=1000))  # 0.07967219999999997

print('замеры на массиве длиной 100000 элементов')
x4 = [randint(-100, 100) for _ in range(100000)]
print(timeit("median_lib_stat(x4[:])", globals=globals(), number=100))  # 0.9890376
print(timeit("median_lib_numpy(x4[:])", globals=globals(), number=100))  # 0.7598885
print(timeit("median_sorted(x4[:])", globals=globals(), number=100))  # 0.96836969

"""
Видим, что на небольших массивах быстрее всех встроенная sorted и из модуля statistics, а на больших
более эффективна из модуля NumPy.
"""
