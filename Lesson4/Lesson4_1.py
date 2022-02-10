from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


nums1 = range(0, 100)
nums2 = range(0, 10000)
nums3 = range(0, 1000000)

print(timeit("func_1(nums1)", "from __main__ import func_1, nums1", number=10))
print(timeit("func_1(nums2)", "from __main__ import func_1, nums2", number=10))
print(timeit("func_1(nums3)", "from __main__ import func_1, nums3", number=10))


def func_2(nums):
    new_lst = [x for x in range(len(nums)) if nums[x] % 2 == 0]
    return new_lst


print(timeit("func_2(nums1)", "from __main__ import func_2, nums1", number=10))
print(timeit("func_2(nums2)", "from __main__ import func_2, nums2", number=10))
print(timeit("func_2(nums3)", "from __main__ import func_2, nums3", number=10))

# Аналитика показала, что функция с list comprehension выполняется быстрее.
