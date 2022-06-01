"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randint
from statistics import median
from timeit import timeit


def test(l_input):
    left_list = []
    right_list = []
    mid = median(l_input)
    m = len(l_input) // 2
    for el in l_input:
        if el < mid:
            left_list.append(el)
        elif el > mid:
            right_list.append(el)
    while len(left_list) < m:
        left_list.append(mid)
    while len(right_list) < m:
        right_list.append(mid)
    return left_list, mid, right_list


m = 10
list_for_test = [randint(0, 1000) for i in range(2 * m + 1)]
print(
    timeit(
        "test(list_for_test[:])",
        globals=globals(),
        number=1000))
m = 100
list_for_test = [randint(0, 1000) for i in range(2 * m + 1)]
print(
    timeit(
        "test(list_for_test[:])",
        globals=globals(),
        number=1000))
m = 1000
list_for_test = [randint(0, 1000) for i in range(2 * m + 1)]
print(
    timeit(
        "test(list_for_test[:])",
        globals=globals(),
        number=1000))

"""
Лучше всего работает встроенная функция median.
В 2_1 выполняется сортировка и на выходе мы имеем еще и отсортированный лист
"""