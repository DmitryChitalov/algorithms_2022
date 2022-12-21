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


orig_list = [randint(-100, 100) for i in range(100)]

bubble_sort(orig_list)


print(bubble_sort.__name__, timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=10000))


def bubble_flag(list_to_sort):
    flag = True
    while flag:
        flag = False
        for i in range(len(list_to_sort) - 1):
            if list_to_sort[i] < list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]
                flag = True


lists = [randint(-100, 100) for j in range(100)]

bubble_flag(lists)


print(bubble_flag.__name__, timeit(
        "bubble_flag(lists[:])",
        globals=globals(),
        number=10000))

'''bubble_sort 5.764909999095835
bubble_flag 0.11965203599538654
При использовании флага время выполнения сортировки быстрее
'''
