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

def bubble_sort_old(lst):
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
        is_sorted = False
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                is_sorted = False
        if is_sorted == True:
            break

        n += 1
    return lst

my_lst = [randint(-100, 100) for _ in range(10)]
sorted_lst = bubble_sort_old(my_lst[:])

print(bubble_sort_old(my_lst[:]))
print(bubble_sort_old(sorted_lst[:]))
print(bubble_sort_mod(my_lst[:]))
print(bubble_sort_mod(sorted_lst[:]))

print(timeit(
        "bubble_sort_old(my_lst[:])", globals=globals(), number=1000))
print(timeit(
        "bubble_sort_old(sorted_lst[:])", globals=globals(), number=1000))
print(timeit(
        "bubble_sort_mod(my_lst[:])", globals=globals(), number=1000))
print(timeit(
        "bubble_sort_mod(sorted_lst[:])", globals=globals(), number=1000))


# стандартная сортировка пузырьком
# несортированный список: 0.007058624999999999'
# сортированный список: 0.004455500000000001'

# доработанная сортировка пузырьком:
# несортированный список: 0.007153208000000001'
# сортированный список: 0.004314333999999996'

# такая реализация может быть эффективной при обработке большого числа
# небольших списков, среди которых могут быть отсортированные,
# но в основном как будто и разницы нет


