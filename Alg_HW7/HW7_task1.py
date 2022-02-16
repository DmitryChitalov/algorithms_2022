"""Сортировка пузырьком"""

from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = 0
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = 1
        if flag == 0:
            # print('Флаг поднят', n)
            break
        n += 1
    return lst_obj  # сначала я решил посмотреть есть ли выигрыш по итерациям статистически
    # и сделал return n


def bubble_sort_1(lst_obj):  # чтобы сразу сравнить время без флага
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


# посмотрел сколько в среднем итераций выигрывается

def count_avg_iter(num):
    avg_iter = 0
    for i in range(1000):
        avg_iter += bubble_sort([randint(-100, 100) for _ in range(num)])  # я делал return n
    avg_iter /= 1000
    print('Среднее число итераций', avg_iter)


# count_avg_iter(10)  # в среднем 7.5
# count_avg_iter(100)  # в среднем 88-89
# count_avg_iter(1000)  # в среднем 960

# Сделаем теперь временные замеры
orig_list = [randint(-100, 100) for _ in range(10)]
# замеры 10
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]
# замеры 100
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры 1000
orig_list = [randint(-100, 100) for _ in range(1000)]
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))
"""
0.008755172000000006
0.009364294999999995
0.756634304
0.766357064
86.58885137
86.28729246
"""
# Равенство во временах в рамках погрешности - доработка не помогла. Для маленьких массивов
# доработка может быть эффективна, т к в среднем число итераций для рандомных массивов
# падает на 25%. Доработка также поможет, если наш массив более менее упорядочен,
# когда итераций нужно меньше и не нужно тратить лишние ресурсы.
