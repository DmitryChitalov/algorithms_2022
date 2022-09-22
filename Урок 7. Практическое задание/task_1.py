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

from random import randint
from timeit import timeit


def bubble_sort(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def bubble_sort_mod(lst):
    n = 1
    while n < len(lst):
        flag = True
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = False
        if flag == True:
            break
        n += 1
    return lst


# 10 элементов
orig_list = [randint(-100, 100) for _ in range(10)]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))      # 0.009113800013437867
print(timeit("bubble_sort_mod(orig_list[:])", globals=globals(), number=1000))  # 0.00895920000039041

# 100 элементов
orig_list = [randint(-100, 100) for _ in range(100)]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))      # 0.5984105000970885
print(timeit("bubble_sort_mod(orig_list[:])", globals=globals(), number=1000))  # 0.5968640999635682

# 1000 элементов
orig_list = [randint(-100, 100) for _ in range(1000)]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))      # 70.72196399990935
print(timeit("bubble_sort_mod(orig_list[:])", globals=globals(), number=1000))  # 71.28127170004882

# заранее отсортированный
orig_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))      # 0.006045499932952225
print(timeit("bubble_sort_mod(orig_list[:])", globals=globals(), number=1000))  # 0.0011554000666365027

"""
Модификация функции поможет только в том случае, когда массив заранее отсортирован
"""
