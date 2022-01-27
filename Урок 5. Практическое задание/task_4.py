"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import timeit
from collections import OrderedDict

dct = {i: i for i in range(10000)}
odct = OrderedDict(dct)


def move_to_end_ODict():
    for i in range(1000):
        odct.move_to_end(i, last=True)


def move_to_end_Dict():
    for i in range(1000):
        val = dct[i]
        del dct[i]
        dct[i] = val


def move_to_start_ODict():
    for i in range(1000):
        odct.move_to_end(i, last=False)


dct = {i: i for i in range(10000)}


def move_to_start(mutable_dict, dict_key):
    temp_dict = mutable_dict.copy()
    val = mutable_dict[dict_key]
    # print(dct)
    del mutable_dict[dict_key]
    print(dct)
    mutable_dict = {dict_key: val}
    for key, val in temp_dict.items():
        if key != dict_key:
            mutable_dict[key] = val
    # print(mutable_dict)
    # return mutable_dict


# def move_to_start_Dict():
#     for i in range(1000):
#         move_to_start(dct, i)

# move_to_start(dct, 50)
# print(dct)
# print(timeit('move_to_end_ODict()', globals=globals(), number=1000),
#       timeit('move_to_end_Dict()', globals=globals(), number=1000),
#       timeit('move_to_start_ODict()', globals=globals(), number=1000),
#       )

dct = {}
odct = OrderedDict({})


def filling_Odict():
    for i in range(10000):
        odct[i] = i


def filling_dict():
    for i in range(10000):
        dct[i] = i

filling_dict()
filling_Odict()
print(timeit('filling_Odict()', globals=globals(), number=10000),
      timeit('filling_dict()', globals=globals(), number=10000))


def changing_Odict():
    for i in range(10000):
        odct[i] = 'fill'


def changing_dict():
    print(dct)
    for i in range(10000):
        dct[i] = 'fill'


print(timeit('changing_Odict()', globals=globals(), number=10000),
      timeit('changing_dict()', globals=globals(), number=10000))





"""
При выполнении операций заполнения, изменения значений обычный словарь гораздо быстрее чем ordered dict.
Python 3.6 и более поздних версиях поддерживает сохранение порядка добавления пар ключ-значение,
поэтому Ordered на данный момент можно использовать только когда нам необходимы функции move_to_end(), popitem().
"""