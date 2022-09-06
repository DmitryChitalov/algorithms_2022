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
        if flag is False:
            return lst
        for i in range(len(lst)-n):
            if lst[i] < lst[i+1]:
                val += 1
                lst[i], lst[i+1] = lst[i+1], lst[i]
        if val == 0:
            flag = False
        n += 1
    return lst


orig_list = [randint(-100, 100) for _ in range(10)]

# замеры 10
print(f'без доработки 10 элементов - {timeit("bubble_sort_rev(orig_list[:])", globals=globals(), number=1000)}')
print(f'c доработкой 10 элементов - {timeit("bubble_sort_rev_mod(orig_list[:])", globals=globals(), number=1000)}')

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(f'без доработки 100 элементов - {timeit("bubble_sort_rev(orig_list[:])", globals=globals(), number=1000)}')
print(f'c доработкой 100 элементов - {timeit("bubble_sort_rev_mod(orig_list[:])", globals=globals(), number=1000)}')
orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(f'без доработки 1000 элементов - {timeit("bubble_sort_rev(orig_list[:])", globals=globals(), number=1000)}')
print(f'c доработкой 1000 элементов - {timeit("bubble_sort_rev_mod(orig_list[:])", globals=globals(), number=1000)}')


"""
без доработки 10 элементов - 0.02641099999891594
c доработкой 10 элементов - 0.018621199997141957
без доработки 100 элементов - 1.8101424999767914
c доработкой 100 элементов - 1.7505328000406735
без доработки 1000 элементов - 191.47216010000557
c доработкой 1000 элементов - 208.09197820001282

ВЫВОДЫ: доработка даст выйгрыш по времени в том случае, когда массив отсортирован ранее "запланированного количества
итераций", либо когда на вход поступит сразу отсортированный массив.
"""