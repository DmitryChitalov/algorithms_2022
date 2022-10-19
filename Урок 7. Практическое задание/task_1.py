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

Script listing  приведен на строке  93++

Оптимизация : если при проходе ни одна перестановка не производится,
значит числа уже отсортированы, параметр is_iteration  = False,
сортировка останавливается.
Неоптимизированная функция :   Bubble_sort_reversed :  0.009294799999999999
Оптимизированная функция :   Bubble_sort_reversed_opt : 0.008665899999999999 - немного быстрее

Оптимизация эффективана.
когда на начальных проходах 2-3 начальные числа выстраваются в отсортированном порядке,
соответственно от последних 2-3 проходов можно отказаться.
"""

from random import randint
from timeit import timeit


def lst_generator():
    mylist = []
    for i in range (15):
        mylist.append(randint(-100, 100))
    return mylist


def bubble_sort_reversed(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            # print(f'{lst_obj}')
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_reversed_opt(lst_obj):
    n = 1
    while n < len(lst_obj):
        is_iteration = False
        for i in range(len(lst_obj)-n):
            # print(f'{lst_obj}')
            if lst_obj[i] < lst_obj[i+1]:
                is_iteration = True
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        if is_iteration:
            n += 1
            continue
        else:
            return lst_obj


lst_object = lst_generator()
print(f'\n List : \n {lst_object}')

print(f'\n Bubble_sort_reversed_opt :')
print(
    timeit(
        "bubble_sort_reversed_opt(lst_object[:])",
        globals=globals(),
        number=1000))
lst_object_sorted2 = bubble_sort_reversed_opt(lst_object[:])
print(f'sorted list : \n {lst_object_sorted2}')

print(f'\n Bubble_sort_reversed :')
print(
    timeit(
        "bubble_sort_reversed(lst_object[:])",
        globals=globals(),
        number=1000))
lst_object_sorted1 = bubble_sort_reversed(lst_object[:])
print(f'sorted list : \n {lst_object_sorted1}')

# Script Listing:
#
#  List :
#  [63, 60, 73, -74, -55, -20, -19, 88, -57, 100, -31, -76, -61, 23, 2]
#
#  Bubble_sort_reversed_opt :
# 0.008665899999999999
# sorted list :
#  [100, 88, 73, 63, 60, 23, 2, -19, -20, -31, -55, -57, -61, -74, -76]
#
#  Bubble_sort_reversed :
# 0.009294799999999999
# sorted list :
#  [100, 88, 73, 63, 60, 23, 2, -19, -20, -31, -55, -57, -61, -74, -76]
#
# Process finished with exit code 0
