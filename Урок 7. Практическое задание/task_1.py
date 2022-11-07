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

"""Сортировка пузырьком"""

from random import randint
from timeit import timeit


def bubble_sort_reverse(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

def bubble_sort_reverse_upd(lst_obj):
    n = 1
    breaker = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                # Заменил знак, чтобы сортировать в порядке убывания
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                breaker += 1
        if breaker == 0:
            break

        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]


print(bubble_sort_reverse(orig_list[:]))
print(bubble_sort_reverse_upd(orig_list[:]))

"""
Убрал из замеров копирование оригинального списка, чтобы увидеть разницу с измененным,
в результате замера видно, что при проходах, даже по уже упорядоченному списку, если не прерывать цикл, то уходит времени меньше, 
но все равно значительно больше, чем с проверкой на сортировку.
[100, 71, 53, 27, 11, -37, -49, -51, -82, -85]
[100, 71, 53, 27, 11, -37, -49, -51, -82, -85]
0.004104299999999998
0.2352596
25.339509900000003
0.0006799999999991257
0.005061600000001221
0.10431499999999971
"""

# замеры 10

print(
    timeit(
        "bubble_sort_reverse(orig_list)",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "bubble_sort_reverse(orig_list)",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "bubble_sort_reverse(orig_list)",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit(
        "bubble_sort_reverse_upd(orig_list)",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "bubble_sort_reverse_upd(orig_list)",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "bubble_sort_reverse_upd(orig_list)",
        globals=globals(),
        number=1000))
