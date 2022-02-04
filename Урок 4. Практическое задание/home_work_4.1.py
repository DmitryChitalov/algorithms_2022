from timeit import timeit
from numpy import array, where


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


def func_3(nums):
    new_arr = []
    for i in range(0, len(nums), 2):
        new_arr.append(i)
    return new_arr


def func_4(nums):
    intarray = array(nums)
    return where(intarray % 2 == 0)


NUMS = [el for el in range(1000)]
print(
    timeit(
        "func_1(NUMS[:])",
        globals=globals(),
        number=5000))

print(
    timeit(
        "func_2(NUMS[:])",
        globals=globals(),
        number=5000))

print(
    timeit(
        "func_3(NUMS[:])",
        globals=globals(),
        number=5000))

print(
    timeit(
        "func_4(NUMS[:])",
        globals=globals(),
        number=5000))

NUMS = [el for el in range(10000)]
print("-------------------------------------------------------------------")
print(
    timeit(
        "func_1(NUMS[:])",
        globals=globals(),
        number=5000))

print(
    timeit(
        "func_2(NUMS[:])",
        globals=globals(),
        number=5000))

print(
    timeit(
        "func_3(NUMS[:])",
        globals=globals(),
        number=5000))


print(
    timeit(
        "func_4(NUMS[:])",
        globals=globals(),
        number=5000))

NUMS = [el for el in range(100000)]
print("-------------------------------------------------------------------")
print(
    timeit(
        "func_1(NUMS[:])",
        globals=globals(),
        number=5000))

print(
    timeit(
        "func_2(NUMS[:])",
        globals=globals(),
        number=5000))

print(
    timeit(
        "func_3(NUMS[:])",
        globals=globals(),
        number=5000))


print(
    timeit(
        "func_4(NUMS[:])",
        globals=globals(),
        number=5000))


"""
Проверила замеры при number=1000 и number=5000.
Самая быстрая функция: func_3(nums):
def func_3(nums):
    new_arr = []
    for i in range(0, len(nums), 2):
        new_arr.append(i)
    return new_arr
Это замеры для number=5000:
0.7393194759999999
0.6030115139999999
0.26121113500000015
0.5586676710000003
-------------------------------------------------------------------
7.925316919999999
5.913597005
2.859822658999999
5.718396992000002
-------------------------------------------------------------------
83.15631159099999
63.65412162899999
31.976052437999982
53.062605093
"""