from random import randint
from timeit import timeit

m = int(input("Введите любое натуральное число: "))
len = 2 * m + 1
lst = [randint(0, 10) for _ in range(len)]


def my_culc(lst):
    def find_m(lst):
        i = 0
        while i != m:
            x = max(lst)
            j = lst.index(x)
            lst.pop(j)
            i += 1

    return max(lst)


lst1 = [randint(0, 10) for _ in range(len)]
print(timeit("my_culc(lst1)", globals=globals(), number=1000))

lst2 = [randint(0, 100) for _ in range(len)]
print(timeit("my_culc(lst2)", globals=globals(), number=1000))

lst3 = [randint(0, 1000) for _ in range(len)]
print(timeit("my_culc(lst3)", globals=globals(), number=1000))
