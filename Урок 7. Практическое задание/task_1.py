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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_flag(lst_obj):
    n = 1
    cont = True
    while n < len(lst_obj) and cont:
        for i in range(len(lst_obj) - n):
            cont = False
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                cont = True
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list[:]))
print(bubble_sort_flag(orig_list[:]))

# замеры 10
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_flag(orig_list[:])",
        globals=globals(),
        number=1000))

# 0.010982200000000011
# 0.010848699999999989
# время одинаковое, для небольших массивов флаг нецелесообразен


orig_list = [randint(-100, 100) for _ in range(100)]
print(orig_list)
print(bubble_sort(orig_list[:]))
print(bubble_sort_flag(orig_list[:]))

# замеры 100
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_flag(orig_list[:])",
        globals=globals(),
        number=1000))

# 0.7188112
# 0.4879337
# время для функции с флагом меньше, но не очень значительно

orig_list = [randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(bubble_sort(orig_list[:]))
print(bubble_sort_flag(orig_list[:]))

# замеры 1000
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_flag(orig_list[:])",
        globals=globals(),
        number=1000))

# 51.1065022
# 44.0766894
# время для функции с флагом меньше, но не очень значительно
