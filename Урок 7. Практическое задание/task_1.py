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


"""Сортировка пузырьком"""

from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_opt(lst_obj):
    flag = True

    while flag:
        flag = False
        for i in range(len(lst_obj)-1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = True
    return lst_obj

orig_list = [randint(-100, 100) for _ in range(10)]

# замеры 10

print(orig_list,bubble_sort(orig_list[:]),
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=100),sep='\n')
print(
    timeit(
        "bubble_sort_opt(orig_list[:])",
        globals=globals(),
        number=100))

orig_list = [randint(-100, 100) for _ in range(100)]


# замеры 100

print(orig_list,bubble_sort(orig_list[:]),
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=100) ,sep='\n')

print(
    timeit(
        "bubble_sort_opt(orig_list[:])",
        globals=globals(),
        number=100))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000

print(orig_list,bubble_sort(orig_list[:]),
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=100),sep='\n' )

print(
    timeit(
        "bubble_sort_opt(orig_list[:])",
        globals=globals(),
        number=100))


"""
По результатам замеров оптимизиваронная функция получилась медленнее, чем не оптимизированная. 
Оптимизированная функция уменьшает количество дейстий на последний проход с помощью флага, но при больших массивах 
работает медленее. Почему так получилось, я не разобрался.

"""



