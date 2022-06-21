from random import randint
from statistics import median
from timeit import timeit

m = 5
test_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(test_list)

print(median(test_list))

print(timeit('median(test_list[:])', globals=globals(), number=100))

# 2
m = 50
test_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('median(test_list[:])', globals=globals(), number=100))

# 3
m = 500
test_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('median(test_list[:])', globals=globals(), number=100))

"""
Замеры:
0.00013049999999999173
0.0006707000000000102
0.020691299999999996
"""