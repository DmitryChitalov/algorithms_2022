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

Гномья сортировка

"""

import time
from random import randint


# Для создания исходных списков используем функцию fill_list

def fill_list(range_step):
    test1_list = []
    for ii in range(0, 2 * range_step + 1):
        test1_list.append(randint(1, 2 * range_step))
    return test1_list


def gnome_sort(list_to_sort):
    i = 0
    j = 2
    list_sorted = list_to_sort
    count = len(list_to_sort)
    med_ind = int((count - 1) / 2)
    start_val = time.time()
    while i < count:
        if list_sorted[i - 1] <= list_sorted[i]:
            i, j = j, j + 1
        else:
            list_sorted[i - 1], list_sorted[i] = list_sorted[i], list_sorted[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    end_val = time.time()
    return end_val - start_val, list_sorted, list_sorted[med_ind]


# Создадим списки, которые будем сортировать
list_to_read11 = fill_list(5)
list_to_read101 = fill_list(50)
list_to_read1001 = fill_list(500)

print('______________Замеры сортировки списка из 11 элементов___________________')

print(f'Несортированнный список:{list_to_read11}')
time_count1, sorted11, med = gnome_sort(list_to_read11)
print(f'Время сортировки: {time_count1}')
print(f'Cортированнный список:{sorted11}')
print(f'Медиана:{med}')

print('______________Замеры сортировки списка из 101 элементов___________________')

print(f'Несортированнный список:{list_to_read101}')
time_count11, sorted111, med2 = gnome_sort(list_to_read101)
print(f'Время сортировки: {time_count11}')
print(f'Cортированнный список:{sorted111}')
print(f'Медиана:{med2}')

print('______________Замеры сортировки списка из 1001 элементов___________________')

print(f'Несортированнный список:{list_to_read1001}')
time_count111, sorted1111, med3 = gnome_sort(list_to_read1001)
print(f'Время сортировки: {time_count111}')
print(f'Cортированнный список:{sorted1111}')
print(f'Медиана:{med3}')
