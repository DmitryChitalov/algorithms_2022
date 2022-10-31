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
import statistics
from timeit import timeit
from statistics import median

def generate_lst(n):
    lst = [random.randint(-100, 100) for i in range(2 * n + 1)]
    return lst


def mediana_with_statistics(lst):
    return statistics.median(lst)


# m = int(input())
# unsorted_lst = generate_lst(m)
# print(unsorted_lst)
# print(mediana_with_statistics(unsorted_lst))


lst_1 = generate_lst(10)
lst_2 = generate_lst(100)
lst_3 = generate_lst(1000)
print(timeit("mediana_with_statistics(lst_1)", globals=globals(), number=1000))
print(timeit("mediana_with_statistics(lst_2)", globals=globals(), number=1000))
print(timeit("mediana_with_statistics(lst_3)", globals=globals(), number=1000))


"""
10 - 0.0004893000004813075
100 - 0.004737800016300753
1000 - 0.13076279999222606
"""


"""
Самый медленный вариант - путем сортировки списка.
Самый короткий, но почему-то не самый быстрый - median
Самый быстрый - через удаление, хотя это не понятно, потому что в интернете пишут обратное давольно долго сидел,
 пытался понять, не понял.
"""