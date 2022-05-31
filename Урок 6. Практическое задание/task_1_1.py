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

Это файл для первого скрипта
"""

"""
скрипт из курса основ. Задание  - создать класс реализующий сложение матриц
"""

from pympler import asizeof


class ErrorDimension(BaseException):
    pass


class Matrix:

    def __init__(self, list_matrix):
        self.matrix = list_matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.matrix])

    def __add__(self, other):
        result_matrix = []
        if len(self.matrix) == len(other.matrix):
            for line1, line2 in zip(self.matrix, other.matrix):
                if len(line1) != len(line2):
                    raise ErrorDimension(f'Различное количество колонок в матрицах')
                result_matrix.append([x + y for x, y in zip(line1, line2)])
        else:
            raise ErrorDimension(f'Различное количество строк в матрицах')
        return Matrix(result_matrix)


# Оптимизируем с помощью слотов


class Matrix_new:

    __slots__ = ('matrix')

    def __init__(self, list_matrix):
        self.matrix = list_matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.matrix])

    def __add__(self, other):
        result_matrix = []
        if len(self.matrix) == len(other.matrix):
            for line1, line2 in zip(self.matrix, other.matrix):
                if len(line1) != len(line2):
                    raise ErrorDimension(f'Различное количество колонок в матрицах')
                result_matrix.append([x + y for x, y in zip(line1, line2)])
        else:
            raise ErrorDimension(f'Различное количество строк в матрицах')
        return Matrix(result_matrix)


if __name__ == '__main__':
    obj_matrix = Matrix([[1, 2], [3, 4]])
    print(asizeof.asizeof((obj_matrix)))  # 552

    obj_matrix_new = Matrix_new([[1, 2], [3, 4]])
    print(asizeof.asizeof((obj_matrix_new)))  # 40
"""
Оптимизация выполнена с использованием слотов в классе. Это позволяет хранить атрибуты класса в слотах а не в словаре
Использование слотов уменьшает потребляемую память у увеличивает скорость доступа к атрибутам
"""
