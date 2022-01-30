"""Генерация списков"""
from timeit import Timer


# итератор с конкатенацией
def test_concat():
    my_lst = []
    for i in range(1000):
        my_lst = my_lst + [i]


# итератор с функцией append
def test_cycle():
    my_lst = []
    for i in range(1000):
        my_lst.append(i)


# списковое включение
# list comprehension
def test_lst_comp():
    my_lst = [i for i in range(1000)]


# встроенная функция range
def test_range():
    my_lst = list(range(1000))


t1 = Timer(stmt="test_concat()", setup="from __main__ import test_concat")
print("list concat ", t1.timeit(number=10000000), "seconds")

t2 = Timer("test_cycle()", "from __main__ import test_cycle")
print("list append ", t2.timeit(number=1000), "seconds")

t3 = Timer("test_lst_comp()", "from __main__ import test_lst_comp")
print("list comprehension ", t3.timeit(number=1000), "seconds")

t4 = Timer("test_range()", "from __main__ import test_range")
print("list range ", t4.timeit(number=1000), "seconds")

"""
concat  1.1779784 seconds
append  0.0715625000000002 seconds
comprehension  0.033750200000000063 seconds
range  0.011227300000000273 seconds

Вы можете объяснить получение таких результатов?
"""
