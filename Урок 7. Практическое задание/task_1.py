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


def bubble_sort_rev(lst_obj):  # Cортировка по убыванию методом "пузырька"
    for n in range(1, len(lst_obj)):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:  # по убыванию
                lst_obj[i], lst_obj[i + 1], n = lst_obj[i + 1], lst_obj[i], 0
    return lst_obj


def bubble_sort_rev_opt(lst_obj):  # Cортировка по убыванию методом "пузырька" с доработкой
    for n in range(1, len(lst_obj)):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1], n = lst_obj[i + 1], lst_obj[i], 0
        if n:  # за проход по списку не совершается ни одной сортировки
            break  # выходим
    return lst_obj


number = 1000
x = [randint(-100, 100) for _ in range(number)]
# x = [7, 8, 2, 3, 7, 0, 5, 4, 3, 0, 1]
print(f'{bubble_sort_rev_opt(x[:])}\n{x}')
print(f'{bubble_sort_rev(x[:])}\n{x}')

print(timeit("bubble_sort_rev(x[:])", globals=globals(), number=10))
print(timeit("bubble_sort_rev_opt(x[:])", globals=globals(), number=10))

"""
Замеры показали, что на небольших массивах доработанный алгоритм дает небольшую стабильную прибавку к скорости.
С увуличением объема данных квадратичная асимптотическая сложность обоих алгоритмов нивелирует разницу
"""