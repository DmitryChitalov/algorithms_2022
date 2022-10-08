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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums, new_arr, i):
    if len(nums) == i:
        return new_arr
    else:
        if nums[i] % 2 == 0:
            new_arr.append(i)
        i += 1
        return func_2(nums, new_arr, i)


def func_3(nums):
    new_arr = []
    [new_arr.append(i) for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


my_lst = [1, 3, 4, 2, 5, 8]

t1 = Timer(stmt="func_1(my_lst)", setup="from __main__ import func_1", globals=globals())
print("Индексы четных чисел с функцией func_1 ", t1.timeit(number=10000), "seconds")

t2 = Timer(stmt="func_2(my_lst, list(), 0)", setup="from __main__ import func_2", globals=globals())
print("Индексы четных чисел с функцией func_2 ", t2.timeit(number=10000), "seconds")

t3 = Timer(stmt="func_3(my_lst)", setup="from __main__ import func_3", globals=globals())
print("Индексы четных чисел с функцией func_3 ", t3.timeit(number=10000), "seconds")


"""
Более оптимального алгоритма не нашел...
Алгоритм через рекурсию становится тяжелее в 2 раза, наверное ввиду необходимости 2-х проверок
Алгоритм list comprehensions так же оказывается в 1.5 раза дольше.
"""
