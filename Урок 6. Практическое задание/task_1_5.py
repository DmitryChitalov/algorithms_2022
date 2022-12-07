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

Это файл для пятого скрипта
"""

from typing import List
from pympler import asizeof
import numpy as np


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        '''Проверка на то, что количество элементов в строках экземпляра объекта matrix одинаковое'''
        for i in range(len(matrix) - 1):
            if not len(self.matrix[i]) == len(self.matrix[i + 1]):
                raise ValueError('fail initialization matrix')
        '''Проверка на то, что в экземпляр объекта matrix входят только математические элементы'''
        for i in range(len(matrix)):
            for k in range(len(matrix[i])):
                if not isinstance(self.matrix[i][k], int):
                    raise ValueError('fail initialization matrix')

    def __str__(self):
        """Метод обеспечивает вывод матрицы на печать согласно заданию"""
        output = str()
        for i in range(len(self.matrix)):
            row = str()
            for k in range(len(self.matrix[i])):
                row = ' '.join([row, str(self.matrix[i][k])])
            output = output + '|' + row + ' |\n'
        return output

    def __add__(self, other):
        """Метод обеспечивает сложение матриц и возвращает объект класса Matrix"""
        sum_matrix = [
            [self.matrix[i][k] + other.matrix[i][k] for k in range(len(self.matrix[i]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(sum_matrix)


def arr_pprint(arr: np.array):
    for row in arr:
        to_print = str()
        for col in row:
            to_print = f'{to_print} {str(col)}'
        print(f'|{to_print} |')
    print('')


if __name__ == '__main__':
    print('\nСкрипт №1 д/з №10 курса "Основы Python". '
          'Сложение матриц и вывод на печать по заданной форме.\n'
          'Оптимизация за счет применения библиотеки numpy.\n')
    print('1. Исходный вариант.')
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(f'Объем памяти, занимаемый 1-й матрицей:'
          f' {round(asizeof.asizeof(first_matrix) / 1024, 5)} MiB')
    print(first_matrix)
    print(f'Объем памяти, занимаемый 2-й матрицей:'
          f' {round(asizeof.asizeof(second_matrix) / 1024, 5)} MiB')
    print(second_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(f'Объем памяти, занимаемый результатом сложения матриц:'
          f' {round(asizeof.asizeof(first_matrix + second_matrix) / 1024, 5)} MiB')
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    # fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    # print(fail_matrix)

    print('2. Оптимизированный вариант.')
    first_matrix_opt = np.array([[1, 2], [3, 4], [5, 6]])
    second_matrix_opt = np.array([[6, 5], [4, 3], [2, 1]])
    print(f'Объем памяти, занимаемый 1-й матрицей:'
          f' {round(asizeof.asizeof(first_matrix_opt) / 1024, 5)} MiB')
    arr_pprint(first_matrix_opt)
    print(f'Объем памяти, занимаемый 2-й матрицей:'
          f' {round(asizeof.asizeof(second_matrix_opt) / 1024, 5)} MiB')
    arr_pprint(second_matrix_opt)
    print(f'Объем памяти, занимаемый результатом сложения матриц:'
          f' {round(asizeof.asizeof(first_matrix_opt + second_matrix_opt) / 1024, 5)} MiB')
    arr_pprint(first_matrix_opt + second_matrix_opt)
