"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def test(l_input):
    left_list = []
    right_list = []
    mid = l_input[0]
    for el in l_input[1:]:
        if mid >= el:
            left_list.append(el)
        elif mid < el:
            right_list.append(el)
    if len(left_list) == len(right_list):
        return left_list, mid, right_list
    elif len(left_list) > len(right_list):
        right_list.append(mid)
        while len(left_list) > len(right_list):
            right_list.append(left_list.pop(left_list.index(max(left_list))))
        mid = right_list.pop(right_list.index(min(right_list)))
    else:
        left_list.append(mid)
        while len(left_list) < len(right_list):
            left_list.append(right_list.pop(right_list.index(min(right_list))))
        mid = left_list.pop(left_list.index(max(left_list)))
    return left_list, mid, right_list


def test2(l_input):
    crash_list = l_input[:]
    left_list = []
    while len(left_list) != len(l_input) // 2:
        left_list.append(crash_list.pop(crash_list.index(min(crash_list))))
    mid = crash_list.pop(crash_list.index(min(crash_list)))
    return left_list, mid, crash_list


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

m = 10
list_for_test = [randint(0, 1000) for i in range(2 * m + 1)]
print(
    timeit(
        "test2(list_for_test[:])",
        globals=globals(),
        number=1000))
m = 100
list_for_test = [randint(0, 1000) for i in range(2 * m + 1)]
print(
    timeit(
        "test2(list_for_test[:])",
        globals=globals(),
        number=1000))
m = 1000
list_for_test = [randint(0, 1000) for i in range(2 * m + 1)]
print(
    timeit(
        "test2(list_for_test[:])",
        globals=globals(),
        number=1000))
"""
Так получилось, два варианта...
Скорость первого варианта зависит от "удачи", но в основном быстрее
Но второй вариант стабильный и более читабельный, так же у него левая часть получается отсортированной
Результаты:
Test:
0.0074059
0.0993253
14.1613449
Test2:
0.007748399999999999
0.2858295
22.8441744
"""
