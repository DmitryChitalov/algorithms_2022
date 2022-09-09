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

test_list = [randint(-100, 100) for _ in range(200)]


def bubble_sort(lst):
    """
    Пузырьковая сортировка.
    """
    for _ in range(len(lst)):
        for index in range(1, len(lst)):
            if lst[index] > lst[index - 1]:
                lst[index], lst[index - 1] = lst[index - 1], lst[index]

    return lst


print(test_list)
print(bubble_sort(test_list[:]))
print(timeit("bubble_sort(test_list[:])", globals=globals(), number=1000))


def bubble_sort_upgrade_one(lst):
    """
      Пузырьковая сортировка.
      При каждой итерации уменьшаем область сортировки на 1
      Прирост скорости 60%
      """
    for i in range(len(lst) - 1):
        for index in range(1, len(lst) - i):
            if lst[index] > lst[index - 1]:
                lst[index], lst[index - 1] = lst[index - 1], lst[index]

    return lst


print(bubble_sort_upgrade_one(test_list[:]))
print(timeit("bubble_sort_upgrade_one(test_list[:])", globals=globals(), number=1000))


def bubble_sort_upgrade_two(lst, already_sorted=0):
    """
    Сортировка пузырьком.
    Если за первый проход не было сделано ни одной перестановки, массив считается отсортированным.
    Для большинства случаев(в которых массив не отсортирован) время работы функции незначительно увеличивается.
    """
    for i in range(len(lst) - 1):
        if i > 0 and already_sorted == 0:
            return lst
        for index in range(1, len(lst) - i):
            if lst[index] > lst[index - 1]:
                lst[index], lst[index - 1] = lst[index - 1], lst[index]
                already_sorted += 1

    return lst


print(bubble_sort_upgrade_two(test_list[:]))
print(timeit("bubble_sort_upgrade_two(test_list[:])", globals=globals(), number=1000))

