"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

usual_dict = {}
ordered_dict = OrderedDict()


def usual_add():
    for k in range(1000):
        usual_dict[str(k)] = k * 100


def usual_access():
    for k in usual_dict.keys():
        acces = usual_dict[k]


def usual_change():
    for k in usual_dict.keys():
        usual_dict[k] = k


def usual_remove():
    copy = usual_dict.copy()
    for k in copy.keys():
        del usual_dict[k]


usual_add()
usual_access()
usual_change()
usual_remove()


def ordered_add():
    for k in range(1000):
        usual_dict[str(k)] = k * 100


def ordered_acces():
    for k in usual_dict.keys():
        acces = usual_dict[k]


def ordered_change():
    for k in ordered_dict.keys():
        ordered_dict[k] = k


def ordered_remove():
    copy = ordered_dict.copy()
    for k in copy.keys():
        del ordered_dict[k]


print('\nusual\n')
print('\tusual_add\n',
      timeit(
          "usual_add()",
          setup='from __main__ import usual_add',
          number=10000),
      '\n\tusual_access\n',
      timeit(
          "usual_access()",
          setup='from __main__ import usual_access',
          number=10000),
      '\n\tusual_change\n',
      timeit(
          "usual_change()",
          setup='from __main__ import usual_change',
          number=10000),
      '\n\tususal_remove\n',
      timeit(
          "usual_remove()",
          setup='from __main__ import usual_remove',
          number=10000))

ordered_add()
ordered_acces()
ordered_change()
ordered_remove()

print('\nOrdered\n')
print('\tordered_add\n',
      timeit(
          "usual_add()",
          setup='from __main__ import usual_add',
          number=10000),
      '\n\tordered_access\n',
      timeit(
          "ordered_acces()",
          setup='from __main__ import ordered_acces',
          number=10000),
      '\n\tordered_change\n',
      timeit(
          "ordered_change()",
          setup='from __main__ import ordered_change',
          number=10000),
      '\n\tordered_remove\n',
      timeit(
          "ordered_remove()",
          setup='from __main__ import ordered_remove',
          number=10000))
"""
цифры почти одинаковые только изменение в ordered dict быстрее 
по другим показателям они одинаковые
Смысл использовать есть ели нам нужно изменять порядок элементов ordered dict позволяет это делать
"""
