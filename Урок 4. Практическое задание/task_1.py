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
    return [i for i, v in enumerate(nums) if not v % 2]


"""
print('-' * 80)
test_arr = [n for n in range(10)]
print(func_1(test_arr))
print(func_2(test_arr))
"""
# 1000
print('-' * 80)
test_arr1 = [n for n in range(0, 1000)]
print("func_1(nums) ",
      timeit(stmt="func_1(test_arr1)",
             number=1000,
             globals=globals()),
      " seconds"
      )
print("func_2(nums) ",
      timeit(stmt="func_2(test_arr1)",
             number=1000,
             globals=globals()),
      " seconds"
      )

# 10000
print('-' * 80)
test_arr2 = [n for n in range(0, 10000)]
print("func_1(nums) ",
      timeit(stmt="func_1(test_arr2)",
             number=1000,
             globals=globals()),
      " seconds"
      )
print("func_2(nums) ",
      timeit(stmt="func_2(test_arr2)",
             number=1000,
             globals=globals()),
      " seconds"
      )

# 100000
print('-' * 80)
test_arr3 = [n for n in range(0, 100000)]
print("func_1(nums) ",
      timeit(stmt="func_1(test_arr3)",
             number=1000,
             globals=globals()),
      " seconds"
      )
print("func_2(nums) ",
      timeit(stmt="func_2(test_arr3)",
             number=1000,
             globals=globals()),
      " seconds"
      )
print('-' * 80)
"""
--------------------------------------------------------------------------------
func_1(nums)  0.11228550000032556  seconds
func_2(nums)  0.07094989999950485  seconds
--------------------------------------------------------------------------------
func_1(nums)  0.9754320000001826  seconds
func_2(nums)  0.7271090999993248  seconds
--------------------------------------------------------------------------------
func_1(nums)  9.670275600000423  seconds
func_2(nums)  7.385107899999639  seconds
--------------------------------------------------------------------------------

Вывод: using list comprehension func_2(nums) reduces 
       execution time by 27%, 25% and 24%.
"""