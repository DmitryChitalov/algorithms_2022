"""Еще замеры с timeit"""
from timeit import timeit

"""
Эта команда выполнит выражение setup один раз, 
а затем возвратит время в секундах типа float, 
которое требуется что бы выполнить основное выражение number раз.
"""


def concat_test():
    my_lst = []
    for i in range(1000):
        my_lst += [i]


def append_test():
    my_lst = []
    for i in range(1000):
        my_lst.append(i)


# через строку кода
STR_CODE = '''
l = [] 
for i in range(1000): 
    l += [i]
'''

# еще через строку кода
STR_CODE_2 = '''
j = sum(range(1, 1000))
'''

print(timeit("concat_test()", setup="from __main__ import concat_test",
             number=1000))
print(timeit("append_test()", setup="from __main__ import append_test",
             number=1000))
print(timeit(STR_CODE, number=1000))
print(timeit(STR_CODE_2, number=1000))

print()

print(timeit("concat_test()", "from __main__ import concat_test", number=1000))
print(timeit("append_test()", "from __main__ import append_test", number=1000))
print(timeit(STR_CODE, number=1000))
print(timeit(STR_CODE_2, number=1000))
