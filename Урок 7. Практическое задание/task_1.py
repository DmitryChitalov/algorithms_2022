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


def get_arr():
    return [randint(-100, 100) for x in range(50)]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_mod(arr):
    checker = True
    while checker:
        checker = False
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                checker = True
    return arr


any_arr = get_arr()

print(any_arr)

# стандартное решение
print(
    timeit(
        "bubble_sort(any_arr)",
        globals=globals(),
        number=10000))

# измененное
print(
    timeit(
        "bubble_sort_mod(any_arr)",
        globals=globals(),
        number=10000))

"""
Результат:
1.2394344999920577
0.024658699985593557

Доработка будет эффективна только если массив, уже отсротирован.
"""
