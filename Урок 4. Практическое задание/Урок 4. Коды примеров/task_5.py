"""Еще замеры с timeit"""

import timeit

import_comp = "import random"

test_code = ''' 
def my_func(): 
    return random.uniform(10, 100)
'''

res = timeit.repeat(stmt=test_code, setup=import_comp)
print(res)

# еще вариант записи
print(timeit.repeat(test_code, import_comp))
