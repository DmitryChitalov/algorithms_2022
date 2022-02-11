"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from timeit import timeit
from collections import OrderedDict

test_dict = {}
test_od = OrderedDict()


def dict_generate():
    for i in range(1, 1000):
        test_dict[i] = str(i)


def orderdict_generate():
    for i in range(1, 1000):
        test_od[i] = str(i)


def dict_extraction():
    for i in test_dict:
        test = test_dict[i]


def orderdict_extraction():
    for i in test_od:
        test = test_od[i]


def dict_pop():
    for i in range(1, 1000):
        test_dict['adding'] = 'adding'
        test_dict.pop('adding')


def orderdict_pop():
    for i in range(1, 1000):
        test_od['adding'] = 'adding'
        test_od.pop('adding')

print('Скорость заполнения словаря:           ', end='')
print(timeit('dict_generate()', setup='from __main__ import dict_generate, test_dict', number=10000))
print('Скорость заполнения OrderDict:         ', end='')
print(timeit('orderdict_generate()', setup='from __main__ import orderdict_generate, test_od', number=10000))

print('Скорость получения элемента словаря:   ', end='')
print(timeit('dict_extraction()', setup='from __main__ import dict_extraction, test_dict', number=10000))
print('Скорость получения элемента OrderDict: ', end='')
print(timeit('orderdict_extraction()', setup='from __main__ import orderdict_extraction, test_od', number=10000))

print('Скорость удаление элемента словаря:    ', end='')
print(timeit('dict_pop()', setup='from __main__ import dict_pop, test_dict', number=10000))
print('Скорость удаление элемента OrderDict:  ', end='')
print(timeit('orderdict_pop()', setup='from __main__ import orderdict_pop, test_od', number=10000))



'''
По скорости выполнения обычных операций, OrderDict приемуществ не дает, даже медленее словарей.
OrderDict необходим толкько если необходим порядок последовательности данных. 
    Скорость заполнения словаря:           1.3251851999666542
    Скорость заполнения OrderDict:         1.5520581000018865
    Скорость получения элемента словаря:   0.315510600048583
    Скорость получения элемента OrderDict: 0.41518939996603876
    Скорость удаление элемента словаря:   0.9892794999759644
    Скорость удаление элемента OrderDict: 1.594444399990607
'''
