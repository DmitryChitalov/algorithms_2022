from timeit import timeit
from collections import OrderedDict

dic = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
ord_dic = OrderedDict([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')])


def dic_pop():
    dic.pop(4)
    return dic


def ord_dic_pop():
    ord_dic.pop(4)
    return ord_dic


def dic_add():
    dic.setdefault(6, 'f')
    return dic


def ord_dic_add():
    ord_dic.setdefault(6, 'f')
    return ord_dic


def dic_update():
    dic2 = {7: 'g', 8: 'h', 9: 'i'}
    dic.update(dic2)
    return dic


def ord_dic_update():
    dic2 = OrderedDict([(7, 'g'), (8, 'h'), (9, 'i')])
    ord_dic.update(dic2)
    return ord_dic


print(f'Удаление элемента по ключу из обычного словаря')
print(timeit("dic_pop", "from __main__ import dic_pop", number=10000))

print(f'Удаление элемента по ключу из упорядоченного словаря')
print(timeit("ord_dic_pop", "from __main__ import ord_dic_pop", number=10000))

print(f'Добавление ключа и значения в обычный словарь')
print(timeit("dic_add", "from __main__ import dic_add", number=10000))

print(f'Добавление ключа и значения в упорядоченный словарь')
print(timeit("ord_dic_add", "from __main__ import ord_dic_add", number=10000))

print(f'Добавление нескольких значений в обычный словарь')
print(timeit("dic_add", "from __main__ import dic_add", number=10000))

print(f'Добавление нескольких значений в упорядоченный словарь')
print(timeit("ord_dic_add", "from __main__ import ord_dic_add", number=10000))

# Аналитика показала, что в общем операции pop, setdefault, update по скорости приблизительно одинаковы для dic и OrderedDict
# Использование OrderedDict оправдано при условии если нам нужно акцентировать внимание на порядок следования элементов в словаре,
# либо если вам нужно переупорядочить элементы в словаря, используя .move_to_end(),либо если вы сравниваете словари
# на предмет их равенства и при сравнении важен порядок элементов.
