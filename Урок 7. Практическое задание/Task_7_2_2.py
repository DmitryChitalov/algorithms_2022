from statistics import median
from random import randint
from timeit import timeit


def median_remove_max(my_list):
    removable_list = my_list.copy()

    for _ in range(len(my_list) // 2):
        removable_list.remove(max(removable_list))

    return max(removable_list)


def median_equal_sides(my_lilst_1):
    border = len(my_lilst_1) // 2
    left_side = []
    right_side = []
    mid = []

    for item in my_lilst_1:
        for element in my_lilst_1:
            if element > item:
                right_side.append(element)
            elif element < item:
                left_side.append(element)
            else:
                mid.append(element)

        if mid:
            mid.remove(item)

        for el in mid:
            left_side.append(el) if len(left_side) < border else right_side.append(el)

        if len(left_side) == len(right_side):
            return item

        left_side.clear()
        right_side.clear()
        mid.clear()

m_3 = (5, 50, 500)

test_list = tuple([randint(0, 100) for _ in range(m * 2 + 1)] for m in m_3)

print('\n\nФункция на основе удаления максимального элемента:')
for test in test_list:
    print(f'\nМассив из {len(test)} элемента(-ов): {median_remove_max(test)}')
    print(f'Проверка встроенной функцией statistics  median: {median(test)}')
    print(f'Время выполнения: {timeit("median_remove_max(test)", globals=globals(), number=1000)}')

    """
Функция на основе удаления максимального элемента:

Массив из 11 элемента(-ов): 38
Проверка встроенной функцией statistics  median: 38
Время выполнения: 0.0029959999999999987

Массив из 101 элемента(-ов): 55
Проверка встроенной функцией statistics  median: 55
Время выполнения: 0.0819473

Массив из 1001 элемента(-ов): 50
Проверка встроенной функцией statistics  median: 50
Время выполнения: 6.5124099

"""

print('\n\nФункция на основе разбиения и равенства массивов:')
for test in test_list:
    print(f'\nМассив из {len(test)} элемента(-ов): {median_equal_sides(test)}')
    print(f'Проверка встроенной функцией statistics  median: {median(test)}')
    print(f'Время выполнения: {timeit("median_equal_sides(test)", globals=globals(), number=1000)}')

"""
Функция на основе разбиения и равенства массивов:

ассив из 11 элемента(-ов): 29
Проверка встроенной функцией statistics  median: 29
Время выполнения: 0.005790399999999529

Массив из 101 элемента(-ов): 49
Проверка встроенной функцией statistics  median: 49
Время выполнения: 0.13878889999999977

Массив из 1001 элемента(-ов): 51
Проверка встроенной функцией statistics  median: 51
Время выполнения: 10.985434700000003

"""
