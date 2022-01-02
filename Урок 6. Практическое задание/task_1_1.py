"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

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

Это файл для первого скрипта
"""

'''
Курс основ, урок 10, задание 1.

Пробуем применить оптимизацию слотами. 

Результаты и выводы:

1 тест - несколько больших матриц:
До:    111     45.0 MiB      0.0 MiB           1       return True
После: 108     45.1 MiB      0.0 MiB           1       return True

2 тест - много маленьких матриц:
До:    122     27.6 MiB      0.0 MiB           1       return True
После: 122     26.8 MiB      0.0 MiB           1       return True    
    
Оптимизация по памяти слотами даст максимальный эффект, когда в объектах много свойств и создается много экземпляров.
 
'''

from copy import deepcopy
from memory_profiler import profile


class Matrix:
    # __slots__ = ['_data']
    def __init__(self, init_list):
        self._data = init_list

    def __str__(self):
        if not self.get_data():
            return ''

        max_len = len(str(max(max(self.get_data()))))
        result = ''
        for i in self.get_data():
            for j in i:
                result += str(j).rjust(max_len, ' ') + ' '
            result += '\n'
        return result

    def __add__(self, other):
        if not self == other:
            raise TypeError('matrix must be equal.')

        self_data = self.get_data()
        other_data = other.get_data()

        result = deepcopy(self_data)
        for i in range(len(self_data)):
            for j in range(len(self_data[i])):
                result[i][j] += other_data[i][j]

        return Matrix(result)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        self_data = self.get_data()
        other_data = other.get_data()

        if len(self_data) != len(other_data):
            return False

        for i in range(len(self_data)):
            if len(self_data[i]) != len(other_data[i]):
                return False

        return True

    def get_data(self):
        return self._data


@profile
def matrix_operation():
    matrix_lst = []
    for i in range(10000):
        matrix_lst.append(Matrix([[i for i in range(10)], [i for i in range(10)], [i for i in range(10)]]))

    matrix_lst.append(0)

    # matrix1 = Matrix([[i for i in range(100000)], [i for i in range(100000)], [i for i in range(100000)]])
    # matrix2 = Matrix([[i for i in range(100000)], [i for i in range(100000)], [i for i in range(100000)]])
    # # matrix3 = Matrix([[2, 2, 2], [2, 2, 2], [1, 1]])
    #
    # print('matrix1:\n', matrix1, sep='')
    # print('matrix2:\n', matrix2, sep='')
    # print('matrix1 == matrix2\n', matrix1 == matrix2, sep='')
    # print('matrix1 + matrix2 + matrix2\n', matrix1 + matrix2 + matrix2, sep='')
    # print('matrix1:\n', matrix1, sep='')
    # print('matrix2:\n', matrix2, sep='')
    # # print('matrix1 + matrix3\n', matrix1 + matrix3, sep='')

    return True

if __name__ == "__main__":
    matrix_operation()
