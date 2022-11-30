"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from collections import OrderedDict
from timeit import timeit

def get_common_dict(dct: dict) -> None:
    # Получить элементы словаря.
    for item in range(len(dct)):
        dct[item]
    return None

def get_ordered_dict(ord_dct: OrderedDict) -> None:
    # Получить элементы OrderedDict.
    for item in range(len(ord_dct)):
        ord_dct[item]
    return None

def del_common_dict(dct: dict) -> None:
    # Удалить элементы словаря.
    for item in range(len(dct)):
        del dct[item]
    return None

def del_ordered_dict(ord_dct: OrderedDict) -> None:
    # Удалить элементы OrderedDict.
    for item in range(len(ord_dct)):
        del ord_dct[item]
    return None

def ch_common_dict(dct: dict) -> None:
    # Измененить элементы словаря.
    for item in range(len(dct)):
        dct[item] = None
    return None

def ch_ordered_dict(ord_dct: OrderedDict) -> None:
    # Измененить элементы OrderedDict.
    for item in range(len(ord_dct)):
        ord_dct[item] = None
    return None


if __name__ == "__main__":
    common_dict: dict = {item: None for item in range(1000)}
    ordered_dict: OrderedDict = OrderedDict([(item, None) for item in range(1000)])
    number: int = 10000 # Количество повторений timeit.

    print("Получение элементов")
    print(f"\tдля словаря: {timeit('get_common_dict(common_dict.copy())', globals=globals(), number=number)}")
    print(f"\tдля OrderedDict: {timeit('get_ordered_dict(ordered_dict.copy())', globals=globals(), number=number)}")

    print("Удаление элементов")
    print(f"\tдля словаря: {timeit('del_common_dict(common_dict.copy())', globals=globals(), number=1)}")
    print(f"\tдля OrderedDict: {timeit('del_ordered_dict(ordered_dict.copy())', globals=globals(), number=1)}")

    print("Изменение элементов")
    print(f"\tдля словаря: {timeit('ch_common_dict(common_dict.copy())', globals=globals(), number=number)}")
    print(f"\tдля OrderedDict: {timeit('ch_ordered_dict(ordered_dict.copy())', globals=globals(), number=number)}")

"""
    Получение элементов
            для словаря: 1.9190571339568123
            для OrderedDict: 2.2897146649775095
    Удаление элементов
            для словаря: 0.0002213600091636181
            для OrderedDict: 0.0005085410084575415
    Изменение элементов
            для словаря: 1.6077475780039094
            для OrderedDict: 2.8344123909482732
"""

"""
    Скорость выполнения стандартных операций у обычного словаря выше чем у OrderedDict. 
    OrderedDict есть смысл использовать, когда важен порядок елементов добавляемых в словарь.
"""