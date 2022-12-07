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


def bubble_sort_1(lst_obj):
    n = 1
    count = len(lst_obj)
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                count -= 1
        if count == len(lst_obj):
            return f'Этот список\n{lst_obj}\nИтак отсортирован!'
        n += 1
    return lst_obj

list_1 = [randint(-100, 100) for i in range(10)]
print(list_1)
lst_2 = sorted(list_1[:], reverse=True)
print(bubble_sort(list_1[:]))
print(timeit('bubble_sort(lst_2[:])', globals=globals(), number=1000))
print(bubble_sort_1(lst_2[:]))
print(timeit('bubble_sort_1(lst_2[:])', globals=globals(), number=1000))

# Судя по результатам, доработка помогла!
