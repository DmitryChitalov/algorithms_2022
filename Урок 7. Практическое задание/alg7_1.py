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


def bubble_sort_opt(lst):
    n = 1
    while n < len(lst):
        sort = True
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sort = False
        if sort == True:
            break

    return lst


orig_list = [randint(-100, 100) for _ in range(1000)]

print(timeit('bubble_sort(orig_list[:])', globals=globals(), number=100))
print(timeit('bubble_sort_opt(orig_list[:])', globals=globals(), number=100))

print(orig_list)
print(bubble_sort(orig_list))
print(bubble_sort_opt(orig_list))

# замеры времени приблизительно одинаковые, потому что, чтобы не совершалась ни одна замена в цикле, цикл должен быть отсортирован изначально
