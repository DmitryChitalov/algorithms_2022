"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
import time

def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print((time.perf_counter() - start_time)*1000)
        return res
    return wrapped


from collections import OrderedDict

@time_of_function
def g():
    prices = OrderedDict([("apple", 10), ("orange", 12), ("banana", 13)])
    for k, v in prices.items():
        prices[k] = round(v * 0.9, 2)
    return prices

print(g())


@time_of_function
def g1():
    prices  = {"apple": 10, "orange": 12, "banana": 13}
    for k, v in prices.items():
        prices[k] = round(v * 0.9, 2)
    return prices
print(g1())

"""
Начиная с версии Python3.7 словари стали упорядоченными.
В ранних версиях Python при запуске программы, порядок ключей словаря мог меняться.
Соответственно время поиска в неупорядоченном словаре было не предсказуемо до упорядочивания.
"""