from numpy import array
from memory_profiler import profile
import random

# поиск минимального значения для списка. дз 1_2


@profile
def list_value_1():
    val = list([random.randint(0, 1000) for i in range(100000)])
    for i in val:
        if i < val[0]:
            val.insert(0, val[val.index(i)])
    return val[0]


@profile
def list_value_2():
    val = array([random.randint(0, 1000) for i in range(100000)])
    min_value = min(val)
    return min_value


list_value_1()
list_value_2()
# использовала библиотеку Numpy, создание списка заняло меньше памяти (особенно заметно на больших объемах данных)
