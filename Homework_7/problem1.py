from random import randint
from timeit import timeit

n = [randint(-100, 100) for i in range(100)]

def func_old(a):
    i = 0
    while i < len(a) - 1:
        j = 0
        m = 0
        while j < len(a) - 1 - i:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
        i += 1
    return a

def func_new(a):
    i = 0
    while i < len(a) - 1:
        j = 0
        m = 0
        while j < len(a) - 1 - i:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                m += 1
            j += 1
        if m == 0:
            return a
        i += 1

print(timeit('func_old(n)', number=1000, globals=globals()))
print(timeit('func_new(n)', number=1000, globals=globals()))

# 1.0886825 old
# 0.017848900000000167 new

# 1.1709339 old
# 0.021700300000000006 new

# 1.1624405 old
# 0.019158699999999973 new
