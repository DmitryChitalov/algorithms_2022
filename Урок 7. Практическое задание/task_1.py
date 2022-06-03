"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
#########################################################################
"""Сортировка пузырьком по убыванию"""

from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_upd(lst_obj):
    n = 1
    while n < len(lst_obj):
        lst_obj_copy = lst_obj[:]
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if lst_obj_copy == lst_obj:
            break
        n += 1
    return lst_obj


orig_lst = [randint(-100, 100) for _ in range(10)]

# замеры 10
print('bubble_sort: ',
      timeit(
          "bubble_sort(orig_lst[:])",
          globals=globals(),
          number=1000))
print('bubble_sort_upd: ',
      timeit(
          "bubble_sort_upd(orig_lst[:])",
          globals=globals(),
          number=1000))

orig_lst = [randint(-100, 100) for _ in range(100)]

# замеры 100
print('bubble_sort: ',
      timeit(
          "bubble_sort(orig_lst[:])",
          globals=globals(),
          number=1000))
print('bubble_sort_upd: ',
      timeit(
          "bubble_sort_upd(orig_lst[:])",
          globals=globals(),
          number=1000))

orig_lst = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print('bubble_sort: ',
      timeit(
          "bubble_sort(orig_lst[:])",
          globals=globals(),
          number=1000))
print('bubble_sort_upd: ',
      timeit(
          "bubble_sort_upd(orig_lst[:])",
          globals=globals(),
          number=1000))

"""
Сделал замеры времени обеих реализаций и как видно доработка помогла
лишь когда массив данных мал. С ростом массива увеличивается время обработки.

bubble_sort:  0.018193348000068
bubble_sort_upd:  0.013873515000000225
bubble_sort:  1.0779874239999572
bubble_sort_upd:  0.9901976060000379
bubble_sort:  105.27688180100006
bubble_sort_upd:  108.44745622599999
"""
