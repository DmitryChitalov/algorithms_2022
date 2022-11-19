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


def built_in(lst_obj):
    return median(lst_obj)


m = int(input('Введите натуральное число: '))
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(orig_list)
print(f'Медиана массива равна: {built_in(orig_list)}')

# при 10 значениях
m = 10
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(
    timeit(
          "built_in(orig_list[:])",
          globals=globals(),
          number=1000))
# при 100
m = 100
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(
    timeit(
          "built_in(orig_list[:])",
          globals=globals(),
          number=1000))
# при 1000
m = 1000
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(
    timeit(
          "built_in(orig_list[:])",
          globals=globals(),
          number=1000))

"""
Введите натуральное число: 15
[599, 645, 393, 297, 520, 327, 598, 73, 259, 481, 177, 286, 489, 520, 308, 545,
 188, 471, 594, 685, 602, 928, 41, 61, 197, 106, 90, 416, 221, 490, 395]
Медиана массива равна: 395
0.0009195999991788995
0.007918600000266451
0.18277349999698345
"""
"""
Однозначно третий способ(встроенная функция) наиболее эффективен. А сымый не
эффективный - нахождение медианы в неотсортированном массиве
"""
