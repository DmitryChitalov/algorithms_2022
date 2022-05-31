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

from memory_profiler import memory_usage
from time import perf_counter
from numpy import array, random


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        start = perf_counter()
        res = func(*args, **kwargs)
        stop = perf_counter()
        m2 = memory_usage()
        mem_dif = m2[0] - m1[0]
        print(f'Функция {func.__name__}, выполнение заняло: {mem_dif} Mib, время выполнения: {stop - start}')
        return res

    return wrapper


class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        matrix_string = f'Матрица вида:\n'
        for el in self.matrix_list:
            matrix_string += f'|{el}|\n'
        return matrix_string

    def __add__(self, other):
        temp_list = []
        for i in range(len(self.matrix_list)):
            if range(len(self.matrix_list)) != range(len(other.matrix_list)):
                raise ValueError('В слогаемых матрицах не совпадают количество строк')
            else:
                temp_list.append([])
                for j in range(len(self.matrix_list[i])):
                    if range(len(self.matrix_list[i])) != range(len(other.matrix_list[i])):
                        raise ValueError('В слогаемых матрицах не совпадают количество столбцов')
                    else:
                        temp_list[i].append(self.matrix_list[i][j] + other.matrix_list[i][j])
        return Matrix(temp_list)


class MatrixOpt:
    __slots__ = ['matrix_list']

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        matrix_string = f'Матрица вида:\n'
        for el in self.matrix_list:
            matrix_string += f'|{el}|\n'
        return matrix_string

    def __add__(self, other):
        try:
            temp_matrix = array(self.matrix_list) + array(other.matrix_list)
        except ValueError:
            print('В слогаемых матрицах не совпадают количество строк')
        return MatrixOpt(temp_matrix)


@memory
def add_matrix(first, second):
    result = Matrix(first) + Matrix(second)
    return result


@memory
def add_matrix_opt(first, second):
    result = MatrixOpt(first) + MatrixOpt(second)
    return result


test_1 = random.random((1000, 1000))
test_2 = random.random((1000, 1000))
# some_matrix = some_matrix_1 + some_matrix_2
# some_matrix = some_matrix_3 + some_matrix_4
result_1 = add_matrix(test_1, test_2)
result_2 = add_matrix_opt(test_1, test_2)

"""
Задание из курса основ - Намисать скрипт для сложения двухмерных массивов (матриц)
Решал через ООП, оригинальный класс - Matrix
Для оптимизации использовал numpy, в нем  же и генерировал два тестовых массива 1000х1000 со случайными числами
Результаты замеров:
Функция add_matrix, выполнение заняло: 40.0 Mib, время выполнения: 1.1497300999981235
Функция add_matrix_opt, выполнение заняло: 7.63671875 Mib, время выполнения: 0.015733200001704972
Применение специализированной библиотеки numpy позволило получить значительный выйгрыш и в памяти, и в скорости 
выполнения! Такую оптимизацию я люблю!)
"""
