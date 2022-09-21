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


def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                swap(i, j)

    return arr


def bubble_sort_optimize(arr):
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


print(f'Before: {array}', f'After reverse_bubble_sort: {bubble_sort(array[:])}',
      f'After bubble_sort_optimize: {bubble_sort_optimize(array[:])}',
      list(sorted(array[:], reverse=True)), sep='\n')
print(len(array), len(bubble_sort(array[:])), len(bubble_sort_optimize(array[:])))
print('bubble_sort:', timeit('bubble_sort(array[:])', globals=globals(), number=100))
print('bubble_sort_optimize', timeit('bubble_sort_optimize(array[:])', globals=globals(), number=100))

"""
bubble_sort: 8.473341900040396
bubble_sort_optimize 6.142269900010433
Оптимизированный вариант оказался лучше, чем простая пузырьковая сортировка 
c использованием двух циклов for in
"""