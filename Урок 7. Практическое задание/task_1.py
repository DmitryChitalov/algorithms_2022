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

""""
0.012767200000000006 - сортировка копии массива обычной функцией
0.0022728999999999944 - сортировка копии массива обновленной функцией
0.013953199999999999  - сортировка массива обычной функцией
0.014205999999999996 - сортировка отсортированного массива обычной функцией
0.0021872999999999754 - сортировка отсортированного массива обновленной функцией
Вывод: обновленный алгоритм более оптимален во всех случаях - и с неотсортированным массивом и с уже
отсортированным.
"""

from random import randint
from timeit import timeit


def bubble_sort_desc(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_desc_check(lst_obj):
    check = 0
    while check == 0:
        check = 1
        for i in range(len(lst_obj)-1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                check = 0
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort_desc(orig_list))
orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort_desc_check(orig_list))
print(timeit("bubble_sort_desc(orig_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_desc_check(orig_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_desc(orig_list)", globals=globals(), number=1000))
print(timeit("bubble_sort_desc(orig_list)", globals=globals(), number=1000))
print(timeit("bubble_sort_desc_check(orig_list)", globals=globals(), number=1000))
