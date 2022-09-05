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


def bubble_sort_1(array):
    for i in range(0, len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] < array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


def bubble_sort_2(array):
    has_swap = True
    count = 0
    while has_swap:
        has_swap = False
        for i in range(len(array) - count - 1):
            if array[i] < array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                has_swap = True
        count += 1

    return array


array = [randint(-100, 100) for i in range(10)]

print(timeit('bubble_sort_1(array[:])', globals=globals(), number=1000)) #  0.0059148
print(timeit('bubble_sort_2(array[:])', globals=globals(), number=1000)) #  0.004548399999999998


array = [randint(-100, 100) for i in range(100)]

print(timeit('bubble_sort_1(array[:])', globals=globals(), number=1000)) #   0.5229648
print(timeit('bubble_sort_2(array[:])', globals=globals(), number=1000)) #   0.4844712

array = [randint(-100, 100) for i in range(1000)]

print(timeit('bubble_sort_1(array[:])', globals=globals(), number=1000)) #  65.7776241
print(timeit('bubble_sort_2(array[:])', globals=globals(), number=1000)) #  69.02069709999999

# дороботка будет эффективной для небольших массивов
