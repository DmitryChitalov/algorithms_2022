from pympler import asizeof


# Атрибуты объекта находятся в словаре.
# Словари требуют много памяти
class BasicClass:
    def __init__(self, param_x, param_y):
        self.param_x = param_x
        self.param_y = param_y


BC_OBJ = BasicClass(5, 6)
print(BC_OBJ.__dict__)  # {'param_x': 5, 'param_y': 6}
print(asizeof.asizeof(BC_OBJ))  # -> 328


# Оптимизация памяти: хранить информацию не в словаре, а в slots (список)
class BasicClass:
    __slots__ = ['param_x', 'param_y']

    def __init__(self, param_x, param_y):
        self.param_x = param_x
        self.param_y = param_y


BC_OBJ = BasicClass(5, 6)
print(BC_OBJ.__slots__)  # ['param_x', 'param_y']
print(type(BC_OBJ.__slots__))  # <class 'list'>
print(asizeof.asizeof(BC_OBJ))  # -> 112

'''
{'param_x': 5, 'param_y': 6}
328
['param_x', 'param_y']
<class 'list'>
112 - экономия памяти почти в 3 раза.
'''