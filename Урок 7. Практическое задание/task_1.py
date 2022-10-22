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

numbers = [randint(-100, 100) for _ in range(100)]
print(f'Исходный массив:\n{numbers}')

# Без оптимизации
def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]

    return array

# С оптимизацией
def bubble_sort_optimized(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False

        if flag == True:
            break
    return array

print('\nСортировка пузырьком (в обратном направлении, скорее камнем)')
time1 = timeit(f'bubble_sort({numbers[:]})',
              setup='from __main__ import bubble_sort',
              number=1000)
print(f'Сортированный массив:\n{bubble_sort(numbers[:])}')
print(f'Время 1000 сортировок: {time1} сек.')

print('\nСортировка пузырьком оптимизированная (в обратном направлении, скорее камнем)')
time2 = timeit(f'bubble_sort_optimized({numbers[:]})',
              setup='from __main__ import bubble_sort_optimized',
              number=1000)
print(f'Сортированный массив:\n{bubble_sort_optimized(numbers[:])}')
print(f'Время 1000 сортировок: {time2} сек.')

print(f"""ЗАКЛЮЧЕНИЕ\n
    Разница между обычной и оптимизированной составила {abs(time1 - time2)} сек.
    В связи с чем очевидно, что оптимизация нецелесообразна.""")