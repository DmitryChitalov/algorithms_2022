'''
Курс: Основы Python. Задание 1
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
'''

from pympler import asizeof

# Исходное
class Matrix:

    def __init__(self, elems):
        self.elems = elems

    def __add__(self, other):
        return Matrix([map(sum, zip(*t)) for t in zip(self.elems, other.elems)])

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.elems]))


m1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
mt1 = Matrix(m1)
mt2 = Matrix(m2)
res = mt1 + mt2
print(f'{asizeof.asizeof(res)}')

# Оптимизированное
class Matrix:
    __slots__ = ('elems')

    def __init__(self, elems):
        self.elems = elems

    def __add__(self, other):
        return Matrix([map(sum, zip(*t)) for t in zip(self.elems, other.elems)])

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.elems]))


m1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
mt1 = Matrix(m1)
mt2 = Matrix(m2)
res = mt1 + mt2
print(f'{asizeof.asizeof(res)}')
'''
Исходный: 440
Со слотами: 40
Использовал слоты, объём памяти объект стал занимать меньше
'''