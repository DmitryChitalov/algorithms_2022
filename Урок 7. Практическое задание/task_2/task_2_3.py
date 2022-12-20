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
from random import randint
from timeit import timeit
from statistics import median


def mediana(lst):
    return median(lst)



m = 10
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "mediana(lst[:])",
        globals=globals(),
        number=100))


m = 100
lst = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "mediana(lst[:])",
        globals=globals(),
        number=100))


m = 1000
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "mediana(lst[:])",
        globals=globals(),
        number=100))


"""
0.0004943999999999782 10 элементов
0.004067300000000024  100 элементов
0.049219400000000024  1000 элементов

Вывод: самой быстрой оказаласб встроенная функция median() для поиска медианы из модуля
statistics 
"""