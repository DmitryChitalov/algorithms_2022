"""
Замечания:
в конце нужно сравнить все три варианта
"""

"""
Для чистоты эксперимента переделала замеры на списках одинаковой длины 11, 101 и 1001
Резюмируем все три варианта решения на этих списках

с сортировкой:
0.004095256999789854
0.09647132999998576
1.6634782609999093

без сортировки:
0.0019714319987542694
0.0625700170003256
5.481170047998603

встроенная функция median из statistics:
0.000435653999375063
0.003051394999602053
0.07917955199991411

встроенная функция на любых списках быстрее остальных
способ без сортировки проигрывает на 1000 элементах всем
на 10 и 100 способ без сортировки показал себя лучше, чем с сортировкой
"""

from random import randint
from timeit import timeit
from statistics import median


lst_10 = [randint(-100, 100) for i in range(11)]
lst_100 = [randint(-100, 100) for i in range(101)]
lst_1000 = [randint(-100, 100) for i in range(1001)]


def mediana(lst):
    lst = lst[:]
    for i in range((len(lst) + 1)//2):
        med = lst.pop(lst.index(max(lst)))
    return med



print(timeit('mediana(lst_10[:])', globals=globals(), number=1000))
print(timeit('mediana(lst_100[:])', globals=globals(), number=1000))
print(timeit('mediana(lst_1000[:])', globals=globals(), number=1000))



lst_10_1 = [randint(-100, 100) for i in range(11)]
lst_100_2 = [randint(-100, 100) for i in range(101)]
lst_1000_3 = [randint(-100, 100) for i in range(1001)]


print(timeit('median(lst_10_1)', globals=globals(), number=1000))
print(timeit('median(lst_100_2)', globals=globals(), number=1000))
print(timeit('median(lst_1000_3)', globals=globals(), number=1000))