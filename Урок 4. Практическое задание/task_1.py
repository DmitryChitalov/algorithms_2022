"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_1_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr = new_arr + [i]
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return [i for i, en in enumerate(nums) if en % 2 == 0]


print(f'Время выполнения функции: {timeit("func_1", globals=globals(), number=1000000)}')
print(f'Время выполнения функции: {timeit("func_1_1", globals=globals(), number=1000000)}')
print(f'Время выполнения функции: {timeit("func_2", globals=globals(), number=1000000)}')
print(f'Время выполнения функции: {timeit("func_3", globals=globals(), number=1000000)}')
print(f'Время выполнения функции с импортом: {timeit("func_1", "from __main__ import func_1", number=1000)}')
print(f'Время выполнения функции с импортом: {timeit("func_1_1", "from __main__ import func_1_1", number=1000)}')
print(f'Время выполнения функции с импортом: {timeit("func_2", "from __main__ import func_2", number=1000)}')
print(f'Время выполнения функции с импортом: {timeit("func_3", "from __main__ import func_3", number=1000)}')

"""
ничего не понял, делал разные замеры, в итоге все практически одинаковое, даже ради интереса взял пример из урока 
и добавил решение с конкатенацией

Интересный факт, если выполнить timeit с указанием конкретной функции будет работать медленнее 
print(f'Время выполнения функции: {timeit("func_1", "from __main__ import func_1", number=1000)}')
при этом разница периодически составляет в 6 раз, в уроке вы не объяснили почему, вроде бы кажется 
когда импортируешь что-то должно быть быстрее, так как globals вы сказали ищет все функции, как буд-то 
должно потратиться больше времени

вот в итоге результаты замеров 5 раз:
Время выполнения функции: 0.012503599999999997
Время выполнения функции: 0.012119200000000004
Время выполнения функции: 0.011529200000000003
Время выполнения функции: 0.012964400000000001
Время выполнения функции: 8.399999999991747e-06
Время выполнения функции: 8.400000000005625e-06
Время выполнения функции: 8.400000000005625e-06
Время выполнения функции: 8.400000000005625e-06

Время выполнения функции: 0.0116152
Время выполнения функции: 0.011513799999999998
Время выполнения функции: 0.011586500000000007
Время выполнения функции: 0.011518700000000007
Время выполнения функции с импортом: 8.499999999994623e-06
Время выполнения функции с импортом: 8.400000000005625e-06
Время выполнения функции с импортом: 8.399999999991747e-06
Время выполнения функции с импортом: 8.399999999991747e-06
 
Время выполнения функции: 0.016929400000000004
Время выполнения функции: 0.012884899999999998
Время выполнения функции: 0.013459299999999993
Время выполнения функции: 0.0130324
Время выполнения функции с импортом: 8.5000000000085e-06
Время выполнения функции с импортом: 9.200000000000874e-06
Время выполнения функции с импортом: 9.200000000000874e-06
Время выполнения функции с импортом: 2.3099999999998122e-05  тут что-то пошло очень даже так :)

Время выполнения функции: 0.021245799999999995
Время выполнения функции: 0.013670699999999994
Время выполнения функции: 0.012328600000000009
Время выполнения функции: 0.0126333
Время выполнения функции с импортом: 9.299999999989872e-06
Время выполнения функции с импортом: 9.200000000000874e-06
Время выполнения функции с импортом: 9.200000000000874e-06
Время выполнения функции с импортом: 9.200000000000874e-06

Время выполнения функции: 0.0149122
Время выполнения функции: 0.0139011
Время выполнения функции: 0.014571700000000007
Время выполнения функции: 0.012985299999999991
Время выполнения функции с импортом: 9.200000000000874e-06
Время выполнения функции с импортом: 9.200000000000874e-06
Время выполнения функции с импортом: 9.200000000000874e-06
Время выполнения функции с импортом: 9.200000000000874e-06
"""
"""
Интересный факт, если выполнить timeit с указанием конкретной функции будет работать медленнее 
print(f'Время выполнения функции: {timeit("func_1", "from __main__ import func_1", number=1000)}')
при этом разница периодически составляет в 6 раз, в уроке вы не объяснили почему, вроде бы кажется 
когда импортируешь что-то должно быть быстрее, так как globals вы сказали ищет все функции, как буд-то 
должно потратиться больше времени
"""