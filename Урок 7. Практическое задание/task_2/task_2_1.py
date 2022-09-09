"""
Задание 2. Массив размером 2m + 1, где m – натуральное число, - нечетное
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


def test_list(m):
    """
    Что бы получить массив длинной 10 элементов при размере массива 2m+1,
    m не может быть натуральным числом.
    """
    return [randint(1, 10) for _ in range(2 * m + 1)]


def gnome_sort(lst, index=1):
    size = len(lst)
    while index < size:
        if lst[index - 1] <= lst[index]:
            index += 1
        else:
            lst[index - 1], lst[index] = lst[index], lst[index - 1]
            if index > 1:
                index -= 1
    return lst


def median_search(sorted_lst):
    median = sorted_lst[len(sorted_lst) // 2]
    return f'{median} с индексом {len(sorted_lst) // 2}'


test_list_10 = test_list(5)
test_list_100 = test_list(50)
test_list_1000 = test_list(500)
print(
    f'Для массива {test_list_10}\nОтсортированный: {gnome_sort(test_list_10[:])}\nмедиана равна {median_search(gnome_sort(test_list_10[:]))}')

print(timeit("gnome_sort(test_list_10[:])", globals=globals(), number=100))
print(timeit("gnome_sort(test_list_100[:])", globals=globals(), number=100))
print(timeit("gnome_sort(test_list_1000[:])", globals=globals(), number=100))