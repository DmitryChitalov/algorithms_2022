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


orig_list = [randint(-100, 100) for _ in range(100)]


def bubble_sort(lst_obj):
    n = 0
    while n < len(lst_obj) - 1:
        for i in range(len(lst_obj) - 1, n, -1):
            if lst_obj[i] > lst_obj[i - 1]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
        n += 1
    return lst_obj
print('рандомный список: ', orig_list)
print('простая сортировка: ', bubble_sort(orig_list[:]))
print('время на простую сортировку: ', timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))


def bubble_sort_optimized(lst_obj):
    n = 0
    my_optimized = True
    while my_optimized:
        my_optimized = False
        for i in range(len(lst_obj) - 1, n, -1):
            if lst_obj[i] > lst_obj[i - 1]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
                my_optimized = True
        n += 1
    return lst_obj

print('сортировка после оптимизации: ', bubble_sort_optimized(orig_list[:]))
print('время на сортировку после оптимизации: ', timeit("bubble_sort_optimized(orig_list[:])", globals=globals(), number=1000))

# bubble_sort_optimized выполняется быстрее. При проходе по списку нет сортировки.
# bubble_sort выполняется медленнее. Простой алгоритм сортировки по убыванию. "Всплывает" самый маленький.