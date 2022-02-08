import collections
import functools


def calc():
    nums = collections.defaultdict(list)
    for d in range(2):
        n = input(f"Введите {d + 1}-е натуральное шестнадцатиричное число: ")
        nums[f"{d + 1}-{n}"] = list(n)
    print(nums)
    sum_res = sum([int(''.join(i), 16) for i in nums.values()])
    print(sum_res)
    print("Сумма: ", list('%X' % sum_res))
    mul_res = functools.reduce(lambda a, b: a * b,
                               [int(''.join(i), 16) for i in nums.values()])
    print("Произведение: ", list('%X' % mul_res))


calc()
