from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    for i in range(len(lst_obj)):
        for j in range(len(lst_obj) - 1):
            if lst_obj[j] < lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
    return lst_obj


def bubble_sort_optimized1(some_lst):
    """Сортировка пузырьком с использованием маркера"""
    flag = True
    while flag:
        flag = False
        for i in range(len(some_lst) - 1):
            if some_lst[i] < some_lst[i + 1]:
                some_lst[i], some_lst[i + 1] = some_lst[i + 1], some_lst[i]
                flag = True
    return some_lst


orig_list = [randint(-100, 100) for _ in range(10)]
print(f'Original list: {orig_list}')
print("Sorted list:", bubble_sort_optimized1(orig_list))

# замеры 10
print(
    "Сортировка пузырьком для 10 элементов: ",
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=100))

print(
    "Сортировка пузырьком оптимизированная для 10 элементов: ",
    timeit(
        "bubble_sort_optimized1(orig_list[:])",
        globals=globals(),
        number=100))

# замеры 100
orig_list = [randint(-100, 100) for _ in range(100)]
print(
    "Сортировка пузырьком для 100 элементов: ",
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=100))

print(
    "Сортировка пузырьком оптимизированная для 100 элементов: ",
    timeit(
        "bubble_sort_optimized1(orig_list[:])",
        globals=globals(),
        number=100))

# замеры 1000
orig_list_1000 = [randint(-100, 100) for _ in range(1000)]
print(
    "Сортировка пузырьком для 1000 элементов: ",
    timeit(
        "bubble_sort(orig_list_1000[:])",
        globals=globals(),
        number=100))

print(
    "Сортировка пузырьком оптимизированная для 1000 элементов: ",
    timeit(
        "bubble_sort_optimized1(orig_list_1000[:])",
        globals=globals(),
        number=100))

# замеры 5000
orig_list_5000 = [randint(-100, 100) for _ in range(5000)]
print(
    "Сортировка пузырьком для 5000 элементов: ",
    timeit(
        "bubble_sort(orig_list_5000[:])",
        globals=globals(),
        number=100))

print(
    "Сортировка пузырьком оптимизированная для 5000 элементов: ",
    timeit(
        "bubble_sort_optimized1(orig_list_5000[:])",
        globals=globals(),
        number=100))

'''
На маленьких размеров массива оптимизированная функция имеет большее преимущество по скорости над обычной.
Но чем больше массив, тем разница в скорости меньше.

Распечатала массив из 10 элементов:
Original list: [-23, -25, 56, -4, -51, 35, -41, 56, -85, 91]
Sorted list: [91, 56, 56, 35, -4, -23, -25, -41, -51, -85]

Сортировка пузырьком для 10 элементов:  0.001522223000000003
Сортировка пузырьком оптимизированная для 10 элементов:  0.00017065500000000566

Сортировка пузырьком для 100 элементов:  0.16445489800000002
Сортировка пузырьком оптимизированная для 100 элементов:  0.145939239

Сортировка пузырьком для 1000 элементов:  18.331867271
Сортировка пузырьком оптимизированная для 1000 элементов:  17.467148513999998

Сортировка пузырьком для 5000 элементов:  478.751222994
Сортировка пузырьком оптимизированная для 5000 элементов:  476.03540759599997
'''
