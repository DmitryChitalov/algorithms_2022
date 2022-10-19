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

from timeit import timeit
from random import randint


def sort_small_bubble(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]

        n += 1
    return lst_obj


def sort_small_bubble_v2(lst_obj):
    n = 1
    while n < len(lst_obj):
        count = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                count += 1
        if count == 0:
            break
        n += 1
    return lst_obj


orig_list_100 = [randint(-100, 100) for _ in range(11)]

print(f"Original_massive >>> {orig_list_100}")
print(
    f'Sorted_massive >>> {sort_small_bubble(orig_list_100[:])}\n'
    f'Time >>> '
    f'{timeit("sort_small_bubble(orig_list_100[:])", globals=globals(), number=10000)}')

"""V.2"""

print(f"Original_massive_v2 >>> {orig_list_100}")
print(
    f'Sorted_massive_v2 >>> {sort_small_bubble_v2(orig_list_100[:])}\n'
    f'Time >>> '
    f'{timeit("sort_small_bubble_v2(orig_list_100[:])", globals=globals(), number=10000)}')

# Original_massive >>> [54, 16, -30, 68, 19, -69, -24, 93, 1, 57, -72]
# Sorted_massive >>> [93, 68, 57, 54, 19, 16, 1, -24, -30, -69, -72]
# Time >>> 0.190850093
# Original_massive_v2 >>> [54, 16, -30, 68, 19, -69, -24, 93, 1, 57, -72]
# Sorted_massive_v2 >>> [93, 68, 57, 54, 19, 16, 1, -24, -30, -69, -72]
# Time >>> 0.15376810300000002

"""Здесь интересные наблюдения. Всё зависит от случайной генерации. Чем больше
упорядоченных элементов в массиве и сам массив не велик (как в моём примере),
тем эффективней способ с доп.счетчиком для сортировок и времязатраты меньше. 
Чем же беспорядочней и крупнее массив, тем данный счетчик становится обузой,
увеличивающий время работы скрипта по сравнению с классикой"""
