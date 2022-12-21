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

В конце сделайте аналитику какой из трех способов оказался эффективнее
"""

from random import randint
from timeit import timeit
from statistics import median
from task_07_2_1 import find_median_with_sort
from task_07_2_2 import find_median_without_sort

print('Для массива из 9 элементов:')
lst_test_9 = [randint(-100, 100) for _ in range(9)]
number_executions_for_lst_test_9 = 1000
print(f'Проверка того, что все 3 функции находят одну и ту же медиану: '
      f'{find_median_with_sort(lst_test_9[:]) == find_median_without_sort(lst_test_9[:]) == median(lst_test_9)}')
print('Поиск медианы с помощью сортировки массива:', end=' ')
print(timeit("find_median_with_sort(lst_test_9[:])", globals=globals(), number=number_executions_for_lst_test_9))
print('Поиск медианы без сортировки массива:', end=' ')
print(timeit("find_median_without_sort(lst_test_9[:])", globals=globals(), number=number_executions_for_lst_test_9))
print('Поиск медианы с помощью встроенной функции:', end=' ')
print(timeit("median(lst_test_9)", globals=globals(), number=number_executions_for_lst_test_9))


print('\nДля массива из 99 элементов:')
lst_test_99 = [randint(-100, 100) for _ in range(99)]
number_executions_for_lst_test_99 = 100
print(f'Проверка того, что все 3 функции находят одну и ту же медиану: '
      f'{find_median_with_sort(lst_test_99[:]) == find_median_without_sort(lst_test_99[:]) == median(lst_test_99)}')
print('Поиск медианы с помощью сортировки массива:', end=' ')
print(timeit("find_median_with_sort(lst_test_99[:])", globals=globals(), number=number_executions_for_lst_test_99))
print('Поиск медианы без сортировки массива:', end=' ')
print(timeit("find_median_without_sort(lst_test_99[:])", globals=globals(), number=number_executions_for_lst_test_99))
print('Поиск медианы с помощью встроенной функции:', end=' ')
print(timeit("median(lst_test_99)", globals=globals(), number=number_executions_for_lst_test_99))

print('\nДля массива из 999 элементов:')
lst_test_999 = [randint(-100, 100) for _ in range(999)]
number_executions_for_lst_test_999 = 10
print(f'Проверка того, что все 3 функции находят одну и ту же медиану: '
      f'{find_median_with_sort(lst_test_999[:]) == find_median_without_sort(lst_test_999[:]) == median(lst_test_999)}')
print('Поиск медианы с помощью сортировки массива:', end=' ')
print(timeit("find_median_with_sort(lst_test_999[:])", globals=globals(), number=number_executions_for_lst_test_999))
print('Поиск медианы без сортировки массива:', end=' ')
print(timeit("find_median_without_sort(lst_test_999[:])", globals=globals(), number=number_executions_for_lst_test_999))
print('Поиск медианы с помощью встроенной функции:', end=' ')
print(timeit("median(lst_test_999)", globals=globals(), number=number_executions_for_lst_test_999))


# Самым эффективным оказался поиск медианы с помощью функции median из модуля statistics,
# в ней сортировка массива происходит с помощью встроенной функции sorted, которая, в свою очередь,
# использует гибридный алгоритм сортировки (Timsort).
