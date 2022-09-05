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
import time
from random import randint


# Для создания исходных списков используем функцию fill_list

def fill_list(range_step):
    test1_list = []
    for ii in range(0, 2 * range_step + 1):
        test1_list.append(randint(1, 2 * range_step))
    return test1_list


def med_wo_sort(list_to_med1):
    i = 0
    list_to_med = list_to_med1
    count = len(list_to_med)
    med_ind = int((count - 1) / 2)
    start_val = time.time()
    while i < med_ind:
        list_to_med.remove(min(list_to_med))
        i += 1
    end_val = time.time()
    med_num = min(list_to_med)
    return end_val - start_val, med_num


# Создадим списки, которые будем сортировать
list_to_read11 = fill_list(5)
list_to_read101 = fill_list(50)
list_to_read1001 = fill_list(500)

print('______________Замеры поиска медианы списка из 11 элементов___________________')

print(f'Список для поиска медианы: {list_to_read11}')
time_count1, med = med_wo_sort(list_to_read11)
print(f'Время поиска медианы: {time_count1}')
print(f'Медиана:{med}')

print('______________Замеры поиска медианы списка из 101 элементов___________________')

print(f'Список для поиска медианы: {list_to_read101}')
time_count11, med2 = med_wo_sort(list_to_read101)
print(f'Время поиска медианы: {time_count11}')
print(f'Медиана:{med2}')

print('______________Замеры поиска медианы списка из 1001 элементов___________________')

print(f'Список для поиска медианы: {list_to_read1001}')
time_count111, med3 = med_wo_sort(list_to_read1001)
print(f'Время поиска медианы: {time_count111}')
print(f'Медиана:{med3}')
