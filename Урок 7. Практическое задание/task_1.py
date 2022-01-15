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

"""
ВЫВОДЫ:
Сортировка пузырьком: 6.832959800027311
Сортировка пузырьком, модернизированная: 6.659955899929628

Сортировка пузырьком проходит все итерации независимо от того отсортирован массив или нет, соответственно если массив 
уже отсортирован, то сортировать его не надо) что и делает наша доработка. Поэтому чем больше перемешан массив, тем 
больше будут совпадать длительности выполнения. 
"""

from random import randint
from timeit import timeit


def buble_sort(array):

    for i in range(1, len(array) + 1):
        for j in range(len(array) - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def buble_sort_mod(array):
    was_changed = False

    for i in range(1, len(array) + 1):
        for j in range(len(array) - i):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                was_changed = True
        if not was_changed:
            return array

    return array


if __name__ == '__main__':
    original_array = [randint(-100, 99) for i in range(1000)]

    print('Сортировка пузырьком:')
    sorted_array = buble_sort(original_array.copy())
    print(timeit('buble_sort(array.copy())', setup='array = original_array.copy()', number=1000, globals=globals()))

    print(f'Исходный массив: {original_array}')
    print(f'Отсортированный массив: {sorted_array}')

    print()

    print('Сортировка пузырьком, модернизированная:')
    sorted_array = buble_sort_mod(original_array.copy())
    print(timeit('buble_sort_mod(array.copy())', setup='array = original_array.copy()', number=1000, globals=globals()))

    print(f'Исходный массив: {original_array}')
    print(f'Отсортированный массив: {sorted_array}')

    print()

    print('Сортировка пузырьком, модернизированная (лучший случай):')
    sorted_array = buble_sort_mod(original_array.copy())
    print(timeit('buble_sort_mod(array)', setup='array = sorted_array', number=10000, globals=globals()))

    print(f'Исходный массив: {original_array}')
    print(f'Отсортированный массив: {sorted_array}')
