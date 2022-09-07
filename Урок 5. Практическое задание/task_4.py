"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
#  Обычный словарь dict был разработан для быстрых операций добавления, извлечения и обновления данных.
#  Начиная с версии 3.6 словари помнят порядок добавления элементов.
#  Спецификация Python 3.7 подтверждает, что встроенные словари упорядочены.
#  Это делает классы dict и ordereddict фактически одинаковыми.
#  Упорядоченные словари сохраняют свою актуальность.
#  - В случае с ordereddict явно указывается, что важен именно порядок следования элементов.
#  - Oy был разработан для частыx операций переупорядочивания.
#  Позволяет быстро удлить и возвротить элемент.
#  У обычного словаря такой оперативности при переупорядочивании нет,
#  поскольку потребуется время на удаление и повторную установку элемента.
#  У ordereddict существует специальный метод .popitem().
#  У OrderedDict есть метод .move_to_end() для эффективного перемещения элемента в конечную точку.
#  До Python 3.8 в обычных словарях dict отсутствовал метод __reversed__().
#  for key in reversed(numbers) в ordereddict cлужит для
#  перебора различных элементов упорядоченного словаря в обратном порядке.
#  - Позволяет проверить словари на эквивалентность (равенство), если важен именно порядок элементов.
#  Таким образом, OrderedDict проигрывает по скорости практически по всем операциям обычному dict,
#  если версия python позволяет, и нужные функции есть в dict, то OrderedDict лучше не использовать.
from collections import OrderedDict
from timeit import timeit

MY_DICT = {'1': 1, '2': 2, '3': 3}
MY_ORD_DICT = OrderedDict([('1', 1), ('2', 2), ('3', 3)])


def el_in_dic(dic_obj={}):
    for i in (range(100)):
        dic_obj[i] = i
    return dic_obj


def el_in_ord_dic(ord_dic_obj=OrderedDict([])):
    for i in (range(100)):
        ord_dic_obj[i] = i
    return ord_dic_obj


def el_out_dic(dic_obj={}):
    dic_obj_сopy = dic_obj.copy()
    for key in dic_obj_сopy:
        del dic_obj[key]
    return dic_obj


def el_out_ord_dic(ord_dic_obj=OrderedDict([])):
    ord_dic_obj_copy = ord_dic_obj.copy()
    for key in ord_dic_obj_copy:
        del ord_dic_obj[key]
    return ord_dic_obj


def move_to_end_dic_alg(dic_obj={}):
    k = 0
    for key in dic_obj:
        if k == 0:
            k += 1
            move_key = key
    del dic_obj[move_key]
    dic_obj[move_key] = move_key
    return dic_obj


def move_to_end_ord_dic_alg(ord_dic_obj=OrderedDict([])):
    k = 0
    for key in ord_dic_obj:
        if k == 0:
            k += 1
            move_key = key
    ord_dic_obj.move_to_end(move_key, last=True)
    return ord_dic_obj


def move_to_end_dic_1(dic_obj={}):
    del dic_obj[1]
    dic_obj[1] = 1
    return dic_obj


def move_to_end_ord_dic_1(ord_dic_obj=OrderedDict([])):
    ord_dic_obj.move_to_end(1, last=True)
    return ord_dic_obj


def popitem_dic_key(dic_obj={}):  # аналога popitem(last=False) для dict нет, прпробуем алгоритм.
    new_dic_obj = {0: dic_obj[0]}
    del dic_obj[0]
    return new_dic_obj


def popitem_dic_last_key(dic_obj={}):
    new_dic_obj = {99: dic_obj[99]}
    del dic_obj[99]
    return new_dic_obj


def popitem_dic(dic_obj={}):
    return dic_obj.popitem()


def popitem_ord_dic(ord_dic_obj=OrderedDict([])):
    return ord_dic_obj.popitem(last=False)


def popitem_ord_dic_last(ord_dic_obj=OrderedDict([])):
    return ord_dic_obj.popitem(last=True)


print(f'el_in_dic(): {timeit("el_in_dic(dic_obj={})", number=1, globals=globals())}')
print(f'el_in_ord_dic(): {timeit("el_in_ord_dic(ord_dic_obj=OrderedDict([]))", number=1, globals=globals())}')
#  ordereddict заполняется практически в полтора раза медленее, чем dict.
MY_DICT = el_in_dic()
MY_ORD_DICT = el_in_ord_dic()
print(f'el_out_dic(): {timeit("el_out_dic(dic_obj=MY_DICT)", number=1, globals=globals())}')
print(f'el_out_ord_dic(): {timeit("el_out_ord_dic(ord_dic_obj=MY_ORD_DICT)", number=1, globals=globals())}')
#  Из ordereddict элементы удаляются практически в 2 раза медленее, чем из dict.
#  Удатение м вставка в словарь dict практически одинаковы по скорости.
#  Удаление из ordereddict в полтора раза медленее, чем вставка в него.
MY_DICT = el_in_dic()
MY_ORD_DICT = el_in_ord_dic()
print(f'move_to_end_dic_alg(): {timeit("move_to_end_dic_alg(dic_obj=MY_DICT)", globals=globals())}')
print(
    f'move_to_end_ord_dic_alg(): {timeit("move_to_end_ord_dic_alg(ord_dic_obj=MY_ORD_DICT)", globals=globals())}')
#  Перемещение элемента в конец словаря в одинаковых алгоритмах медленее в ordereddict примерно на 20%.
print(f'move_to_end_dic_1(): {timeit("move_to_end_dic_1(dic_obj=MY_DICT)", number=1, globals=globals())}')
print(
    f'move_to_end_ord_dic_1(): {timeit("move_to_end_ord_dic_1(ord_dic_obj=MY_ORD_DICT)", number=1, globals=globals())}')
#  При одиночном замере перемещение элемента в ordereddict и dict сравнимо по скорости,
#  в ordereddict иногда чуть быстрее, иногда медленее.
print(f'popitem_dic_key(): {timeit("popitem_dic_key(dic_obj=MY_DICT)", number=1, globals=globals())}')
print(f'popitem_dic_last_key(): {timeit("popitem_dic_last_key(dic_obj=MY_DICT)", number=1, globals=globals())}')
#  Удаление разных элементов словаря dict сравнимо по скорости (скорость практически одинаковая).
MY_DICT = el_in_dic()
MY_ORD_DICT = el_in_ord_dic()
print(f'popitem_dic(): {timeit("popitem_dic(dic_obj=MY_DICT)", number=1, globals=globals())}')
print(f'popitem_ord_dic(): {timeit("popitem_ord_dic(ord_dic_obj=MY_ORD_DICT)", number=1, globals=globals())}')
MY_ORD_DICT = el_in_ord_dic()
print(f'popitem_ord_dic_last(): {timeit("popitem_ord_dic_last(ord_dic_obj=MY_ORD_DICT)", number=1, globals=globals())}')
#  Удаление элементов из конца с помощью команды popitem в ordereddict
#  быстрее почти в 2 раза, чем из его начала.
#  Удаление элемента из ordereddict с помощью popitem из конца медленее,
#  чем из dict с помощью алгоритма по ключу, примерно в 1,5 раза. Из начала - примерно в 3 раза.
#  При удаление с помощью команды popitem скорости срвнимы(одинаковы),
#  иногда чуть-чуть медленее удаление из dict, иногда из ordereddict.
#  Для popitem(last=False) в dict аналога нет.
#  Удаление первого элемента по ключу удаление быстрее в dict.
