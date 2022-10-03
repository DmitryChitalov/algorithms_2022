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
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def bubble_sort_opt(lst):
    swap = True
    while swap:
        swap = False
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap = True


my_list = [randint(-100, 100) for i in range(1000)]


print(
    timeit(
        "bubble_sort(my_list[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "bubble_sort_opt(my_list[:])",
        globals=globals(),
        number=100))


"""
22.495833802
21.965128442

Как показывают замеры, удалось добиться только небольшого улучшения по времени.
Соответственно смысл в оптимизации есть только в том случае, если массив хотя бы частично отсортирован.
"""
