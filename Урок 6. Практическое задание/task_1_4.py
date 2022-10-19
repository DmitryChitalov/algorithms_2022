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

Это файл для четвертого скрипта
"""

# Урок 10 задание 1
# Реализовать класс Matrix (матрица)
from pympler import asizeof


class Matrix:
    def __init__(self, matrix):
        lst_length = []
        for el in range(len(matrix)):
            lst_length.append(len(matrix[el]))
        if len(set(lst_length)) == 1:
            self.matrix = matrix
        else:
            raise ValueError("Incorrect data for Matrix initialization: not equal lenght of lists")

    def __str__(self):
        matrix = ''
        for el in self.matrix:
            matrix += '| '
            for i in el:
                matrix += '{:>3}'.format(i)
            matrix += ' |\n'
        return matrix

    def __add__(self, other):
        rez = []
        for i in range(len(self.matrix)):
            rez1 = []
            if len(self.matrix) == len(other.matrix):
                for el in range(len(self.matrix[i])):
                    if len(self.matrix[i]) == len(other.matrix[i]):
                        rez1.append(self.matrix[i][el] + other.matrix[i][el])
                    else:
                        raise ValueError('Incorrect dimensions for add method')
                rez.append(rez1)
            else:
                raise ValueError('Incorrect dimensions for add method')
        return Matrix(rez)


class ModyMatrix:
    __slots__ = ['matrix']

    def __init__(self, matrix):
        lst_length = []
        for el in range(len(matrix)):
            lst_length.append(len(matrix[el]))
        if len(set(lst_length)) == 1:
            self.matrix = matrix
        else:
            raise ValueError("Incorrect data for Matrix initialization: not equal lenght of lists")

    def __str__(self):
        matrix = ''
        for el in self.matrix:
            matrix += '| '
            for i in el:
                matrix += '{:>3}'.format(i)
            matrix += ' |\n'
        return matrix

    def __add__(self, other):
        rez = []
        for i in range(len(self.matrix)):
            rez1 = []
            if len(self.matrix) == len(other.matrix):
                for el in range(len(self.matrix[i])):
                    if len(self.matrix[i]) == len(other.matrix[i]):
                        rez1.append(self.matrix[i][el] + other.matrix[i][el])
                    else:
                        raise ValueError('Incorrect dimensions for add method')
                rez.append(rez1)
            else:
                raise ValueError('Incorrect dimensions for add method')
        return Matrix(rez)


if __name__ == '__main__':
    m1 = Matrix([[11, 2, 3], [4, 5, 6], [117, 8, 9]])
    print(asizeof.asizeof(m1))
    m2 = ModyMatrix([[11, 2, 3], [4, 5, 6], [117, 8, 9]])
    print(asizeof.asizeof(m2))
