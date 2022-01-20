from statistics import median
from random import randint
from timeit import timeit

def stat_median(my_list_2):
    median(my_list_2)

    return median(my_list_2)


m_3 = (5, 50, 500)

test_list = tuple([randint(0, 100) for _ in range(m * 2 + 1)] for m in m_3)


print('\n\nФункция на основе встроенной функцией statistics  median:')
for test in test_list:
    print(f'\nМассив из {len(test)} элемента(-ов): {stat_median(test)}')
    print(f'Время выполнения: {timeit("median(test)", globals=globals(), number=1000)}')

"""
Функция на основе встроенной функцией statistics  median:

Массив из 11 элемента(-ов): 34
Время выполнения: 0.00037700000000000233

Массив из 101 элемента(-ов): 49
Время выполнения: 0.0038004999999999983

Массив из 1001 элемента(-ов): 49
Время выполнения: 0.07208329999999999

"""