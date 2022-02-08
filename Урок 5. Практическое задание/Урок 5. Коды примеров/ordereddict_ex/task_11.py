from collections import OrderedDict

# специальные возможности
NEW_DICT = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

NEW_DICT_0 = OrderedDict(a=1, b=2, c=3, d=4)
NEW_DICT_1 = OrderedDict(b=2, a=1, c=3, d=4)
NEW_DICT_2 = OrderedDict(a=1, b=2, c=3, d=4)

print(NEW_DICT_0 == NEW_DICT_1)  # False
print(NEW_DICT_0 == NEW_DICT_2)  # True

NEW_DICT_0 = dict(a=1, b=2, c=3, d=4)
NEW_DICT_1 = dict(b=2, a=1, c=3, d=4)
NEW_DICT_2 = dict(a=1, b=2, c=3, d=4)

print(NEW_DICT_0 == NEW_DICT_1)  # True
print(NEW_DICT_0 == NEW_DICT_2)  # True
print(NEW_DICT_0 == NEW_DICT_1 == NEW_DICT_2)  # True

NEW_DICT_0 = OrderedDict(a=1, b=2, c=3, d=4)
NEW_DICT_1 = dict(b=2, a=1, c=3, d=4)

print(NEW_DICT_0 == NEW_DICT_1)  # True
