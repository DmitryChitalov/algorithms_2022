"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
###########################################################################

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


lst_obj = [1, 2, 3, 4, 5, 6]
print(timeit("func_1(lst_obj)", globals=globals(), number=1000))


def func_2(nums):
    new_arr = []
    for i in range(1, len(nums), 2):
        new_arr.append(i)
    return new_arr


print(timeit("func_2(lst_obj)", globals=globals(), number=1000))


def func_3(nums):
    new_arr = nums[::2]
    return new_arr


print(timeit("func_3(lst_obj)", globals=globals(), number=1000))


print(func_1(lst_obj))
print(func_2(lst_obj))
print(func_3(lst_obj))

"""
Аналитика:
В функции func_2 я убрал условие поиска и математическое действие и начал добавлять элементы 
в новый массив с шагом 2. Это помогло увеличить  скорость решения примерно на 60%.
В функции func_3 я скопировал массив с шагом 2. Это помогло увеличить  скорость решения примерно в 4 раза.
Я считаю функция func_3 самая оптимальная из выше представленных.
"""
