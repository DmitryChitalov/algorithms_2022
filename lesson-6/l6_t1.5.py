from memory_profiler import profile
from timeit import timeit
import numpy as np
from sys import getsizeof

@profile
def min_el_1(obj: [list]) -> int:  # O(n**2)
    answ = obj[0]  # O(1)
    for i in obj:  # O(n)
        if i < answ:  # O(1)
            for j in obj:  # O(n)
                if i < j:  # O(1)
                    answ = i  # O(1)
    return answ  # O(1)

@profile
def min_py(obj: [list]) -> int:
    return min(obj)


my_list = np.random.randint(1, 1000000, 10 * 100)


print(min_el_1(my_list))
print(min_py(my_list))

#памяти будет задействовано меньше в момент выполнения во встроенных функций