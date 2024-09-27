from collections import OrderedDict

# порядок
NEW_DICT = {'a': 1, 'b': 2, 'c': 3}
print(NEW_DICT)  # -> {'a': 1, 'b': 2, 'c': 3}
NEW_DICT = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)  # -> OrderedDict([('a', 1), ('b', 2), ('c', 3)])
