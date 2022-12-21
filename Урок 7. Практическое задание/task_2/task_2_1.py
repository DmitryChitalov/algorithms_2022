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


# m = 3
# my_list = [randint(-100,100) for i in range(2 * m + 1)]
# print(my_list)
# my_list2 = sorted(my_list)
# print(my_list2)
# print(my_list2[m])

def dwarf_sort(lst_obj, num):

    i = 1
    while i < len(lst_obj):
        if lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            if i > 1:
                i -= 1

    return f'Oтсортированный список {lst_obj}' \
           f' Медиана списка {lst_obj[num]}'


m = 7
my_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(dwarf_sort(my_list, m))

my_list10 = [randint(-100, 100) for x in range(10)]
print('Длина массива 10 элементов', timeit(
        "dwarf_sort(my_list10[:], m)",
        globals=globals(),
        number=100))


my_list100 = [randint(-100, 100) for _ in range(100)]
print('Длина массива 100 элементов', timeit(
        "dwarf_sort(my_list100[:], m)",
        globals=globals(),
        number=100))

my_list1000 = [randint(-100, 100) for j in range(1000)]
print('Длина массива 1000 элементов', timeit(
        "dwarf_sort(my_list1000[:], m)",
        globals=globals(),
        number=100))

'''
Длина массива 10 элементов 0.0016113229794427752
Длина массива 100 элементов 0.24784921703394502
Длина массива 1000 элементов 19.009888597996905
'''