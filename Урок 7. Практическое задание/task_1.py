"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
from timeit import timeit
from random import randint


def bubble_sort(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def bubble_sort_optimized(lst):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = True
    return lst


lst_obj = [randint(-100, 100) for _ in range(20)]

print(lst_obj)
print(bubble_sort(lst_obj[:]))

print('*' * 100)

print(lst_obj)
print(bubble_sort_optimized(lst_obj[:]))


print(f'{timeit("bubble_sort(lst_obj[:])", globals=globals(), number=1000)} - Не оптимизированная')
print(f'{timeit("bubble_sort_optimized(lst_obj[:])", globals=globals(), number=1000)} - оптимизированная')

"""
Оптимизация ничего не дает при рандомной генерации списка,
так как шансы получить сразу отсортированный список равны 0
"""