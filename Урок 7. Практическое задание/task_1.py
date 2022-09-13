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

from timeit import timeit
from random import randint

N = 100
lst_ = [randint(-100, 100) for _ in range(N)]


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


def bubble_sort_upd(lst):
    is_end = True
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                is_end = False
        if is_end:
            break

    return lst


print(f'Неотсортированный массив:\n {lst_}')
print(f'Отсортированный массив bubble sort:\n {bubble_sort(lst_[:])}')
print(f'Отсортированный массив bubble sort upd:\n {bubble_sort_upd(lst_[:])}')

print(f'Замер для bubble sort: {timeit("bubble_sort(lst_[:])", globals=globals(), number=10000)}')
print(f'Замер для bubble sort upd {timeit("bubble_sort_upd(lst_[:])", globals=globals(), number=10000)}')

'''
Замер для bubble sort: 8.517657599877566
Замер для bubble sort upd 8.50762869999744
Никакого значения доработка не имеет. Время остается тем же
'''
