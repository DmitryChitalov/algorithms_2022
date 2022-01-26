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


def bubble_sort(my_lst):
    n = 1
    while n < len(my_lst):
        for i in range(len(my_lst) - n):
            if my_lst[i] < my_lst[i + 1]:
                my_lst[i], my_lst[i + 1] = my_lst[i + 1], my_lst[i]
        n += 1
    return my_lst


def bubble_sort_flag(my_lst):
    flag = True
    for j in range(len(my_lst) - 1):
        if not flag:
            return my_lst
        flag = False
        for i in range(len(my_lst) - 1 - j):
            if my_lst[i] < my_lst[i + 1]:
                my_lst[i], my_lst[i + 1] = my_lst[i + 1], my_lst[i]
                flag = True
    return my_lst


my_list = [randint(-100, 100) for x in range(1000)]
print('bubble_sort ',
      timeit('bubble_sort(my_list[:])', globals=globals(), number=100), ' seconds ')
my_list = [randint(-100, 100) for x in range(1000)]
print('bubble_sort_flag ',
      timeit('bubble_sort_flag(my_list[:])', globals=globals(), number=100), ' seconds ')

my_list_sorted = bubble_sort(my_list)

print('bubble_sort for sorted list ',
      timeit('bubble_sort(my_list_sorted[:])', globals=globals(), number=100), ' seconds ')
print('bubble_sort_flag for sorted list ',
      timeit('bubble_sort_flag(my_list_sorted[:])', globals=globals(), number=100), ' seconds ')

# В качестве оптимизации выбрано добавление флага,показывающего факт перестановки элементов во время каждой итерации.
# Соответтсвенно, если во время итерации флаг не был выставлен, то список уже отвосртирован и можно прекращать сортировку


# Данный подход достигает максимальной эффективности когда массив близок к состоянию отсортированного,
# тк в этом случае алгоритм с флагом завершает свою работу быстрее чем обычный, который в любом случае проводит
# полный перебор
