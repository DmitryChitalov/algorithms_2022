"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

"""
По словам Раймонда Хеттингера, разработчика ядра Python и соавтора OrderedDict, класс был специально разработан,
чтобы упорядочивать его элементы, тогда как новая реализация dict была спроектирована так, чтобы быть компактной
и обеспечивать быструю итерацию
специфичные для порядка, которых нет в обычных диктах (например, move_to_end() и popitem(),
1.Сигнализация намерения: если вы используете OrderedDict вместо dict, тогда ваш код проясняет, что порядок элементов в
 словаре важен. Вы четко даете понять, что вашему коду нужен порядок элементов в базовом словаре или он полагается 
 на него.
2.Контроль над порядком элементов: если вам нужно переупорядочить или переупорядочить элементы в словаре,тогда вы можете
использовать .move_to_end(), а также расширенный вариант .popitem().
3.Поведение теста на равенство: если ваш код сравнивает словари на предмет равенства, и порядок элементов важен в этом
сравнении, то OrderedDict — правильный выбор.
"""
transl = [('one', 1), ('two', 2), ('three', 3)]
d, od = dict(transl), OrderedDict(transl)
# Упорядоченность сохраняют оба типа словарей и при добавлении элементов
_, _ = d.setdefault('four', 4), od.setdefault('four', 4)
print(f'{d=}')  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
print(f'{od=}')  # [('one', 1), ('two', 2), ('three', 3), ('four', 4)]

# Перенесем {'two':2} в конец словаря, а затем восстановим порядок
d.setdefault('two', d.pop('two'))  # {'one': 1, 'three': 3, 'four': 4, 'two': 2}
d.setdefault('three', d.pop('three'))  # {'one': 1, 'four': 4, 'two': 2, 'three': 3}
d.setdefault('four', d.pop('four'))  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# в OrderedDict опреаций меньше и выглядят они более очевидными с move_to_end и popitem
od.move_to_end('two')  # [('one', 1), ('three', 3), ('four', 4), ('two', 2)]
od.move_to_end('two', False)  # [('two', 2), ('one', 1), ('three', 3), ('four', 4)]
od.move_to_end('one', False)  # [('one', 1), ('two', 2), ('three', 3), ('four', 4)]

# Забрать первый элемента словаря
key = list(d.keys())[0]  # определяем ключ 1-го эл-та. key = 'one'
val1 = (key, d[key])  # ('one', 1)
d.pop(key)  # d: {'two': 2, 'three': 3, 'four': 4}
# в OrderedDict
val2 = od.popitem(False)  # val2: ('one', 1) od: [('two', 2), ('three', 3), ('four', 4)]

# И OrderedDict функция odd_keys добавления новых атрибутов к экземпляру словаря __dict__
# Например нам часто нужна функция выборки ключей с четными значениями
od.even_keys = lambda: [k for k in od.keys() if not od[k] % 2]
print(od.even_keys())  # ['two', 'four']
print(od, od.__dict__)  # [('two', 2), ('three', 3), ('four', 4)], {'even_keys': <function <lambda> at ...}

# При проверке на равенство для OrderedDict важен порядок, для dict - нет
print(d, od)  # {'two': 2, 'three': 3, 'four': 4},  [('two', 2), ('three', 3), ('four', 4)]
print(d == od)  # true
d.setdefault('two', d.pop('two'))  # изменяем порядок
print(d == od)  # True
print(od == OrderedDict(d))  # False

"""
По результатам исследования OrderedDict в Python 3.6 и более поздних версиях в определенных случаях стоит использовать.
Из-за проверки на равенство, собственных функций popitem, move_to_end, odd_keys, которые могут сущщественно облегчить
кодирование. А если бы можно было обЪединить OrderedDict и defaultdict, dict использовали бы, только тогда, когда
нужна скорость.
"""

# По словам Раймонда Хеттингера, разработчика ядра Python и соавтора OrderedDict, класс был специально разработан,
# чтобы упорядочивать его элементы, тогда как новая реализация dict была спроектирована так, чтобы быть компактной
# и обеспечивать быструю итерацию.
# Замеры ниже подтвердили слова Раймонда Хеттингера


def dict_update(n):
    d1 = {}
    [d1.update({k: val}) for k, val in zip(range(10, n + 10), range(n))]
    [d1.setdefault(k, val + 1) for k, val in d1.items()]
    return d1


def sorted_dict_update(n):
    d1 = OrderedDict()
    [d1.update({k: val}) for k, val in zip(range(10, n + 10), range(n))]
    [d1.setdefault(k, val + 1) for k, val in d1.items()]
    return d1


statements1 = [
    'dict_update(numb)', 'dict_update: ',
    'sorted_dict_update(numb)', 'sorted_dict_update: ',
    '[dict_read[k] if dict_read[k] else 0 for k in dict_read]', 'dict_read: ',
    '[sort_dict_read[k] if sort_dict_read[k] else 0 for k in sort_dict_read]', 'sort_dict_read: '
]
numb = 10
dict_read = dict_update(numb)
sort_dict_read = sorted_dict_update(numb)
[print(info, timeit(
    st,
    setup="from __main__ import dict_update, sorted_dict_update, dict_read, sort_dict_read, numb", number=10000))
 for st, info in zip(statements1[::2], statements1[1::2])]
