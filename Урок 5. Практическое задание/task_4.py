"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import timeit
import collections
import random
import string


def generate_dict_items(key_length: int, items_total: int) -> list:
    items = []
    for x in range(items_total):
        key = "".join(random.choice(string.ascii_letters) for _ in range(key_length))
        value = random.randint(0, 100000000)
        items.append((key, value))
    return items

def order_dict_generation(items: list):
    _dict = collections.OrderedDict(items)

def dict_generation(items: list):
    _dict = {*items}

def update_dict(new_dict: dict, items: list):
    new_dict.update({*items})

def get_dict_item(_dict: dict, item_key: any) -> any:
    return _dict[item_key]


if __name__ == "__main__":
    print("Создание словарей:")
    items_to_dict = generate_dict_items(6, 100)
    print(f'order_dict: {timeit("order_dict_generation(items_to_dict)", globals=globals())} s')
    print(f'dict: {timeit("dict_generation(items_to_dict)", globals=globals())} s')
    """
    Создание словарей, замер на number=1000000
        order_dict: 12.011956000000001 s
        dict: 2.9701614999999997 s
    Вывод:
        создание обычного словаря требует меньше времени 
    """
    my_dict = {}
    order_dict = collections.OrderedDict()
    print("обновление элементов")
    for variable in (my_dict, order_dict):
        print(f'%s: {timeit("update_dict(variable ,items_to_dict)", globals=globals())} s' % type(variable))
    """
    Обновление словарей, замер на number=1000000
        <class 'dict'>: 6.1320532 s
        <class 'collections.OrderedDict'>: 12.251461599999999 s
    Вывод:
        Обновление OrderedDict происходит в 2 раза медленее
    """

    print("Получение значений из словаря")
    print("кортеж для тестирования ", items_to_dict[1])
    item_key = items_to_dict[1][0]
    for variable in (my_dict, order_dict):
        print(f'%s: {timeit("get_dict_item(variable ,item_key)", globals=globals(), number=10000000)} s' % type(variable))
    """
    Получение значений по ключу, замер на number=10000000
        <class 'dict'>: 1.314293799999998 s
        <class 'collections.OrderedDict'>: 1.3141349000000027 s
    Вывод:
        Впринципе, получение значения в обоих случаях происходит в среднем с одинаковой скоростью 
    """

    """ В Python 3.6 и более поздних версиях особого смысла использовать OrderedDict нет, только если он идеально 
    вписывается в специфику задачи. Так как обычный словарь не учитывает порядок елементов при сравнении, то в такой 
    задаче OrderedDict впишится идеально. В коде на уровне соглашения можно понять что важен порядок элементов с помощью 
    OrderedDict """

