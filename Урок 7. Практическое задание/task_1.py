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


def bubble_sort(rand_list):
    for i in range(len(rand_list)):
        for j in range(len(rand_list) - 1):
            if rand_list[j] < rand_list[j + 1]:
                rand_list[j], rand_list[j + 1] = rand_list[j + 1], rand_list[j]
    return rand_list


def bubble_sort_with_flag(rand_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(rand_list) - 1):
            if rand_list[i] > rand_list[i + 1]:
                rand_list[i], rand_list[i + 1] = rand_list[i + 1], rand_list[i]
                swapped = True
    return rand_list


rand_list = [randint(-100, 100) for i in range(100)]
print(rand_list)
print(bubble_sort(rand_list[:]))
print('-' * 50)
print(
    timeit(
        "bubble_sort(rand_list[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "bubble_sort_with_flag(rand_list[:])",
        globals=globals(),
        number=100))
'''
При длинне массива 100:
0.322345900000073
0.29511799989268184
При длинне массива 1000:
15.119207800016738
14.627836699946783
Согласно полученным данным, оптимизация имеет смысл
'''
