"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

"""
Дописал вторую функцию, заменив цикл на LC, сделал замеры времени, которые подвердили, что LC несколько быстрее цикла
0.27936930000000004
0.24561349999999998
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


num = [x**2 for x in range(1, 50)]


print(timeit("func_1(num)", "from __main__ import func_1, num", number=100000))
print(timeit("func_2(num)", "from __main__ import func_2, num", number=100000))
