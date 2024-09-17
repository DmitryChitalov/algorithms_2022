from random import randint
from timeit import timeit


def find_med(arr):
    for i in range(int((len(arr)-1)/2)):
        arr.remove(max(arr))
    # print(arr)
    return max(arr)


m = 10
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
# print(orig_list)
print(find_med(orig_list))
print(
    timeit(
        "find_med(orig_list[:])",
        globals=globals(),
        number=10000))
# 0.032955082999999996
m = 100
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "find_med(orig_list[:])",
        globals=globals(),
        number=10000))

m = 1000
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "find_med(orig_list[:])",
        globals=globals(),
        number=1000))
"""
0.033273833
4.116173961
37.001731159 - за 1000 
Выигриш у сортироваки кучей на малых данных. На больших существенный проигрыш почти в 5 раз.
"""