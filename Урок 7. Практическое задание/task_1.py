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

import random
from timeit import timeit

my_array = [random.randrange(-100, 100) for i in range(100)]
print(f'исходный массив: {my_array}')


def bubble_sort(some_array):
    for j in range(len(some_array) - 1):
        for i in range(len(some_array) - 1 - j):
            if some_array[i] < some_array[i+1]:
                some_array[i], some_array[i + 1] = some_array[i+1], some_array[i]
    return some_array


print('Не оптимизировано')
print(bubble_sort(my_array[:]))
print(timeit('bubble_sort(my_array[:])', globals=globals(), number=10000))

print(f'исходный массив: {my_array}')


def bubble_sort2(some_array):
    for j in range(len(some_array) - 1):
        sort_counter = 0
        for i in range(len(some_array) - j - 1):
            if some_array[i] < some_array[i+1]:
                some_array[i], some_array[i + 1] = some_array[i+1], some_array[i]
                sort_counter += 1
        if sort_counter == 0:
            return some_array
    return some_array


print('Оптимизировано')
print(bubble_sort2(my_array[:]))
print(timeit('bubble_sort2(my_array[:])', globals=globals(), number=10000))

'''
Оптимизация замедлила работу алгоритма из-за дополнительных проверок. 
Она бы помогла, если бы числа в исходном массиве были упорядочены.
'''