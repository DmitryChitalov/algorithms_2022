"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

# Помним проходили OrderedDict упорядочивал словарь, но так как в обновление к python c версии 3.6,
# все словари стали упорядоченными

from timeit import timeit
from collections import OrderedDict

first_dict = OrderedDict()
second_dict = dict()

print(type(first_dict))
print(type(second_dict))


# 1 Добавление
test_add_orderdict = timeit('for i in range(100): first_dict[i] = i', globals=globals(), number=10000)
test_add_dict = timeit('for i in range(100): second_dict[i] = i', globals=globals(), number=100000)
print(f'Добавление элемента в OrderedDict - {test_add_orderdict}\nДобавление элемента в Dict - {test_add_dict}')
# Добавление элемента в OrderedDict - 0.08824680000543594
# Добавление элемента в Dict - 0.6287523000501096
# Вывод: При многократных замерах orderdict и dict, видно что orderdict работает эффективней примерно в 8 раз


# 2 Удаление
def func_del_orderdict():
    for i in range(100):
        del first_dict[i]


def func_del_dict():
    for i in range(100):
        del second_dict[i]


func_del_orderdict()
func_del_dict()

test_del_orderdict = timeit('func_del_orderdict', globals=globals(), number=10000)
test_del_dict = timeit('func_del_dict', globals=globals(), number=10000)
print(f'Удаление элементов del OrderedDict - {test_del_orderdict}\nУдаление элементов del Dict - {test_del_dict}')
# Удаление элементов del OrderedDict - 0.0003154999576508999
# Удаление элементов del Dict - 0.00045640021562576294
# Вывод: При многократных замерах orderdict и dict, видно что orderdict работает эффективней

# Итог: Хоть словари стали упорядоченными с версии 3.6, ордер дикт имеет место быть за счет своей оптимизированности,
# я считаю что его использование ускоряет работу программы, лучше использовать OrderedDict вместо обычного словаря.
