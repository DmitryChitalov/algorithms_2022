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


def bubble_sort_reverse(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(0, len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_modification(lst_obj):
    n = 1
    action = False
    while n < len(lst_obj):
        for i in range(0, len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                action = True
        if not action:
            return lst_obj
        n += 1
    return lst_obj


lst = [randint(-100, 100) for _ in range(1, 10)]

print(f'Пузырки на убывание (Исходный массив)       : {lst}')
print(f'Пузырки на убывание (Отсортированный массив): {bubble_sort_reverse(lst[:])}')
print('-------------------------------------------------------------------------------')
print(f'Пузырки на убывание доработанный (Исходный массив)       : {lst}')
print(f'Пузырки на убывание доработанный (Отсортированный массив): {bubble_sort_modification(lst[:])}')
print('-------------------------------------------------------------------------------')
print('Время до модификации: ', end='')
print(timeit('bubble_sort_reverse(lst[:])', globals=globals(), number=1000))
print('Время после модификации: ', end='')
print(timeit('bubble_sort_modification(lst[:])', globals=globals(), number=1000))


'''
Доработка сортировки методом "пузырька" через завершение в случае если за один проход небыло сортировки эффективней, 
только если необходима незначительная сортировка.  
'''