"""Обычный класс и класс со слотами"""

"""
Функция sys.getsizeof возвращает размер переданного ей обьекта, 
этот размер не включает в себя сложные структуры классов и т.д.

Функция pympler.asizeof - рекурсивно ищет все вложенные 
поля и элементы, и отображает общий размер обьекта
"""

from pympler import asizeof


class BasicClass:
    def __init__(self, param_x, param_y):
        self.param_x = param_x
        self.param_y = param_y


BC_OBJ = BasicClass(5, 6)
print(asizeof.asizeof((BC_OBJ)))  # -> 344


class BasicClass:
    __slots__ = ['param_x', 'param_y']

    def __init__(self, param_x, param_y):
        self.param_x = param_x
        self.param_y = param_y


BC_OBJ = BasicClass(5, 6)
print(asizeof.asizeof(BC_OBJ))  # -> 120
