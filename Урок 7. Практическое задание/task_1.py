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


def arr_gen(dim: int):
    return [random.randint(-100, 100) for _ in range(0, dim)]

'''
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj
'''


def bubble_sort_st(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_opt(lst_obj):
    n = 1
    while n < len(lst_obj):
        count = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                count += 1
        if count > 0:
            n += 1
        else:
            break
    return lst_obj


if __name__ == '__main__':
    my_arr = arr_gen(100)
    my_arr_copy = my_arr[:]
    print('\nИсходный массив')
    print(my_arr)
    print('\nМассив, отсортированный пузырьком (без доработки)')
    print(bubble_sort_st(my_arr_copy))
    t1 = timeit(stmt='bubble_sort_st(my_arr[:])',
                setup='from __main__ import bubble_sort_st',
                globals=globals(),
                number=1000)
    t2 = timeit(stmt='bubble_sort_st(my_arr_copy)',
                setup='from __main__ import bubble_sort_st',
                globals=globals(),
                number=1000)
    print(f'\n1000 повторов сортировки,'
          f' при этом на вход функции каждый раз подается неотсортированный массив: {t1:.5f} сек.')
    print(f'1000 повторов сортировки,'
          f' при этом после 1-го повтора на вход функции подается уже отсортированный массив: {t2:.5f} сек.')

    print('\nМассив, отсортированный пузырьком (c доработкой)')
    print(bubble_sort_opt(my_arr_copy))
    t1 = timeit(stmt='bubble_sort_opt(my_arr[:])',
                setup='from __main__ import bubble_sort_opt',
                globals=globals(),
                number=1000)
    t2 = timeit(stmt='bubble_sort_opt(my_arr_copy)',
                setup='from __main__ import bubble_sort_opt',
                globals=globals(),
                number=1000)
    print(f'\n1000 повторов сортировки,'
          f' при этом на вход функции каждый раз подается неотсортированный массив: {t1:.5f} сек.')
    print(f'1000 повторов сортировки,'
          f' при этом после 1-го повтора на вход функции подается уже отсортированный массив: {t2:.5f} сек.\n\n'
          f'          ВЫИГРЫШ ПО ВРЕМЕНИ ПРИ СОРТИРОВКЕ УЖЕ СОРТИРОВАННЫХ ДАННЫХ')
