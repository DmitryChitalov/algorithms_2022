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


def gnome_sort(my_list):
    l = len(my_list)
    i = 1
    while i < l:
        if i == 0:
            i = 1
        if my_list[i] > my_list[i - 1]:
            my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
            i -= 1
        else:
            i += 1
    return my_list


m = 10
rand_list = [random.randrange(-100, 100) for i in range(2 * m + 1)]
print('список для m=10: ', rand_list, '\n', 'время выполнения для m=10: ',
      round(timeit('(gnome_sort(rand_list[:]))[m]', globals=globals(), number=1), 6))
print(f'Медиана: {rand_list[m]}')

m = 100
rand_list = [random.randrange(-100, 100) for i in range(2 * m + 1)]
print('список для m=100: ', rand_list, '\n', 'время выполнения для m=100: ',
      round(timeit('(gnome_sort(rand_list[:]))[m]', globals=globals(), number=1), 6))
print(f'Медиана: {rand_list[m]}')

m = 1000
rand_list = [random.randrange(-100, 100) for i in range(2 * m + 1)]
print('список для m=1000: ', rand_list, '\n', 'время выполнения для m=1000: ',
      round(timeit('(gnome_sort(rand_list[:]))[m]', globals=globals(), number=1), 6))
print(f'Медиана: {rand_list[m]}')