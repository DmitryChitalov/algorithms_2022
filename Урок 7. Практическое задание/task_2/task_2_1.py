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
# Использовал оптимизированную гномью сортировку
from timeit import timeit
from random import randint
def gnome_opt_sort(my_list):
      i, j, size = 1, 2, len(my_list)
      while i < size:
            if my_list[i - 1] <= my_list[i]:
                  i, j = j, j + 1
            else:
                  my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
                  i -= 1
                  if i == 0:
                        i, j = j, j + 1
      return  my_list

def get_mediana(my_list, m):
      gnome_opt_sort(my_list)
      return my_list[m]

m = 10
my_list_10 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("get_mediana(my_list_10[:], m)", globals=globals(), number=1000))

m = 100
my_list_100 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("get_mediana(my_list_100[:], m)", globals=globals(), number=1000))

m = 1000
my_list_1000 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("get_mediana(my_list_1000[:], m)", globals=globals(), number=1000))
# Результаты:
# m 10 - 0.1154299
# m 100 - 9.2553353
# m 1000 - 1022.599794




