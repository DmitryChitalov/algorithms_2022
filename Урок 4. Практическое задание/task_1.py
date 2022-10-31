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
    new_arr = [i for i in range(len(nums)) if nums[i] == 0]
    return new_arr


num_1 = [i for i in range(100)]
num_2 = [i for i in range(1000)]

print(timeit("func_1(num_1)", globals=globals(), number=10000))
print(timeit("func_2(num_1)", globals=globals(), number=10000))

print(timeit("func_1(num_2)", globals=globals(), number=10000))
print(timeit("func_2(num_2)", globals=globals(), number=10000))

#  func_1, 100 - 0.055011200020089746
#  func_2, 100 - 0.032153000007383525

#  func_1, 1000 - 0.601673299970571
#  func_2, 1000 - 0.2650100999744609

"""
Через List Comprehension выполняется быстрее, при 100 это не сильно влияет, но если чисел уже 1000, то уже заметнее
"""
