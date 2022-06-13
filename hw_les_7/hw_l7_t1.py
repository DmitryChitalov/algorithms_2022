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


def bub_sort_rev(sorted_list):
    my_list = sorted_list[:]
    n = 1
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        n += 1
    return f'исходный массив {sorted_list}, \nотсортированный массив {my_list}'


def smart_bub_sort_rev(sorted_list):
    my_list = sorted_list[:]
    n = 1
    mark = 0
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                mark = 1
        if not mark:
            return f'Доработанная функция \nисходный массив {sorted_list}, \nотсортированный массив {my_list}'
        n += 1
    return f'Доработанная функция \nисходный массив {sorted_list}, \nотсортированный массив {my_list}'


my_list = list(randint(-100, 100) for i in range(10))
print(smart_bub_sort_rev(my_list), timeit('smart_bub_sort_rev(my_list)', globals=globals(), number=10000))
print(bub_sort_rev(my_list), timeit('bub_sort_rev(my_list)', globals=globals(), number=10000))

# Доработанная функция работает быстрее, так как исключает ненужные проходы, если уже все отсартированно
