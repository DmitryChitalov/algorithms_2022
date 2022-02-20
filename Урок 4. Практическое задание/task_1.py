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
from cProfile import run

my_list = [i for i in range(1000)]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# Оптимизируем функцию применив list comprehensions
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr



def func_time_compare(func_1, func_2):

    res_1 = timeit("func_1(my_list)", globals=globals(), number=1)
    print(res_1)
    res_2 = timeit("func_2(my_list)", globals=globals(), number=1)
    print(res_2)
    return  ((res_1 - res_2) / res_1) * 100

print(f'Разница во времени между первым и вторым вариантом составляет {func_time_compare(func_1, func_2):.2f} %')


#
# Вывод: Применив list comprehension удалось увеличить скорость работы функции примерно на 10-20%.
# 6.969999999999893e-05
# 5.8000000000002494e-05
# Разница во времени между первым и вторым вариантом составляет 16.79 %