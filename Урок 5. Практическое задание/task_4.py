"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit
from random import randint

usual_dict = {}
order_dict = OrderedDict()

filing_data = [(''.join([chr(randint(97, 122)) for _ in range(3)]), i) for i in range(20)]

# 1. Заполнение элементами
def fill_dict(dct):
    for k, v in filing_data:
        dct[k] = v


# 2. Проверка упорядочности
def check_orderly():
    return f"Совпадение порядка ключей: {list(usual_dict.keys()) == list(order_dict.keys())}"


# 3. Получение элементов
def get_elem(dct):
    for k, v in filing_data:
        x = dct[k]


# 4. Удаление элементов
def del_elem(dct):
    obj = dct.copy()  # Работаем с копией
    for k, v in filing_data:
        obj.pop(k)


if __name__ == '__main__':
    NUMBER = 10_000
    print(timeit('fill_dict(usual_dict)', globals=globals(), number=NUMBER))
    print(timeit('fill_dict(order_dict)', globals=globals(), number=NUMBER))

    print(check_orderly())

    print(timeit('get_elem(usual_dict)', globals=globals(), number=NUMBER))
    print(timeit('get_elem(order_dict)', globals=globals(), number=NUMBER))

    print(timeit('del_elem(usual_dict)', globals=globals(), number=NUMBER))
    print(timeit('del_elem(order_dict)', globals=globals(), number=NUMBER))

    """
    - Заполнение обычного словаря происходит быстрей, чем упорядоченного
        0.02254360999995697 - обычный словарь (20 пар ключ: значение, 10_000 запусков)
        0.07385588999932224 - OrderedDict (20 пар ключ: значение, 10_000 запусков)
    - Порядок ключей совпадает
    - Получение элементов по ключу в обычном словаре в большинстве случаях медленней
        0.01770521300022665 - обычный словарь
        0.01296174399976735 - OrderedDict
    - Удаление элементов по ключу в обычном словаре выполняется быстрей, чем в OrderedDict
        0.022947413000110828 - обычный словарь
        0.04811240299932251 - OrderedDict
    Итог: Так как порядок ключей в обычном словаре сохраняется в версии Python 3.6 и выше, и времена полученные 
    замерами лучше чем у OrderedDict, использование OrderedDict не имеет смысла
    """
