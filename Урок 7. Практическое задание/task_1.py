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
import timeit
from random import randint


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_reverse(lst_obj):
    n = 0
    while n < len(lst_obj):
        is_not_sorted = True
        for i in range(1, len(lst_obj) - n):
            i *= -1

            if lst_obj[i] > lst_obj[i - 1]:
                is_not_sorted = False
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
        if is_not_sorted:
            return lst_obj
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]

print(timeit.timeit(stmt='bubble_sort(orig_list[:])', globals=globals(), number=10000))
print(timeit.timeit(stmt='bubble_sort_reverse(orig_list[:])', globals=globals(), number=10000))
