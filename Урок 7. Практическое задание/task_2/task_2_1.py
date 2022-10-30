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
import random
from timeit import timeit


def generate_lst(n):
    lst = [random.randint(-100, 100) for i in range(2 * n + 1)]
    return lst


def gnome_sort(lst):
    index = 1
    i = 0
    while i < len(lst) - 1:
        if lst[i] <= lst[i + 1]:
            i, index = index, index + 1
        else:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            if i > 0:
                i -= 1
            else:
                i, index = index, index + 1
    mediana = lst[len(lst) // 2]
    return lst, mediana


# m = int(input())
# unsorted_lst = generate_lst(m)
# print(gnome_sort(unsorted_lst))


lst_1 = generate_lst(10)
lst_2 = generate_lst(100)
lst_3 = generate_lst(1000)
print(timeit("gnome_sort(lst_1)", globals=globals(), number=1000))
print(timeit("gnome_sort(lst_2)", globals=globals(), number=1000))
print(timeit("gnome_sort(lst_3)", globals=globals(), number=1000))


"""
10 - 0.0019659000099636614
100 - 0.019264100003056228
1000 - 0.3686249000020325
"""