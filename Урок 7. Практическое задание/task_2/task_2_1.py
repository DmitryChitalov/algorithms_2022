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


# "Гномья"
def gnome_sort(lst_obj):
    i = 0
    while i < len(lst_obj):
        if i == 0:
            i += 1
        if lst_obj[i] >= lst_obj[i - 1]:
            i += 1
        else:
            lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
            i -= 1
    return lst_obj


m = 10
list1 = [randint(-100, 100) for _ in range(2*m + 1)]
print(timeit("gnome_sort(orig_list)", globals=globals(), number=1000))
print(list1[m])

m = 100
list_2 = [randint(-100, 100) for _ in range(2*m + 1)]
print(timeit("gnome_sort(orig_list_1)", globals=globals(), number=1000))
print(list_2[m])

m = 1000
list_3 = [randint(-100, 100) for _ in range(2*m + 1)]
print(timeit("gnome_sort(orig_list_2)", globals=globals(), number=1000))
print(list_3[m])

"""
10 элементов:
0.026555499999999982 
-13
100 элементов:
0.072162
4
1000 элементов:
2.057299
0
"""
