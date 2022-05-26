"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit


def dict_gen(n=1000):
    return {n: n for n in range(n)}


def get_dict_el(user_dict, n=100):
    for i in range(n):
        user_dict[i]


def del_dict_el(user_dict, n=1):
    user_dict.popitem()


def get_keys(user_dict):
    user_dict.keys()


def get_items(user_dict):
    user_dict.items()


def dict_input(user_dict, n=100000):
    for i in range(n):
        user_dict[i + 1000] = i


# Сгенерируем для экспериментов тестовые словари: обычный - test_dict, и упорядоченный - test_ord_dict
test_dict = dict_gen()
test_ord_dict = OrderedDict(dict_gen())

# Замеры создания словарей:
print('Генерация dict: ', timeit("dict_gen()", globals=globals(), number=10000))
print('Генерация ordered_dict: ', timeit("OrderedDict(dict_gen())", globals=globals(), number=10000))
# Взятие элемента по индексу:
print('Взятие элемента по индексу dict: ', timeit("get_dict_el(test_dict)", globals=globals(), number=10000))
print('Взятие элемента по индексу ordered_dict: ',
      timeit("get_dict_el(test_ord_dict)", globals=globals(), number=10000))
# Запрос ключей словаря:
print('Запрос ключей dict: ', timeit("get_keys(test_dict)", globals=globals(), number=10000))
print('Запрос ключей ordered_dict: ',
      timeit("get_keys(test_ord_dict)", globals=globals(), number=10000))
# Запрос пар ключ, значение:
print('Запрос пар ключ, значени dict: ', timeit("get_items(test_dict)", globals=globals(), number=10000))
print('Запрос пар ключ, значени ordered_dict: ',
      timeit("get_items(test_ord_dict)", globals=globals(), number=10000))
# Добавление 100000 новых элементов в словарь :
print('Добавление 100000 новых элементов в dict: ', timeit("dict_input(test_dict)", globals=globals(), number=1))
print('Добавление 100000 новых элементов в ordered_dict: ',
      timeit("dict_input(test_ord_dict)", globals=globals(), number=1))
# Удаление элемента:
print('Удаление элемента dict: ', timeit("del_dict_el(test_dict)", globals=globals(), number=1000))
print('Удаление элемента ordered_dict: ',
      timeit("del_dict_el(test_ord_dict)", globals=globals(), number=1000))

"""
Итого, мои результаты:
Генерация dict:  0.39390049999929033
Генерация ordered_dict:  1.2808024999976624
Взятие элемента по индексу dict:  0.027025400020647794
Взятие элемента по индексу ordered_dict:  0.025655800011008978
Запрос ключей dict:  0.0012146999943070114
Запрос ключей ordered_dict:  0.001207199995405972
Запрос пар ключ, значени dict:  0.001280700002098456
Запрос пар ключ, значени ordered_dict:  0.0008470999891869724
Добавление 100000 новых элементов в dict:  0.00789390000863932
Добавление 100000 новых элементов в ordered_dict:  0.012029500008793548
Удаление элемента dict:  0.00011669998639263213
Удаление элемента ordered_dict:  0.00016239998512901366
Заметную разницу по времени я вижу только в создани: упорядоченный словарь создался у меня в 3 раза медленнее...
в остальном же особой разницы как по мне невидно... Хочеться подтвердить Ваш лекционный тезиз: используем упорядоченный 
словарь когда хотим ПОДЧЕРКНУТЬ! его упорядоченность.
"""