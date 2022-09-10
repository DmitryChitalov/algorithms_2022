"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


mass_1 = 2 * 10 + 1
mass_2 = 2 * 100 + 1
mass_3 = 2 * 1000 + 1
lst1 = [randint(-900, 900) for _ in range(mass_1)]
lst2 = [randint(-900, 900) for _ in range(mass_2)]
lst3 = [randint(-900, 900) for _ in range(mass_3)]


def bubbleSort(array):
    ''' Метод Шелла '''
    swapped = False
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array


print(timeit('bubbleSort(lst1)[10]', globals=globals(), number=2))
print(timeit('bubbleSort(lst2)[100]', globals=globals(), number=2))
print(timeit('bubbleSort(lst3)[1000]', globals=globals(), number=2))