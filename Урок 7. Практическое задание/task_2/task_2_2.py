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

"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов

Шелла сортировка
"""

from random import randint
from timeit import timeit


def shell_sort(lst_obj):
    step = len(lst_obj) // 2
    while step > 0:
        for i in range(step,len(lst_obj)):
            j = i
            tmp = lst_obj[i]
            while j>=step and lst_obj[j-step] > tmp:
                lst_obj[j] = lst_obj[j - step]
                j = j-step
            lst_obj[j] = tmp
        step = step // 2
    return lst_obj

m = 10
orig_list = [randint(1, 10) for _ in range(2*m+1)]
print(orig_list)
sort_list = shell_sort(orig_list[:])
print ('Медиана: ' , sort_list, sort_list[m],sep='\n')



# замеры 10

print(orig_list,shell_sort(orig_list[:]),
    timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=100),sep='\n')


orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100

print(orig_list,shell_sort(orig_list[:]),
    timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=100) ,sep='\n')


orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000

print(orig_list,shell_sort(orig_list[:]),
    timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=100),sep='\n' )


