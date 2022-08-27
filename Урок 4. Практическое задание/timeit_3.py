from task_3 import revers, revers_2, revers_3, revers_4, revers_5
from timeit import timeit

ENTER_NUM = 3452933333


print(timeit('revers(ENTER_NUM)', globals=globals(), number=1000))
print(timeit('revers_2(ENTER_NUM)', globals=globals(), number=1000))
print(timeit('revers_3(ENTER_NUM)', globals=globals(), number=1000))
print(timeit('revers_4(ENTER_NUM)', globals=globals(), number=1000))
print(timeit('revers_5(ENTER_NUM)', globals=globals(), number=1000))
