from task_4 import func_1, func_2, func_3
from timeit import timeit


print(timeit('func_1()', globals=globals(), number=10000000))
print(timeit('func_2()', globals=globals(), number=10000000))
print(timeit('func_3()', globals=globals(), number=10000000))
