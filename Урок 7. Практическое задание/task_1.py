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

from random import randrange
from timeit import timeit


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubble_sort_improved(array):
    for i in range(len(array) - 1):
        swap = False
        for j in range(len(array) - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
        if not swap:
            return array
    return array


arr = [randrange(-100, 100) for x in range(20)]
print('Массив:', arr)
print(bubble_sort(arr))

print('Обычная - 10: ', timeit('bubble_sort([randrange(-100, 100) for x in range(10)])', globals=globals(), number=100))
print('Обычная - 100: ',
      timeit('bubble_sort([randrange(-100, 100) for x in range(100)])', globals=globals(), number=100))
print('Обычная - 1000: ',
      timeit('bubble_sort([randrange(-100, 100) for x in range(1000)])', globals=globals(), number=100))
print('Улучшенная - 10: ',
      timeit('bubble_sort_improved([randrange(-100, 100) for x in range(10)])', globals=globals(), number=100))
print('Улучшенная - 100: ',
      timeit('bubble_sort_improved([randrange(-100, 100) for x in range(100)])', globals=globals(), number=100))
print('Улучшенная - 1000: ',
      timeit('bubble_sort_improved([randrange(-100, 100) for x in range(1000)])', globals=globals(), number=100))

"""
Обычная - 10:  0.0017998998519033194
Обычная - 100:  0.10664150002412498
Обычная - 1000:  11.261642899829894
Улучшенная - 10:  0.001667700009420514
Улучшенная - 100:  0.09976530005224049
Улучшенная - 1000:  10.997549999970943

Улучшенная версия может выигрывать у обычной, если хвост массива изначально в значительной степени близок к 
отсортированному виду. В таком случае циклы прекращаются в момент, когда больше нечего переставлять.
"""
