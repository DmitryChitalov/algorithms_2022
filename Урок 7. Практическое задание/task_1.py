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
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_new(lst_obj):
    n = 1
    flag = False
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
            if flag is False:
                n = len(lst_obj)
                break
        n += 1
    return lst_obj


orig_list_10 = [randint(-100, 100) for _ in range(10)]
sorted_list_10 = [i for i in range(10)]
sorted_list_10.sort(reverse=True)

print(bubble_sort(sorted_list_10[:]))
print('bubble_sort(sorted_list_10[:]) замеры 10')
# замеры 10
print(
    timeit(
        "bubble_sort(sorted_list_10[:])",
        globals=globals(),
        number=1000))

print(bubble_sort(orig_list_10[:]))
print('bubble_sort(orig_list_10[:]) замеры 10')
# замеры 10
print(
    timeit(
        "bubble_sort(orig_list_10[:])",
        globals=globals(),
        number=1000))

print(bubble_sort_new(sorted_list_10[:]))
print('bubble_sort_new(sorted_list_10[:]) замеры 10')
# замеры 10
print(
    timeit(
        "bubble_sort_new(sorted_list_10[:])",
        globals=globals(),
        number=1000))

print(bubble_sort_new(orig_list_10[:]))
print('bubble_sort_new(orig_list_10[:]) замеры 10')
# замеры 10
print(
    timeit(
        "bubble_sort_new(orig_list_10[:])",
        globals=globals(),
        number=1000))

orig_list_100 = [randint(-100, 100) for _ in range(100)]
sorted_list_100 = [i for i in range(100)]
sorted_list_100.sort(reverse=True)

print('bubble_sort(sorted_list_100[:]) замеры 100')
# замеры 100
print(
    timeit(
        "bubble_sort(sorted_list_100[:])",
        globals=globals(),
        number=1000))

print('bubble_sort(orig_list_100[:]) замеры 100')
# замеры 100
print(
    timeit(
        "bubble_sort(orig_list_100[:])",
        globals=globals(),
        number=1000))

print('bubble_sort_new(sorted_list_100[:]) замеры 100')
# замеры 100
print(
    timeit(
        "bubble_sort_new(sorted_list_100[:])",
        globals=globals(),
        number=1000))

print('bubble_sort_new(orig_list_100[:]) замеры 100')
# замеры 100
print(
    timeit(
        "bubble_sort_new(orig_list_100[:])",
        globals=globals(),
        number=1000))

orig_list_1000 = [randint(-100, 100) for _ in range(1000)]
sorted_list_1000 = [i for i in range(1000)]
sorted_list_1000.sort(reverse=True)

print('bubble_sort(sorted_list_1000[:]) замеры 1000')
# замеры 1000
print(
    timeit(
        "bubble_sort(sorted_list_1000[:])",
        globals=globals(),
        number=1000))

print('bubble_sort(orig_list_1000[:]) замеры 1000')
# замеры 1000
print(
    timeit(
        "bubble_sort(orig_list_1000[:])",
        globals=globals(),
        number=1000))

print('bubble_sort_new(sorted_list_1000[:]) замеры 1000')
# замеры 1000
print(
    timeit(
        "bubble_sort_new(sorted_list_1000[:])",
        globals=globals(),
        number=1000))

print('bubble_sort_new(orig_list_1000[:]) замеры 1000')
# замеры 1000
print(
    timeit(
        "bubble_sort_new(orig_list_1000[:])",
        globals=globals(),
        number=1000))

"""
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
bubble_sort(sorted_list_10[:]) замеры 10
0.01637619999999998
[93, 46, 29, -3, -21, -29, -46, -85, -96, -98]
bubble_sort(orig_list_10[:]) замеры 10
0.02503519999999998
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
bubble_sort_new(sorted_list_10[:]) замеры 10
0.0018087999999999993
[93, 46, 29, -3, -21, -29, -46, -85, -96, -98]
bubble_sort_new(orig_list_10[:]) замеры 10
0.028203599999999995
bubble_sort(sorted_list_100[:]) замеры 100
0.8833905999999999
bubble_sort(orig_list_100[:]) замеры 100
1.8356102
bubble_sort_new(sorted_list_100[:]) замеры 100
0.002217400000000147
bubble_sort_new(orig_list_100[:]) замеры 100
1.9196228999999998
bubble_sort(sorted_list[:]) замеры 1000
88.6964009
bubble_sort(orig_list[:]) замеры 1000
203.007579
bubble_sort_new(sorted_list[:]) замеры 1000
0.007463400000006004
bubble_sort_new(orig_list[:]) замеры 1000
234.7072582, хотя при нескольких запусках возможны и значения, на порядок меньше и даже
сравнимые с сортировкой уже отсортированного списка.

Как видно из проведенных замеров, дорабртка помогант только в том случае, 
если весь список, либо его часть, уже отсортированы, за счет того,
что не тратится время на сортировку этой части (нет лишних безрезультатных проходов по списку).
В случае с отсортированным списком время сокращается в десятки - тысячи раз, и,
чем больше исходный список, тем разрыв во времени больше.

"""
