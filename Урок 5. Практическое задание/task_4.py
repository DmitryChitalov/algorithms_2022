"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

Creating dictionaries :
 DICT_append() > 1.8616221 sec
 ODICT_append() > 2.1606764000000003 sec        OrderedDICT   создается дольше чем  DICT

 DICT_MvToEnd()  > 0.12051839999999991 sec
 ODICT_MvToEnd() > 0.057773000000000074 sec
                                                    MvToEnd   для OrderedDICT быстрее чем для DICT


 Для операций popitem_last и popitem_first замеры timeit производились для
 клличества повторений number = 20, иначе словари быстро исчерпывались

 DICT_pop_last()  > 1.1399999999994748e-05 sec
 ODICT_popitem_last() > 4.200000000231796e-06 sec
                                                     popitem_last()  для OrderedDICT быстрее чем для DICT

 DICT_pop_first()  > 8.19999999990273e-06 sec
 ODICT_popitem_first() > 2.7999999998584713e-06 sec
                                                    popitem_first ()  для OrderedDICT быстрее чем для DICT

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях

Вывод:
Если в коде необходимы операции над словарем типа
move_to_end , popitem(last=True), popitem(last=False) , то
в Python 3.6 и более поздних версиях есть смысл использовать OrderedDict .
"""

from collections import OrderedDict
from timeit import timeit


def dict_append(inp_dict):
    inp_text = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. " \
               "Ab nam voluptate alias accusamus explicabo doloribus quis id quisquam, " \
               "cum culpa necessitatibus provident omnis iste eum " \
               "aspernatur nulla molestiae autem assumenda."
    for i, v in enumerate(inp_text.split()):
        inp_dict[i] = v
    return inp_dict

def dict_move_to_end(inp_dict,my_key):
    if my_key not in inp_dict:
        raise ValueError
    val = inp_dict[my_key]
    del inp_dict[my_key]
    inp_dict[my_key] = val
    return inp_dict

def dict_pop(inp_dict, last = True):

    if not last :
        k = list(inp_dict)[0]  # first key
    else:
        #   print(list(inp_dict.keys()))
        k = list(inp_dict.keys())[-1]  # last key
    v = inp_dict.pop(k)
    return (k, v)



NEW_DICT = {}
NEW_ODICT = OrderedDict()
dict_append(NEW_DICT)
dict_append(NEW_ODICT)

print("\n Creating dictionaries : ")
print(f' DICT_append() > {timeit("dict_append(NEW_DICT)", globals=globals())} sec')
print(f' ODICT_append() > {timeit("dict_append(NEW_ODICT)", globals=globals())} sec')
print('\n  Dictionaries:  ')
print(NEW_DICT)
print(NEW_ODICT)
print('')
print(f' DICT_MvToEnd()  > {timeit("dict_move_to_end(NEW_DICT,2)", globals=globals())} sec')
print(f' ODICT_MvToEnd() > {timeit("NEW_ODICT.move_to_end(2, last=True)", globals=globals())} sec')

NEW_DICT = {}
NEW_ODICT = OrderedDict()
dict_append(NEW_DICT)
dict_append(NEW_ODICT)
print(f' DICT_pop_last()  > {timeit("dict_pop(NEW_DICT, last=True)", globals=globals(), number=20)} sec')
print(f' ODICT_popitem_last() > {timeit("NEW_ODICT.popitem(last=True)", globals=globals(), number=20)} sec')

NEW_DICT = {}
NEW_ODICT = OrderedDict()
dict_append(NEW_DICT)
dict_append(NEW_ODICT)
print(f' DICT_pop_first()  > {timeit("dict_pop(NEW_DICT, last=False)", globals=globals(), number=20)} sec')
print(f' ODICT_popitem_first() > {timeit("NEW_ODICT.popitem(last=False)", globals=globals(), number=20)} sec')

# Script Listing:
#  Creating dictionaries :
#  DICT_append() > 1.8616221 sec
#  ODICT_append() > 2.1606764000000003 sec
#
#   Dictionaries:
# {0: 'Lorem', 1: 'ipsum', 2: 'dolor,', 3: 'sit', 4: 'amet', 5: 'consectetur', 6: 'adipisicing', 7: 'elit.', 8: 'Ab', 9: 'nam', 10: 'voluptate', 11: 'alias', 12: 'accusamus', 13: 'explicabo', 14: 'doloribus', 15: 'quis', 16: 'id', 17: 'quisquam,', 18: 'cum', 19: 'culpa', 20: 'necessitatibus', 21: 'provident', 22: 'omnis', 23: 'iste', 24: 'eum', 25: 'aspernatur', 26: 'nulla', 27: 'molestiae', 28: 'autem', 29: 'assumenda.'}
# OrderedDict([(0, 'Lorem'), (1, 'ipsum'), (2, 'dolor,'), (3, 'sit'), (4, 'amet'), (5, 'consectetur'), (6, 'adipisicing'), (7, 'elit.'), (8, 'Ab'), (9, 'nam'), (10, 'voluptate'), (11, 'alias'), (12, 'accusamus'), (13, 'explicabo'), (14, 'doloribus'), (15, 'quis'), (16, 'id'), (17, 'quisquam,'), (18, 'cum'), (19, 'culpa'), (20, 'necessitatibus'), (21, 'provident'), (22, 'omnis'), (23, 'iste'), (24, 'eum'), (25, 'aspernatur'), (26, 'nulla'), (27, 'molestiae'), (28, 'autem'), (29, 'assumenda.')])
#
#  DICT_MvToEnd()  > 0.12051839999999991 sec
#  ODICT_MvToEnd() > 0.057773000000000074 sec
#  DICT_pop_last()  > 1.1399999999994748e-05 sec
#  ODICT_popitem_last() > 4.200000000231796e-06 sec
#  DICT_pop_first()  > 8.19999999990273e-06 sec
#  ODICT_popitem_first() > 2.7999999998584713e-06 sec
#
# Process finished with exit code 0
