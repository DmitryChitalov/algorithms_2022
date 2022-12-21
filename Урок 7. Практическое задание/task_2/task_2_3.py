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


def internal_sort(lst_obj):
    lst_obj.sort()
    return lst_obj

m = 10
orig_list = [randint(1, 10) for _ in range(2*m+1)]
print(orig_list)
sort_list = internal_sort(orig_list[:])
print ('Медиана: ' , sort_list, sort_list[m],sep='\n')



# замеры 10

print(orig_list,internal_sort(orig_list[:]),
    timeit(
        "internal_sort(orig_list[:])",
        globals=globals(),
        number=100),sep='\n')


orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100

print(orig_list,internal_sort(orig_list[:]),
    timeit(
        "internal_sort(orig_list[:])",
        globals=globals(),
        number=100) ,sep='\n')


orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000

print(orig_list,internal_sort(orig_list[:]),
    timeit(
        "internal_sort(orig_list[:])",
        globals=globals(),
        number=100),sep='\n' )

"""
Встроенная функция показала наилучшие результаты на порядок быстрее как при малых массивах, так и при больших .
Самая медленная сортировка Шелла
"""
