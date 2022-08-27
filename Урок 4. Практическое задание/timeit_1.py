from task_1 import func_1, func_2
from timeit import timeit


nums_1000 = [x for x in range(1000)]
print('nums_1000')
print(timeit('func_1(nums_1000)', globals=globals(), number=1000))
print(timeit('func_2(nums_1000)', globals=globals(), number=1000))
print('-' * 100)

print('nums_10000')
nums_10000 = [x for x in range(10000)]
print(timeit('func_1(nums_10000)', globals=globals(), number=1000))
print(timeit('func_2(nums_10000)', globals=globals(), number=1000))
print('-' * 100)

print('nums_100000')
nums_100000 = [x for x in range(100000)]
print(timeit('func_1(nums_100000)', globals=globals(), number=1000))
print(timeit('func_2(nums_100000)', globals=globals(), number=1000))
print('-' * 100)

