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


def buble_sort_org(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def buble_sort_new(lst_obj):
    n = 1
    replace = True
    while replace:
        replace = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                replace = True
        n += 1
    return lst_obj


my_lst = [randint(-100, 100) for _ in range(100)]

print(f'Время оригинальной ф-ции сортировки:',
      timeit(
          "buble_sort_org(my_lst[:])",
          globals=globals(),
          number=1000))

print(f'Время улучшенной ф-ции сортировки:',
      timeit(
          "buble_sort_new(my_lst[:])",
          globals=globals(),
          number=1000))

print(f'Исходный массив: {my_lst}')
print(f'Отсортированный массив: {buble_sort_new(my_lst)}')

"""
Время оригинальной ф-ции сортировки: 3.2011459000059403
Время улучшенной ф-ции сортировки: 2.8315208999993047

Исходный массив: [-40, 41, -53, -95, 29, 76, -23, 48, -41, -82, -77, -84, 77, 31, 54, -13, 66, 63, 69, -64, 51, -20, 
                  92, 67, -34, 12, 18, -15, 37, 84, -17, -22, 73, 95, 37, 1, -66, 10, -91, 30, -46, 13, 33, -32, 5, 
                  79, -7, 82, -29, -44, 4, -25, 43, -32, -77, -77, -58, -80, 1, 36, 98, -94, -10, 83, 100, -6, -42, 
                  -50, 78, -64, 77, -95, 59, 13, -10, -70, 0, 2, -61, -5, -24, -17, -22, -6, 7, 6, 25, 87, -1, -38, 
                  -58, -44, -51, 63, -82, 53, 63, 17, -62, -30]
                  
Отсортированный массив: [100, 98, 95, 92, 87, 84, 83, 82, 79, 78, 77, 77, 76, 73, 69, 67, 66, 63, 63, 63, 59, 54, 53, 
                         51, 48, 43, 41, 37, 37, 36, 33, 31, 30, 29, 25, 18, 17, 13, 13, 12, 10, 7, 6, 5, 4, 2, 1, 1, 
                         0, -1, -5, -6, -6, -7, -10, -10, -13, -15, -17, -17, -20, -22, -22, -23, -24, -25, -29, -30, 
                         -32, -32, -34, -38, -40, -41, -42, -44, -44, -46, -50, -51, -53, -58, -58, -61, -62, -64, -64,
                         -66, -70, -77, -77, -77, -80, -82, -82, -84, -91, -94, -95, -95]


Доработка однозначно помогла, так как выполняется меньше итераций по массиву,
это ускоряет выполнение кода! 

"""
