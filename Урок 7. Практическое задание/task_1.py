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


def new_bubble_sort(lst_obj):
    n = 1
    change_count = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                change_count += 1
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if change_count == 0:
            return lst_obj
        else:
            n += 1
    return lst_obj


not_sorted_list = [randint(-100, 100) for _ in range(100)]
sorted_list = [_ for _ in reversed(range(100))]

# замер недоработанного алгоритма на неотсортированном списке
print(timeit("bubble_sort(not_sorted_list[:])", globals=globals(), number=1000))

# замер недоработанного алгоритма на сортированном списке
print(timeit("bubble_sort(sorted_list[:])", globals=globals(), number=1000))

# замер доработанного алгоритма на неотсортированном списке
print(timeit("new_bubble_sort(not_sorted_list[:])", globals=globals(), number=1000))

# замер доработанного алгоритма на отсортированном списке
print(timeit("new_bubble_sort(sorted_list[:])", globals=globals(), number=1000))

# доработанный алгоритм показывает существенную разницу в скорости на отсортированном списке
# ввиду того, что проход по списку осуществляется один раз
