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
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(len(rand_list) - 1):
            if rand_list[i] > rand_list[i + 1]:
                rand_list[i], rand_list[i + 1] = rand_list[i + 1], rand_list[i]
                has_swapped = True
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
0.06921233300090535
0.04856604200176662

При длинне массива 1000:
6.181994541999302
6.115758874999301

Как видно по замерам оптимизация имеет смысл, но при больших размерах массива
эффективность оптимизации становиться меньше
'''