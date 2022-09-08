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

###############################################################################
from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_mod(lst_obj):
    has_swapped = True
    while (has_swapped):
        has_swapped = False
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                has_swapped = True
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))      # 0.017054299998562783
print(timeit("bubble_sort_mod(orig_list[:])", globals=globals(), number=1000))  # 0.00958600000012666

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))      # 1.8577923999982886
print(timeit("bubble_sort_mod(orig_list[:])", globals=globals(), number=1000))  # 1.6617155999992974

""" Доработка помогла ускорить процесс сортировки, применима для списка из многих элементов"""
