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

range_numbers = [randint(-100, 100) for _ in range(0, 10)]


def sorting(numbers: list):
    for x in range(1, len(numbers)):
        for i in range(len(numbers) - x):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers


def sorting_break(numbers: list):
    for x in range(1, len(numbers)):
        replaced = False

        for i in range(len(numbers) - x):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                replaced = True

        if replaced is False:
            break
    return numbers


print(sorting(range_numbers))
print(sorting_break(range_numbers))

"""
Сортировка по убыванию
[93, 47, 7, 3, -11, -20, -24, -35, -38, -65]
[93, 47, 7, 3, -11, -20, -24, -35, -38, -65]
"""

print(
    timeit(
        "sorting(range_numbers)",
        setup='from __main__ import range_numbers, sorting',
        number=1000))
print(
    timeit(
        "sorting(range_numbers)",
        setup='from __main__ import range_numbers, sorting',
        number=50000))
print(
    timeit(
        "sorting(range_numbers)",
        setup='from __main__ import range_numbers, sorting',
        number=200000))
"""
sorting
0.004628500000000001
0.2298332
0.8820570999999999
"""

print(
    timeit(
        "sorting_break(range_numbers)",
        setup='from __main__ import range_numbers, sorting_break',
        number=1000))
print(
    timeit(
        "sorting_break(range_numbers)",
        setup='from __main__ import range_numbers, sorting_break',
        number=50000))
print(
    timeit(
        "sorting_break(range_numbers)",
        setup='from __main__ import range_numbers, sorting_break',
        number=200000))
"""
sorting_break
0.0010262000000000882
0.048039299999999896
0.19311279999999997
"""

"""
    "...дайте ответ помогла ли доработка..." - Да.
    "и в каких случаях она будет эффективной" - Всегда. 
    Потому что пропадают лишние, не нужные, проходы. 
"""
