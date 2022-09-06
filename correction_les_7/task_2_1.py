"""
Замечания:
не прочитано ДЗ
"Массив размером 2m + 1"
при сортировке медиана будет просто по индексу m
это мы обсудили на уроке
"""


"""
моё решение и отдаёт элемент с индексом m, исходя из того, что 2m + 1 = len(lst)  => m = (len(lst) - 1) // 2
в задании написано сделать замеры на массивах длиной 10, 100, 1000 элементов, а это чётные числа,
исправила решение с учётом создания правильных списков с нечётным количеством элементов,
а также исправила ошибку в замерах
замеры на 11, 101 и 1001 элементах:
0.004095256999789854
0.09647132999998576
1.6634782609999093
"""

from random import randint
from timeit import timeit


def shell_mediana(lst):
    step = len(lst) // 2
    while step > 0:
        for i in range(step, len(lst)):
            j = i
            delta = j - step
            while delta >= 0 and lst[delta] > lst[j]:
                lst[delta], lst[j] = lst[j], lst[delta]
                j = delta
                delta = j - step
        step //= 2
    return lst[(len(lst) - 1) // 2]


m1 = 5
m2 = 50
m3 = 500
lst_10 = [randint(-100, 100) for i in range(2 * m1 + 1)]
lst_100 = [randint(-100, 100) for i in range(2 * m2 + 1)]
lst_1000 = [randint(-100, 100) for i in range(2 * m3 + 1)]

print(timeit('shell_mediana(lst_10[:])', globals=globals(), number=1000))
print(timeit('shell_mediana(lst_100[:])', globals=globals(), number=1000))
print(timeit('shell_mediana(lst_1000[:])', globals=globals(), number=1000))