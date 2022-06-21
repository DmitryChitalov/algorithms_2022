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
"""


from random import randint
from timeit import timeit


# Гномья сортировка
def gnome_sort(lst_obj):
    len_list = len(lst_obj)
    i = 0
    while i < len_list:
        if i == 0:
            i += 1
        if lst_obj[i] >= lst_obj[i - 1]:
            i += 1
        else:
            lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
            i -= 1
    return lst_obj[(len(lst_obj) // 2)]


# Сортировка расчёской
def brush_sort(lst_obj):
    step = len(lst_obj) - 1
    while step > 0:
        for i in range(0, len(lst_obj)-step):
            if lst_obj[i] > lst_obj[i+step]:
                lst_obj[i], lst_obj[i+step] = lst_obj[i+step], lst_obj[i]
        step = int(step // 1.25)
    return lst_obj[(len(lst_obj) // 2)]


# Сортировка Шелла
def shell_sort(lst_obj):
    step = len(lst_obj)//2
    while step > 0:
        for i in range(step, len(lst_obj)):
            delta = i - step
            while delta >= 0 and lst_obj[delta] > lst_obj[i]:
                lst_obj[delta], lst_obj[i] = lst_obj[i], lst_obj[delta]
                delta -= step
        step //= 2
    return lst_obj[(len(lst_obj) // 2)]


orig_list = [randint(-100, 100) for _ in range(0, 2 * 10 + 1)]
orig_list_1 = [randint(-100, 100) for _ in range(0, 2 * 100 + 1)]
orig_list_2 = [randint(-100, 100) for _ in range(0, 2 * 1000 + 1)]


print(f'Медиана для массива из 21 элементов (гномья сортировка): {gnome_sort(orig_list)}')
print(timeit("gnome_sort(orig_list[:])", globals=globals(), number=100))
print(f'Медиана для массива из 201 элементов (гномья сортировка): {gnome_sort(orig_list_1)}')
print(timeit("gnome_sort(orig_list_1[:])", globals=globals(), number=100))
print(f'Медиана для массива из 2001 элементов (гномья сортировка): {gnome_sort(orig_list_2)}')
print(timeit("gnome_sort(orig_list_2[:])", globals=globals(), number=100))
print('-' * 50)
print(f'Медиана для массива из 21 элементов (сортировка расческой): {brush_sort(orig_list)}')
print(timeit("brush_sort(orig_list[:])", globals=globals(), number=100))
print(f'Медиана для массива из 201 элементов (сортировка расческой): {brush_sort(orig_list_1)}')
print(timeit("brush_sort(orig_list_1[:])", globals=globals(), number=100))
print(f'Медиана для массива из 2001 элементов (сортировка расческой): {brush_sort(orig_list_2)}')
print(timeit("brush_sort(orig_list_2[:])", globals=globals(), number=100))
print('-' * 50)
print(f'Медиана для массива из 21 элементов (сортировка Шелла): {shell_sort(orig_list)}')
print(timeit("shell_sort(orig_list[:])", globals=globals(), number=100))
print(f'Медиана для массива из 201 элементов (сортировка Шелла): {shell_sort(orig_list_1)}')
print(timeit("shell_sort(orig_list_1[:])", globals=globals(), number=100))
print(f'Медиана для массива из 2001 элементов (сортировка Шелла): {shell_sort(orig_list_2)}')
print(timeit("shell_sort(orig_list_2[:])", globals=globals(), number=100))

'''
Вывод: получение медианы с помощью гномьей сортировка гораздо быстрее, 
чем получение медианы с помощью сортировки расческой или сортировки Шелла.

Замеры для массива из 21 элементов 
гномья сортировка:      0.0003744999994523823
сортировка расческой:   0.0017420999938622117
сортировка Шелла:       0.0014377000043168664
--------------------------------------------------
Замеры для массива из 201 элементов 
гномья сортировка:      0.003842300036922097
сортировка расческой:   0.03309119999175891
сортировка Шелла:       0.018507500004488975
--------------------------------------------------
Замеры для массива из 2001 элементов 
гномья сортировка:      0.03214480000315234
сортировка расческой:   0.5295008999528363
сортировка Шелла:       0.3160593999782577
'''
