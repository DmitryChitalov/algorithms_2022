"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
import time

# декоратор для замеров времени
def time_measurement(func):
    def wrapper(arg1):
        start_time = time.time()
        c = func(arg1)
        print(f'{func.__name__} : {(time.time() - start_time)} seconds')
        return c
    return wrapper

new_dict = {}
new_ordict = OrderedDict()

# Наполним наши словари

@time_measurement
def filling(a):
    for i in range(10000):
        a[i] = i
    return a

x = filling(new_dict)     # filling : 0.00023603439331054688 seconds
y = filling(new_ordict)   # filling : 0.00038909912109375 seconds
# разница не заметна, хотя в моих замерах new_dict = {} чуть быстрее

@time_measurement
def removal(a):
    for i in range(len(a)):
        a.pop(i)
    return a

removal(x)
removal(y)
# разница не заметна, хотя в моих замерах new_dict = {} чуть быстрее

# есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
# Смысл есть: если используем OrderedDict, а не dict, то видно сразу,
# что важен порядок следования элементов в словаре. Определенно сообщаем,
# что код требует и полагается на порядок элементов в словаре.
# так же важно, что бы код работал на более старых версиях Python