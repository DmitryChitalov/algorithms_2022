"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from numba import jit
from numba.typed import List
from timeit import Timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@jit(nopython=True)
def func_2(nums):
    """
    Декоратор @jit из библиотеки numba компилирует код во время первого исполнения.
    При последующих вызовах выполнение кода происходит без интерпретатора Python,
    поэтому получаем преимущество в производительности.
    """
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


user_nums = [i for i in range(1, 10 ** 5 + 1)]
iterations = 1000
print(f'1. Замер времени работы функции func_1(nums)\nСгенерирован список чисел'
      f' от {user_nums[0]} до {user_nums[len(user_nums) - 1]}')
timer_1 = Timer(stmt="func_1(user_nums)", setup="from __main__ import func_1", globals=globals())
exec_time_1 = timer_1.timeit(number=iterations)
print(f'Время работы функции на {iterations} итераций составило {exec_time_1:.2f} секунд\n')
"""
Для эффективной работы со списками и словарями, согласно документации numba, их необходимо переформатировать в
библиотечный формат typed. Формат необходимо импортировать.
В противном случае скорость выполнения кода будет хуже и будет предупреждение о том, что стандартные списки и словари
Python скоро перестанут поддерживаться.
"""
typed_user_nums = List()
[typed_user_nums.append(n) for n in user_nums]
print(f'2. Замер времени работы функции func_1(nums) с декоратором @jit\nСгенерирован список чисел'
      f' от {typed_user_nums[0]} до {typed_user_nums[len(typed_user_nums) - 1]}')
timer_2 = Timer(stmt="func_2(typed_user_nums)", setup="from __main__ import func_2", globals=globals())
exec_time_2 = timer_2.timeit(number=iterations)
print(f'Время работы функции на {iterations} итераций составило {exec_time_2:.2f} секунд\n')
print(f'C декоратором @jit функция работает в {exec_time_1/exec_time_2:.2f} раз быстрее')



