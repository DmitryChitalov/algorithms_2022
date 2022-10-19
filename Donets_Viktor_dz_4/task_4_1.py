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


def func_2(nums):
    new_arr = [x for x in range(len(nums)) if x % 2 != 0]
    return new_arr


print(timeit("func_1([i for i in range(100)])", globals=globals(),
             number=1000))
print('!' * 25)
some_lst = [i for i in range(1, 101)]
print(timeit("func_1(some_lst)", globals=globals(), number=1000))
print('!' * 25)
print(timeit("func_2(some_lst)", globals=globals(), number=1000))

"""
0.013496499999746447
!!!!!!!!!!!!!!!!!!!!!!!!!
0.010053899997728877
!!!!!!!!!!!!!!!!!!!!!!!!!
0.005820700000185752
"""

"""
Во-первых функция будет быстрей работать с уже готовым списком, а не 
создавать его внутри.
Во-вторых, для увеличения скорости работы функции используем 
list comprehension.
"""
