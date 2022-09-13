"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
import timeit
from collections import OrderedDict


def timer(n):
    def deco(func):
        def wrapper():
            result = 0
            for _ in range(n):
                start = timeit.default_timer()
                ret = func()
                result += timeit.default_timer() - start
            print(f"{result:.7f}", end="  ")
            return ret

        return wrapper

    return deco


@timer(100)
def dict_in():
    global dct
    for i in range(1000):
        dct[i] = str(i)


@timer(100)
def orddict_in():
    global orddct
    for i in range(1000):
        orddct[i] = str(i)


@timer(100)
def dict_out():
    global dct
    for i in range(1000):
        a = dct[i]


@timer(100)
def orddict_out():
    global orddct
    for i in range(1000):
        a = orddct[i]


@timer(1000)
def dict_keys():
    global dct
    dct.keys()


@timer(1000)
def orddict_keys():
    global orddct
    orddct.keys()


@timer(1)
def dict_del():
    global dct
    for i in range(0, 999, 2):
        del dct[i]


@timer(1)
def orddict_del():
    global orddct
    for i in range(0, 999, 2):
        del orddct[i]


dct = {}
orddct = OrderedDict()

print('Заполнение')
dict_in()
orddict_in()
print('\nПо ключу')
dict_out()
orddict_out()
print('\nКлючи')
dict_keys()
orddict_keys()
print('\nУдаление')
dict_del()
orddict_del()

"""
Судя по многочисленным запускам тайминга, OrderedDict по сравнению с обычным словарем работает
чуть медленнее, разница - в проценты. Но если смотреть на минимальные впремена, то одинаково.
У меня стоит версия Python 3.10, смысла пользоваться OrderedDict не вижу
"""
