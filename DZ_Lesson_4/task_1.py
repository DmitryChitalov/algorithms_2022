from timeit import *

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

n = [1, 45, 66, 34, 98, 123, 456, 76]
print(func_1(n))
print("время работы первой функции - ", Timer(stmt="func_1(n)", setup="from __main__ import func_1, n").timeit(number=100000))

def func_2(nums):
    new_arr = []
    for i in nums:
        if i % 2 == 0:
            new_arr.append(nums.index(i))
    return new_arr

n = [1, 45, 66, 34, 98, 123, 456, 76]
print(func_2(n))
print("время работы второй функции - ", Timer(stmt="func_1(n)", setup="from __main__ import func_1, n").timeit(number=100000))

"""вторая функция работает быстрее чем первая
   я убрал len(), range() и [] в if, добавил index(i)"""