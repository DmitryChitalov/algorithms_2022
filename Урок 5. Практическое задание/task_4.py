"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit


temp_1 = range(1, 27)
temp_2 = (chr(i) for i in range(ord('a'), ord('z') + 1))
my_dict = dict(zip(temp_1, temp_2))
ordered_dict = OrderedDict(my_dict)
print(f'{my_dict = }')
print(f'{ordered_dict = }')

# print(timeit('', globals=globals(), number=10000))
print('Set d[key] to value:')
print(timeit('for i in range(97, 123): my_dict[i] = chr(i)', globals=globals(), number=10000))
print(timeit('for i in range(97, 123): ordered_dict[i] = chr(i)', globals=globals(), number=10000))

print('key in dict:')
print(timeit('for i in range(97, 123): i in my_dict', globals=globals(), number=10000))
print(timeit('for i in range(97, 123): i in ordered_dict', globals=globals(), number=10000))

print('get(key, None):')
print(timeit('for i in range(97, 123): my_dict.get(i, None)', globals=globals(), number=10000))
print(timeit('for i in range(97, 123): ordered_dict.get(i, None)', globals=globals(), number=10000))

print('pop(key, None):')
print(timeit('for i in range(97, 123): my_dict.pop(i, None)', globals=globals(), number=10000))
print(timeit('for i in range(97, 123): ordered_dict.pop(i, None)', globals=globals(), number=10000))

# Все замеры в пределах погрешности, обычный словарь чуть быстрее, только pop(key) на OrderedDict
# отрабатывает значительно дольше, но заметно будет только на очень больших словарях.
# Использовать OrderedDict можно только для того, чтобы подчеркнуть, что нам важен порядок элементов.
# Например, если будем сравнивать словари и будет важно, в каком порядке они заполнялись.
