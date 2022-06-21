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
from statistics import median
from timeit import timeit


def middle_elem(lst_obj):
    return median(lst_obj)


def middle_nosort(lst_obj):
    copy_lst = lst_obj
    for i in range(len(lst_obj) // 2):
        copy_lst.remove(min(copy_lst))
    return min(copy_lst)


def middle_bubble(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj[(len(lst_obj) // 2)]


m = 10
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Медиана для массива из 21 элементов (пузырьковая сортировка): {middle_bubble(orig_list)}')
print(timeit("middle_bubble(orig_list[:])", globals=globals(), number=1000))
print(f'Медиана для массива из 21 элементов (встроенная функция): {middle_elem(orig_list)}')
print(timeit("middle_elem(orig_list[:])", globals=globals(), number=1000))
print(f'Медиана для массива из 21 элементов (без сортировки): {middle_nosort(orig_list)}')
print(timeit("middle_nosort(orig_list[:])", globals=globals(), number=1000))
print('-' * 50)
m = 100
orig_list_1 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Медиана для массива из 201 элементов (пузырьковая сортировка): {middle_bubble(orig_list_1)}')
print(timeit("middle_bubble(orig_list_1[:])", globals=globals(), number=1000))
print(f'Медиана для массива из 201 элементов (встроенная функция): {middle_elem(orig_list_1)}')
print(timeit("middle_elem(orig_list_1[:])", globals=globals(), number=1000))
print(f'Медиана для массива из 201 элементов (без сортировки): {middle_nosort(orig_list_1)}')
print(timeit("middle_nosort(orig_list_1[:])", globals=globals(), number=1000))
print('-' * 50)
m = 1000
orig_list_2 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Медиана для массива из 2001 элементов (пузырьковая сортировка): {middle_bubble(orig_list_2)}')
print(timeit("middle_bubble(orig_list_2[:])", globals=globals(), number=1000))
print(f'Медиана для массива из 2001 элементов (встроенная функция): {middle_elem(orig_list_2)}')
print(timeit("middle_elem(orig_list_2[:])", globals=globals(), number=1000))
print(f'Медиана для массива из 2001 элементов (без сортировки): {middle_nosort(orig_list_2)}')
print(timeit("middle_nosort(orig_list_2[:])", globals=globals(), number=1000))

'''Вывод: быстрее всего считается медиана с помощью встроенной функции (median), 
дольше всего - с помощью сортировки (в данном случае была использована пузырькова сортировка).

Замеры для массива из 21 элементов 
пузырьковая сортировка: 0.027986699948087335
встроенная функция:     0.0006799999973736703
без сортировки:         0.0019648000015877187
--------------------------------------------------
Замеры для массива из 201 элементов 
пузырьковая сортировка: 2.233826300012879
встроенная функция:     0.0033110000076703727
без сортировки:         0.05121349997352809
--------------------------------------------------
Замеры для массива из 2001 элементов 
пузырьковая сортировка: 225.15585969999665
встроенная функция:     0.015139999974053353
без сортировки:         3.5131546999909915
'''
