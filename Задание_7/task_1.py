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
"""Сортировка пузырьком"""

from random import randint
from timeit import timeit

def bubble_sort():
    lst_obj = orig_list.copy()
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

def bubble_sort_modif():
    lst_obj = orig_list.copy()
    n = 1
    fl_change = True
    while (n < len(lst_obj)) and fl_change:
        fl_change = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                fl_change = True
        n += 1
    return lst_obj

orig_list = [randint(-100, 100) for _ in range(10)]
# orig_list = bubble_sort() # отсортирован
# orig_list = bubble_sort()[::-1]  # отсортирован в обратном порядке
print('Исходный:')
print(orig_list)
print('Сортировка:')
print(bubble_sort())
print('Сортировка доработанная:')
print(bubble_sort_modif())

number = 100000
print(
    'Сортировка, время:',
    timeit(
        "bubble_sort()",
        globals=globals(),
        number=number))

print(
    'Сортировка доработанная, время:',
    timeit(
        "bubble_sort_modif()",
        globals=globals(),
        number=number))

# для случайного распределения оба алгоритма работают примерно одинаково
# если массив уже отсортирован, модифицированный работает много быстрее
# если массив уже отсортирован в обратном порядке, скорость примерно одинаковая
