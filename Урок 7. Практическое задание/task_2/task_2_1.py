"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def comb_sort(l_input):
    l_len = len(l_input)
    gap = int(l_len // 1.247) if l_len > 1 else 0
    while gap:
        swapped = False
        for i in range(l_len - gap):
            if l_input[i + gap] < l_input[i]:
                l_input[i], l_input[i + gap] = l_input[i + gap], l_input[i]
                swapped = True
        gap = int(gap // 1.247) or swapped
    return l_input[:(l_len//2)], l_input[l_len//2], l_input[(l_len//2)+1:]


m = 10
list_for_test = [randint(0, 1000) for i in range(2 * m + 1)]
print(
    timeit(
        "comb_sort(list_for_test[:])",
        globals=globals(),
        number=1000))
m = 100
list_for_test = [randint(0, 1000) for i in range(2 * m + 1)]
print(
    timeit(
        "comb_sort(list_for_test[:])",
        globals=globals(),
        number=1000))
m = 1000
list_for_test = [randint(0, 1000) for i in range(2 * m + 1)]
print(
    timeit(
        "comb_sort(list_for_test[:])",
        globals=globals(),
        number=1000))
"""
Использовал сортировку "Расчёски": по факту пузырьковая сортировка но сравнивающая не соседние элементы
а элементы на расстоянии 1,247 от длины строки и постепенно уменьшая  
Замеры:
0.014943100000000004
0.2458744
4.2970429
"""