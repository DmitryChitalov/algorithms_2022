"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import Timer
from random import choices


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """
    Использование list comprehensions самый оптимальный вариант
    преимущество в его использовании перед списком как я понял
    не вызывает метод append
    :param nums:
    :return:
    """
    new_arr = [x for x in range(len(nums)) if nums[x] % 2 == 0]
    return new_arr


# timer settings
run_num = 10000
arr = choices(list(range(10000)), k=1000)
# Func 1
t1 = Timer(stmt=f'func_1({arr})', setup="from __main__ import func_1")
print(f'Func_1 : {t1.timeit(run_num)} seconds')
# Func_1 : 1.2108487000000423 seconds

# Func 2
t2 = Timer(stmt=f'func_2({arr})', setup="from __main__ import func_2")
print(f'Func_2 : {t2.timeit(run_num)} seconds')
# Func_2 : 0.807719200000065 seconds

"""
Я писал несколько алгоритмов но ничего лучше чем выражение списков не придумал
Не стал делать рекурсию изза стеков вызовов
"""