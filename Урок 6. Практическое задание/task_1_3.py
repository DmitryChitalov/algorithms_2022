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
from sys import getsizeof


"""
Основы Python (10 урок, 1 задание)
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы. И т.д...
"""
matrix_1 = [[2, 3], [5, 7], [8, 9]]
matrix_2 = [[45, 65, 90], [23, 34, 45], [56, 67, 78]]
matrix_3 = [[-1, 64, -8, 70], [95, 30, 54, 10]]
matrix_4 = [[12, 13], [15, 17], [18, 19]]


class Matrix:

    def __init__(self, param_1: list):
        self.param_1 = param_1

    def __str__(self):
        s = ''
        for i in self.param_1:
            s += str(i).replace('[', '|').replace(']', '|').replace(',', '') + '\n'
        return s

    def __add__(self, other):
        result = []
        if len(self.param_1) == len(other.param_1):
            if len(self.param_1[0]) == len(other.param_1[0]):
                for n in range(len(self.param_1)):
                    line = [x + y for x, y in zip(self.param_1[n], other.param_1[n])]
                    result.append(line)
        return Matrix(result)



matr_1 = Matrix(matrix_1)
matr_2 = Matrix(matrix_4)
print(matr_1 + matr_2)
print(getsizeof(matr_1))


class Matrix_1:
    __slots__ = ['param_1']

    def __init__(self, param_1: list):
        self.param_1 = param_1

    def __str__(self):
        s = ''
        for i in self.param_1:
            s += str(i).replace('[', '|').replace(']', '|').replace(',', '') + '\n'
        return s

    def __add__(self, other):
        result = []
        if len(self.param_1) == len(other.param_1):
            if len(self.param_1[0]) == len(other.param_1[0]):
                for n in range(len(self.param_1)):
                    line = [x + y for x, y in zip(self.param_1[n], other.param_1[n])]
                    result.append(line)
        return Matrix(result)


matr_3 = Matrix_1(matrix_1)
matr_4 = Matrix_1(matrix_1)
print(matr_3 + matr_4)
print(getsizeof(matr_3))

# Для оптимизации я атрибут внутри класса сохранил в список, а не в словарь (как заложено по умолчанию).
# Чтобы было видно результат, я использую функцию getsizeof(), т.к. при использовании @profile не видно изменений.