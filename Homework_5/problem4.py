from collections import OrderedDict
from timeit import timeit

dct = {}
odt = OrderedDict()

def func_1_dct():
    return dct.setdefault(1, 2)
def func_1_odt():
    return odt.setdefault(1, 2)

def func_2_dct():
    return dct.get(1)
def func_2_odt():
    return odt.get(1)

def func_3_dct():
    return dct.values()
def func_3_odt():
    return odt.values()

def func_4_dct():
    return dct.keys()
def func_4_odt():
    return odt.keys()

def func_5_dct():
    return dct.items()
def func_5_odt():
    return odt.items()

print(timeit('func_1_dct()', number=10000000, globals=globals()) - timeit('func_1_odt()', number=10000000, globals=globals()))
print(timeit('func_2_dct()', number=10000000, globals=globals()) - timeit('func_2_odt()', number=10000000, globals=globals()))
print(timeit('func_3_dct()', number=10000000, globals=globals()) - timeit('func_3_odt()', number=10000000, globals=globals()))
print(timeit('func_4_dct()', number=10000000, globals=globals()) - timeit('func_4_odt()', number=10000000, globals=globals()))
print(timeit('func_5_dct()', number=10000000, globals=globals()) - timeit('func_5_odt()', number=10000000, globals=globals()))

# В установлении значения OrdDict определённо быстрее,
# но медленнее в получении значения по ключу и в выведении самих ключей,
# а так как обращение по ключам - большая часть работы, нежели установка связок ключ - значение,
# то лучше пользоваться обычным словарём после версии 3.6