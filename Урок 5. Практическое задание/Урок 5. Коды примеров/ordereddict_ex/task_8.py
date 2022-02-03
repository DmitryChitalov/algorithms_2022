"""Класс collections.OrderedDict()"""

from collections import OrderedDict

NEW_DICT = {'a': 1, 'b': 2, 'c': 3}  # -> с версии 3.6 порядок сохранится
print(NEW_DICT)  # -> {'a': 1, 'b': 2, 'c': 3}

# а в версии 3.5 и более ранних можно было получить и такой результат
# {'b': 2, 'c': 3, 'a': 1}
# и вообще любой, ведь порядок ключей не сохранялся

# поэтому приходилось при необходимости обращаться к OrderedDict
NEW_DICT = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT['a'])  # -> OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# {} vs OrderedDict ??
# csv

"""
v,d,s
1,1,1
1,2,3
1,2,3
"""
