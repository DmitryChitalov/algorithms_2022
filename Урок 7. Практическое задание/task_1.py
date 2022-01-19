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


def bubble(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


a = [randint(-100, 100)for i in range(1000)]
print(timeit('bubble(a[:])', globals=globals(), number=100))
# print(a)
# b = a.copy()


def best_bubble(lst):
    temp_list = lst.copy()
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if lst == temp_list:
            break
    return lst


def best_best_bubble(lst):
    flag = True
    while flag:
        flag = False
        for j in range(len(lst)-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                flag = True
    return lst


# print(bubble(a[:]), '\n', best_bubble(a[:]), '\n', bubble(a[:]) == best_bubble(a[:]) )

print(timeit('best_bubble(a[:])', globals=globals(), number=100))
# print(timeit('best_best_bubble(a[:])', globals=globals(), number=100))


def bubble_sort_unoptimized(some_lst):
    """Выполняет самую простую сортировку пузырьком"""
    for i in range(len(some_lst)):
        for j in range(len(some_lst) - 1):
            if some_lst[j] < some_lst[j + 1]:
                some_lst[j], some_lst[j + 1] = some_lst[j + 1], some_lst[j]
    return some_lst


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


orig_list = [randint(-100, 100) for i in range(1000)]

print(
    timeit(
        "bubble_sort_unoptimized(orig_list[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "bubble_sort_optimized1(orig_list[:])",
        globals=globals(),
        number=100))


'''
Особой разницы в скорости выполнения задания нет, а разница в скорости в предложенном варианте решения не объективны,
так как в качестве аргумента используется сам массив, а не его копия, поэтому скорость настолько высокая в функции
оптимизированной функции 
'''
