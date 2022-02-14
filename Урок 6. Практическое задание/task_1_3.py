"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
Это файл для третьего скрипта
"""
import numpy as np
from memory_profiler import profile

"""--------------------------------------------
1.3 Для ОПТИМИЗАЦИИ используем библиотеку NumPy
-----------------------------------------------"""


# Курс 'Основы PYTHON'
# 10.1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#        3х2:          3х3:            2х4:
#      31  22        3  5 32        3  5  8  3
#      37  43        2  4  6        8  3  7  1
#      51  86       -1 64 -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и пр.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_check()  # проверяем, что тип matrix list, все его эл-ты list и они равного размера
        self.m_rows = len(self.matrix)
        self.n_columns = len(self.matrix[0])

    def matrix_check(self):
        if type(self.matrix) is not list \
                or any(type(x) is not list for x in self.matrix) \
                or any(len(x) != len(self.matrix[0]) for x in self.matrix):
            raise ValueError('Invalid matrix')

    def get_matrix_dimension(self):
        return [self.m_rows, self.n_columns]

    def __str__(self):
        # конкатенация списков(sum) в строки (map); строка с макс. длиной(max); +2 пробела
        xx_max = len(max(list(map(str, sum(self.matrix, []))), key=len)) + 2  # длина поля для вывода значений матрицы
        s = '\n'.join([''.join([(str(i)).rjust(xx_max) for i in x]) for x in self.matrix])
        return f' матрица [{self.m_rows}x{self.n_columns}]\n{s}'

    def __add__(self, other):
        if self.get_matrix_dimension() != other.get_matrix_dimension():
            return None  # сложение матриц возможно только одной размерности
        return Matrix([[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.matrix, other.matrix)])


"""
Используем NumPy для оптимизации Класса 
"""


class MatrixNP:
    def __init__(self, data):
        self.matrix = np.array(data) if isinstance(data, list) else data

    def __add__(self, other):
        return MatrixNP(self.matrix + other.matrix)

    def __str__(self):
        return '\n'.join([str(self.matrix[i]) for i in range(len(self.matrix))])


# Проверяем, что функционал одинаковый и под комментарий
# m0 = [[0, 3, 4], [100, 200, 400], [10, 20, 30], [-20, -40, -80]]
# m1 = [[10, 11, 12], [-20, -21, -22], [100, 200, 300], [100, 200, 300]]
# print(f'Old Class:\n{Matrix(m0)}\n+\n{Matrix(m1)}\n=\n{Matrix(m0) + Matrix(m1)}')
# print(f'New Class:\n{MatrixNP(m0)}\n+\n{MatrixNP(m1)}\n=\n{MatrixNP(m0) + MatrixNP(m1)}')


@profile
def matrix_test():
    x1 = Matrix(lst)
    x2 = Matrix(lst)
    x3 = x1 + x2
    return x3


@profile
def matrix_np_test():
    x1 = MatrixNP(lst)
    x2 = MatrixNP(lst)
    x3 = x1 + x2
    return x3


rows = 1000
column = 10000
lst = [list(range(column)) for _ in range(rows)]
matrix_test()
matrix_np_test()

"""
Результаты тестов показали, что новый класс MatrixNP заметно оптимизирован по памяти с помощью использования
библиотеки NumPy, поскольку пакет специализирован на экономном потреблении памяти при обработке больших данных.

Line  Mem usage  Increment Occur  Line Contents        | Line  Mem usage  Increment Occur  Line Contents 
====================================================== | =======================================================
  94  409.8 MiB  409.8 MiB     1  @profile             |  102  413.1 MiB  413.1 MiB     1  @profile
  95                              def matrix_test():   |  103                              def matrix_np_test():
  96  409.9 MiB    0.0 MiB     1      x1 = Matrix(lst) |  104  451.3 MiB   38.1 MiB     1      x1 = MatrixNP(lst)
  97  409.9 MiB    0.0 MiB     1      x2 = Matrix(lst) |  105  489.4 MiB   38.1 MiB     1      x2 = MatrixNP(lst)
  98  797.4 MiB  387.6 MiB     1      x3 = x1 + x2     |  106  527.6 MiB   38.1 MiB     1      x3 = x1 + x2
  99  797.4 MiB    0.0 MiB     1      return x3        |  107  527.6 MiB    0.0 MiB     1      return x3
"""
