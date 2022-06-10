"""Замеряем время работы блоков кода"""

from timeit import timeit

print(timeit("x = 2 + 2", number=1000))
print(timeit("x = sum(range(10))"))

print(timeit("""
for i in range(3):
    y = i + 2
    a = 4
    if a == y:
        1/2
"""))

"""
0.010643799999999981
0.3782346000000001
0.40320979999999995
"""
