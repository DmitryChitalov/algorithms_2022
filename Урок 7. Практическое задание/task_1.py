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


def bubble_sort_rev(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst)-n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n += 1
    return lst


def bubble_sort_rev_mod(lst):
    n = 1
    flag = True
    while n < len(lst):
        val = 0
        if not flag:
            return lst
        for i in range(len(lst)-n):
            if lst[i] < lst[i+1]:
                val += 1
                lst[i], lst[i+1] = lst[i+1], lst[i]
        if val == 0:
            return lst
        n += 1
    return lst


# 10
orig_list = [randint(-100, 100) for _ in range(10)]
print(f'10 - {timeit("bubble_sort_rev(orig_list[:])", globals=globals(), number=1000)}')
print(f'10 (мод) - {timeit("bubble_sort_rev_mod(orig_list[:])", globals=globals(), number=1000)}')

# 100
orig_list = [randint(-100, 100) for _ in range(100)]
print(f'100 - {timeit("bubble_sort_rev(orig_list[:])", globals=globals(), number=1000)}')
print(f'100 (мод) - {timeit("bubble_sort_rev_mod(orig_list[:])", globals=globals(), number=1000)}')

# 1000
orig_list = [randint(-100, 100) for _ in range(1000)]
print(f'1000 - {timeit("bubble_sort_rev(orig_list[:])", globals=globals(), number=1000)}')
print(f'1000 (мод) - {timeit("bubble_sort_rev_mod(orig_list[:])", globals=globals(), number=1000)}')


"""
10 - 0.009678299999999994
10 (мод) - 0.010625400000000007
100 - 0.8136931
100 (мод) - 0.8829319999999999
1000 - 86.915843
1000 (мод) - 94.60045509999999

Вывод:
Если бы на вход нашей функции поступал отсортированный массив, то был бы смысл от "оптимизации",
а так лишние проверки лишь замедляют процесс. 
"""
