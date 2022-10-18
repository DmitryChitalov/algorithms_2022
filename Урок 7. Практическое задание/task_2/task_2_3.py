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

Листинг работы кода приведен на строках 61:76

Аналитика:
для массива 11 элементов:
"Gnome"  Sorting time (sec)                 = 0.0049036 (сортировка)
"sorting_by_del1" Sorting time of   (sec)   = 0.00498   (обрезка + медианное число)
"sorting_by_del2" Sorting time of   (sec)   = 0.00527   (обрезка + медианное число)
"median" Sorting time  (sec)                = 0.00036689999999999987 ( медианное число)

для массива 101 элемент:
"Gnome" Sorting time (sec)                = 0.3836452   (сортировка)
"sorting_by_del1" Sorting time of   (sec) = 0.1077575   (обрезка + медианное число)
"sorting_by_del2" Sorting time of   (sec) = 0.12418159999999998     (обрезка + медианное число)
"median" Sorting time   (sec)               = 0.0026787999999999985  ( медианное число)

для массива 1001 элемент:
"Gnome"  Sorting time (sec)                 = 37.4209624        (сортировка)
"sorting_by_del1" Sorting time of   (sec)   = 6.6253855         (обрезка + медианное число)
"sorting_by_del2" Sorting time of   (sec)   = 7.1048184         (обрезка + медианное число)
"median"  Sorting time of   (sec)           = 0.0597834         ( медианное число)

Выводы:
поиск медианного числа быстрее всего работает встроенным  методом "median";
поиск медианного числа сортировкой Gnome работает дольше всего;
Фуyкции  "sorting_by_del1" и "sorting_by_del2" используют обрезку массива,
и, думаю что не являются точными функциями определения медианного числа,
работают со средней скоростью.
"""

from random import randint
from statistics import median
from timeit import timeit

print('\n --- Замеры для median --- ')
for i in range(1, 4):
    list_len = 10 ** i + 1
    print(f'\n for list of size {list_len}')
    lst_object = [randint(-100, 100) for _ in range(list_len)]
    print(f' Median = {median(lst_object[:])}')
    print(' Sorting time of "median"  (sec) = ', end='')
    print(timeit("median(lst_object[:])", globals=globals(), number=1000))

#
#  --- Замеры для median ---
#
#  for list of size 11
#  Median = -10
#  Sorting time of "median"  (sec) = 0.00036689999999999987
#
#  for list of size 101
#  Median = 11
#  Sorting time of "median"  (sec) = 0.0026787999999999985
#
#  for list of size 1001
#  Median = -7
#  Sorting time of "median"  (sec) = 0.0597834
#
# Process finished with exit code 0