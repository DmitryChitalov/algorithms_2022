from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in nums if nums.index(i) % 2 == 0]
    return new_arr

print(timeit('func_1(numbers[:])', globals=globals()))
print(timeit('func_2(numbers[:])', globals=globals()))