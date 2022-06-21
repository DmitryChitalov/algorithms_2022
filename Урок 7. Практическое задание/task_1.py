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
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_2(lst_obj):
    n = 1
    a = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                a += 1
        if a == 0:
            break
        n += 1
    return lst_obj


# замеры 10
orig_list = [randint(-100, 100) for _ in range(20)]
print(f'Исходный массив на 10 элементов: \n{orig_list}')
print(f'Отсортированный массив: \n{bubble_sort(orig_list[:])}')
print(f'Отсортированный массив_2: \n{bubble_sort_2(orig_list[:])}')
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_2(orig_list[:])", globals=globals(), number=1000))
print('-' * 50)
# замеры 100
orig_list_2 = [randint(-100, 100) for _ in range(100)]
print(f'Исходный массив на 100 элементов: \n{orig_list_2}')
print(f'Отсортированный массив: \n{bubble_sort(orig_list_2[:])}')
print(f'Отсортированный массив_2: \n{bubble_sort_2(orig_list_2[:])}')
print(timeit("bubble_sort(orig_list_2[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_2(orig_list_2[:])", globals=globals(), number=1000))
print('-' * 50)
# замеры 1000
orig_list_3 = [randint(-100, 100) for _ in range(1000)]
print(f'Исходный массив на 1000 элементов: \n{orig_list_3}')
print(f'Отсортированный массив: \n{bubble_sort(orig_list_3[:])}')
print(f'Отсортированный массив_2: \n{bubble_sort_2(orig_list_3[:])}')
print(timeit("bubble_sort(orig_list_3[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_2(orig_list_3[:])", globals=globals(), number=1000))

'''
Вывод: разница во времени при обычной сортировке и сортировке с доработкой небольшая. 
Сортировка с доработкой работает быстрее, если массив мал. 
При больших массивах (более 10 элементов) лучше использовать сортировку без доработки, это будет быстрее.'''
