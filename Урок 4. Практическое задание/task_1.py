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
    """ cycle + append """
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """ list comprehentions """
    return [i for i, el in enumerate(nums) if el % 2 == 0]


ar = [i for i in range(1, 99)]
lunches = 100_000

print(f'The array: {ar}')
print('-' * 100)
print(f'Function #1 result:{func_1(ar)}')
t1 = timeit('func_1(ar)', globals=globals(), number=lunches)
t2 = timeit('func_2(ar)', globals=globals(), number=lunches)

print(f'Function #1 execution takes {t1} seconds for {lunches} executions')
print('-' * 100)
print(f'Function #2 result:{func_2(ar)}')
print(f'Function #2 execution takes {t2} seconds for {lunches} executions')
print('-' * 100)

# Analytics:
dif = max([t1, t2]) - min([t1, t2])
dif_p = round(1 - min([t1, t2]) / max([t1, t2]), 4) * 100
print(f'The difference between{func_1.__doc__}vs{func_2.__doc__}is: {dif} sec\n'
      f'{"func_1" if min([t1, t2]) == t1 else "func_2 (optimized one)"} '
      f'with the{func_1.__doc__ if min([t1, t2]) == t1 else func_2.__doc__}is {dif_p}% '
      f'more efficient, than the other one\n'
      f'Which means the{func_1.__doc__ if min([t1, t2]) == t1 else func_2.__doc__}won.')


"""
The difference between cycle + append  vs  list comprehentions is: 0.111149041 sec
func_2 (optimized one) with the list comprehentions is 25.2% more efficient, than the other one
Which means the list comprehentions won.
"""

# Conclusion: LC wins. Flawless victory.

