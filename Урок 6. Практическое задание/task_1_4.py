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

from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение {func.__name__} заняло {mem_diff} Mib")
        return res

    return wrapper


# Курс основ, урок 10, задание 1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать
# данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n '.join(['\t '.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip(*t)) for t in zip(self.matrix, other.matrix)])


cols = rows = 500


@memory
def initial_version():
    matrix_1 = Matrix([[i * j for j in range(rows)] for i in range(cols)])
    matrix_2 = Matrix([[i + j for j in range(rows)] for i in range(cols)])
    # print('Сумма матриц:\n', matrix_1 + matrix_2)


print(initial_version())


class Matrix_2:
    __slots__ = ('_matrix')

    def __init__(self, matrix):
        self._matrix = matrix

    def __str__(self):
        return str('\n '.join(['\t '.join([str(i) for i in j]) for j in self._matrix]))

    def __add__(self, other):
        return Matrix_2([map(sum, zip(*t)) for t in zip(self._matrix, other.matrix)])


@memory
def optimized_version():
    matrix_1 = Matrix_2([[i * j for j in range(rows)] for i in range(cols)])
    matrix_2 = Matrix_2([[i + j for j in range(rows)] for i in range(cols)])
    # print('Сумма матриц:\n', matrix_1 + matrix_2)


print(optimized_version())

# Выполнение initial_version заняло 1.2890625 Mib
# Выполнение optimized_version заняло 0.5117187 Mib - экономия памяти при использовании слотов


