"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100]. Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ, помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
from random import randint
from timeit import timeit


def bubble_sort_asc(li):
    """Простая сортировка пузырьком по возрастанию"""
    for i in range(len(li)):
        for j in range(len(li) - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li


def bubble_sort_dec(li):
    """Простая сортировка пузырьком по убыванию"""
    for i in range(len(li)):
        for j in range(len(li) - 1):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li


def bubble_sort_asc_best(li):
    """Улучшенная сортировка пузырьком по возрастанию"""
    work = True
    while work:
        work = False
        for i in range(len(li) - 1):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                work = True
    return li


def bubble_sort_dec_best(li):
    """Улучшенная сортировка пузырьком по убыванию"""
    work = True
    while work:
        work = False
        for i in range(len(li) - 1):
            if li[i] < li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                work = True
    return li

# -----------------------------------------------------------------------------
print('-' * 60)
origin_list = [randint(-100, 100) for _ in range(10)]
print(origin_list)
sorted_list = bubble_sort_dec_best(origin_list[:])
print(sorted_list)
print()
del origin_list

# -----------------------------------------------------------------------------
origin_list = [randint(-100, 100) for _ in range(10)]
print('-' * 60)
# Измерение среднего время выполнения куска кода.
time_simple = timeit(stmt="bubble_sort_dec(origin_list[:])",  # проверяемый код
                     number=100,  # число циклов измерений
                     globals=globals())  # область видимости
print(f"bubble_sort_dec(li)      {'%.8f' % time_simple} seconds")
time_best = timeit(stmt="bubble_sort_dec_best(origin_list[:])",
                   number=100,
                   globals=globals())
print(f"bubble_sort_dec_best(li) { '%.8f' % time_best} seconds")
print(f"Прирост скорости: {(time_simple - time_best)/time_simple * 100} %")
print()
del origin_list

# -----------------------------------------------------------------------------
print('-' * 60)
origin_list = [randint(-100, 100) for _ in range(100)]
# Измерение среднего время выполнения куска кода.
time_simple = timeit(stmt="bubble_sort_dec(origin_list[:])",  # проверяемый код
                     number=100,  # число циклов измерений
                     globals=globals())  # область видимости
print(f"bubble_sort_dec(li)      {'%.8f' % time_simple} seconds")
time_best = timeit(stmt="bubble_sort_dec_best(origin_list[:])",
                   number=100,
                   globals=globals())
print(f"bubble_sort_dec_best(li) { '%.8f' % time_best} seconds")
print(f"Прирост скорости: {(time_simple - time_best)/time_simple * 100} %")
print()
del origin_list

# -----------------------------------------------------------------------------
origin_list = [randint(-100, 100) for _ in range(1000)]
print('-' * 60)
# Измерение среднего время выполнения куска кода.
time_simple = timeit(stmt="bubble_sort_dec(origin_list[:])",  # проверяемый код
                     number=100,  # число циклов измерений
                     globals=globals())  # область видимости
print(f"bubble_sort_dec(li)      {'%.8f' % time_simple} seconds")
time_best = timeit(stmt="bubble_sort_dec_best(origin_list[:])",
                   number=100,
                   globals=globals())
print(f"bubble_sort_dec_best(li) { '%.8f' % time_best} seconds")
print(f"Прирост скорости: {(time_simple - time_best)/time_simple * 100} %")
print()

"""
------------------------------------------------------------
[71, -92, 9, -70, 12, -16, 35, 8, 21, 76]
[76, 71, 35, 21, 12, 9, 8, -16, -70, -92]

------------------------------------------------------------
bubble_sort_dec(li)      0.00139210 seconds
bubble_sort_dec_best(li) 0.00111730 seconds
Прирост скорости: 19.739961209683113 %

------------------------------------------------------------
bubble_sort_dec(li)      0.12045250 seconds
bubble_sort_dec_best(li) 0.10652500 seconds
Прирост скорости: 11.562649177061484 %

------------------------------------------------------------
bubble_sort_dec(li)      13.21427800 seconds
bubble_sort_dec_best(li) 12.61850010 seconds
Прирост скорости: 4.508592145556495 %

"""
