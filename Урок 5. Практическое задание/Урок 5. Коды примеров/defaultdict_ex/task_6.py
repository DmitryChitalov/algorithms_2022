from timeit import timeit
from collections import defaultdict

s = [('раз', 1), ('два', 2), ('раз', 3), ('два', 4), ('три', 1)]
d_1 = defaultdict(list)
d_2 = {}


def check_1():
    for k, v in s:
        d_1[k].append(v)
    return d_1


def check_2():
    for k, v in s:
        d_2.setdefault(k, []).append(v)
    return d_2


print(timeit(check_1))  # 0.78448056
print(timeit(check_2))  # 1.2408615469999997
