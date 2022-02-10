from random import randint
from timeit import timeit

m = 5
test_list = [randint(-100, 100) for _ in range(2 * m + 1)]


def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data


sorted_list = shell(test_list)
print(sorted_list)
print(f'Медиана: {sorted_list[m]}')

print(timeit('shell(test_list[:])', globals=globals(), number=100))

# 2
m = 50
test_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('shell(test_list[:])', globals=globals(), number=100))

# 3
m = 500
test_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('shell(test_list[:])', globals=globals(), number=100))

"""
Замеры:
0.0011110999999999968
0.03260179999999999
0.7327408000000001
"""