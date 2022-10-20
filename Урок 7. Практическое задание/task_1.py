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


def bubble_sort_opposite(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list[:])
print(bubble_sort_opposite(orig_list[:]))

# Замеры 10
print(
    timeit(
        "bubble_sort_opposite(orig_list[:])",
        globals=globals(),
        number=1000))

"""
[43, 1, -57, -65, -2, -44, -85, -62, -80, -40]
[43, 1, -2, -40, -44, -57, -62, -65, -80, -85]
0.006273499922826886
"""


def bubble_sort_opposite_2(lst_obj):
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


print(orig_list[:])
print(bubble_sort_opposite_2(orig_list[:]))

# Замеры 10
print(
    timeit(
        "bubble_sort_opposite_2(orig_list[:])",
        globals=globals(),
        number=1000))

"""
[43, 1, -57, -65, -2, -44, -85, -62, -80, -40]
[43, 1, -2, -40, -44, -57, -62, -65, -80, -85]
0.006036699982360005
"""

# Замеры 1000

orig_list = [randint(-100, 100) for _ in range(1000)]

print(
    timeit(
        "bubble_sort_opposite(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "bubble_sort_opposite_2(orig_list[:])",
        globals=globals(),
        number=1000))

"""
Время выполнения функции без доработки - 50.11915779998526
Время выполнения функции с доработкой - 53.64278239989653
Такая доработка (завершение выполнения функции, если не было выполнено ни одной перестановки) 
эффективно скажется на времени выполнения функции только в случае, если массив уже отсортирован.
"""
