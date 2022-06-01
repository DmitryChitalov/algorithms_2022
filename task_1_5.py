"""
Курс: Основы языка Python
Урок: 7
Задание: 1
-----------------------------------------------------------------------------
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для
формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй
матрицы и т.д.
"""

from pympler.asizeof import asizeof
from memory_profiler import memory_usage
import numpy as np
from memory_profiler import profile

def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


##############################################################################
"""
ИСХОДНОЕ РЕШЕНИЕ

Размер отдельного объекта: 1048 байт(а)
Размер всех объектов: 2832 байт(а)
"""

class Matrix:

    def __init__(self, matrix=''):
        self.n_row = len(matrix) # число строк матрицы
        if not isinstance(matrix, list): # если входные данные не являются списком,
            self.reset() # то считаем матрицу неопределенной
        elif self.n_row == 0: # если входной список пустой,
            self.reset() # то считаем матрицу неопределенной
        else:
            self.n_col = len(matrix[0]) # число столбцов матрицы
            for l in matrix[1:]:
                if self.n_col != len(l): # если число элементов внутри вложенных списков различно,
                    self.reset() # то считаем матрицу неопределенной
                    return
                for el in l:
                    if not isinstance(el, (int, float)): # если отдельные элементы не являются числовыми,
                        self.reset() # то считаем матрицу неопределенной
                        return
            self.matrix = matrix

    def reset(self): # сброс атрибутов
        self.n_row = None
        self.n_col = None
        self.matrix = None

    def __str__(self):
        if self.matrix:
            out = f'{self.__class__.__name__} {self.n_row} x {self.n_col}:\n\t'
            for row in self.matrix:
                out += ' '.join([str(el) for el in row]) + '\n\t'
            out = out[:len(out)-1]
        else:
            out = 'Матрица не определена'
        return out

    def __add__(self, other):
        if self.n_row != other.n_row or self.n_col != other.n_col:
            matrix = ''
        else:
            matrix =[]
            for i in range(self.n_row):
                matrix.append([self.matrix[i][j] + other.matrix[i][j] for j in range(self.n_col)])
        return Matrix(matrix)


A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
C = A + B
print('---> ИСХОДНОЕ РЕШЕНИЕ')
print(f'Матрица А:\n{A}Размер объекта: {asizeof(A)} байт(а)')
print(f'Матрица B:\n{B}Размер объекта: {asizeof(B)} байт(а)')
print(f'Матрица C:\n{C}Размер объекта: {asizeof(C)} байт(а)')
print('----------------------------------')
print(f'Размер всех объектов: {asizeof(A) + asizeof(B) + asizeof(C)} байт(а)')
print('----------------------------------')

##############################################################################
"""
ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ

Описание: использовал библиотеку numpy и задавал матрицы через np.array.

Размер отдельного объекта: 184 байт(а)
Размер всех объектов: 552 байт(а)
"""


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
C = A + B
print('---> ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ')
print(f'Матрица А:\n{A}\nРазмер объекта: {asizeof(A)} байт(а)')
print(f'Матрица B:\n{B}\nРазмер объекта: {asizeof(B)} байт(а)')
print(f'Матрица C:\n{C}\nРазмер объекта: {asizeof(C)} байт(а)')
print('----------------------------------')
print(f'Размер всех объектов: {asizeof(A) + asizeof(B) + asizeof(C)} байт(а)')
print('----------------------------------')
