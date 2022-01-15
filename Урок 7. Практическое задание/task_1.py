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

array = [randint(-100, 100) for i in range(1000)]


def reverse_bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                swap(i, j)

    return arr


def reverse_bubble_sort_optimize(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, len(arr) - x):
            if arr[i - 1] < arr[i]:
                swap(i - 1, i)
                swapped = True

    return arr


print(f'Before: {array}', f'After reverse_bubble_sort: {reverse_bubble_sort(array[:])}',
      f'After reverse_bubble_sort_optimize: {reverse_bubble_sort_optimize(array[:])}',
      list(sorted(array[:], reverse=True)), sep='\n')
print(len(array), len(reverse_bubble_sort(array[:])), len(reverse_bubble_sort_optimize(array[:])))
print('reverse_bubble_sort:', timeit('reverse_bubble_sort(array[:])', globals=globals(), number=100))
print('reverse_bubble_sort_optimize', timeit('reverse_bubble_sort_optimize(array[:])', globals=globals(), number=100))
print("""Разница между вариантами пузырьковой сортировки достаточно значительная.
Оптимизированный вариант оказался лучше, чем простая пузырьковая сортировка c использованием двух циклов for in,
Это связано с тем, что двойной for in проходит по массиву даже по упорядоченным элементам - лишнее действие.
Оптимизированный вариант избавляет нас от этого и причём неплохо
""")
