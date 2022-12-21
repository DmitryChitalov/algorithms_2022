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

from random import randint
from timeit import timeit


def dwarf_sort(lst_obj):
    i = 1
    while i < len(lst_obj):
        if lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            if i > 1:
                i -= 1

    return lst_obj


m = 5
orig_list = [randint(1, 9) for _ in range(2 * m + 1)]
sort_list = dwarf_sort(orig_list[:])
print('Медиана: ', sort_list, sort_list[m], sep='\n')

# замеры 10

print(orig_list, dwarf_sort(orig_list[:]),
      timeit(
          "dwarf_sort(orig_list[:])",
          globals=globals(),
          number=100), sep='\n')

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100

print(orig_list, dwarf_sort(orig_list[:]),
      timeit(
          "dwarf_sort(orig_list[:])",
          globals=globals(),
          number=100), sep='\n')

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000

print(orig_list, dwarf_sort(orig_list[:]),
      timeit(
          "dwarf_sort(orig_list[:])",
          globals=globals(),
          number=100), sep='\n')
