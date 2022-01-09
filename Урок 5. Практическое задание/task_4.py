"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import default_timer
# обеспечивает наилучшие способ, доступный на моей платформе и версии Python
from collections import OrderedDict

reg_dict = {}
order_dict = OrderedDict()
n = 10 ** 6


def timer(my_func):

    def wrapper(*args, **kwargs):
        start = default_timer()
        result = my_func(*args, **kwargs)
        print(f'Общее время выполнения функции {my_func.__name__} '
              f'составило {default_timer() - start}. ')

        return result

    return wrapper


@timer
def test_reg_dict(reg_dict, n):
    for i in range(n):
        reg_dict[i] = i


@timer
def test_order_dict(order_dict, n):
    for i in range(n):
        order_dict[i] = i


test_reg_dict(reg_dict, n)
test_order_dict(order_dict, n)

# Общее время выполнения функции test_reg_dict составило 0.0781093.
# Общее время выполнения функции test_order_dict составило 0.11969260000000001.


""" Встроенный словарь работает быстрее, чем упорядоченный словарь. 
так как при разработке OrderedDict вопросы об эффективности использования памяти, скорости итерирования,
быстродействия операций обновления были отодвинуты на второй план. На первом месте — операции, 
связанные с переопределением порядка. Поэтому упорядоченные словари выигрывают в сценариях
с частым переупорядочиванием элементов, подобных LRU-кешу.

"""


@timer
def change_reg_dict(reg_dict):
    for i in range(10*6):
        reg_dict.pop(i)
    for j in range(1000001, 2000002):
        reg_dict[j] = 'change'
    for k, v in reg_dict.items():
        reg_dict[k] = 'change value'


@timer
def change_order_dict(order_dict):
    for i in range(10*6):
        order_dict.pop(i)  # удаляем 1000000 ключей из OrderedDict"
    for j in range(1000001, 2000002):
        order_dict[j] = 'change'  # изменяем 1000000 значений в OrderedDict"
    for k, v in order_dict.items():
        order_dict[k] = 'change value'  # итерируемся по OrderedDict, изменяя значения


change_reg_dict(reg_dict)
change_order_dict(order_dict)

# Общее время выполнения функции change_dict составило 0.16523279999999999.
# Общее время выполнения функции change_ordered_dict составило 0.2982302.

"""
Встроенный словарь работает в два раза быстрее, чем упорядоченный словарь. 
OrderedDict был разработан до появления поддержки запоминания порядка добавления 
значений в обычном словаре. В настоящее время  использование OrderedDict необходимо, 
если требуется использовать  move_to_end(key, last=True), popitem(last=True).
"""