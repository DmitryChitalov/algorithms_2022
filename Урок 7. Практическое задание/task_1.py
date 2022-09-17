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
import random
from timeit import timeit

mass = [random.randint(-100, 100) for i in range(100)]


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


'''Сделал чуть по другому, но получилось дольше по времени'''


def my_bubble_sort(my_list):
    for run in range(len(my_list) - 1):
        flag = False
        for i in range(len(my_list) - 1):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                flag = True
        if not flag:
            break
    return my_list


'''В моём случае доработка помогла, но совсем немного, при работе с большими
массивами, время равно обычной сортировке без доработки'''


def new_bubble_sort(my_list):
    for i in reversed(range(len(my_list) + 1)):
        flag = True
        for j in range(i - 1):
            if my_list[j] < my_list[j + 1]:
                tmp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = tmp
                flag = False
        if flag:
            break
    return my_list


print(timeit("bubble_sort(mass[:])", globals=globals(), number=1000))
print()
print(timeit("my_bubble_sort(mass[:])", globals=globals(), number=1000))
print()
print(timeit("new_bubble_sort(mass[:])", globals=globals(), number=1000))
print()
print(my_bubble_sort(mass))
print()
print(bubble_sort(mass))
print()
print(new_bubble_sort(mass))
