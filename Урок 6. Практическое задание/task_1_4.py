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
from pympler import asizeof

'''Задание 10.1 из основ питона. Так как задание на ООП, в качестве оптимизации попробовал использовать слоты. Замеры 
производятся с помощью asizeof из pympler. Добавляем __slots__ = ('some_list') и сопоставляем размеры: в первом 
случае имеем 1728, во втором 40. '''


# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.

# Версия до:
class Matrix:
    def __init__(self, some_list):
        self.some_list = some_list

    def __str__(self):
        for el in self.some_list:
            print('|', end=' ')
            for i in el:
                print(f'{i}', end=' ')
            print('|')
        return ''

    def __add__(self, other):

        res = self.some_list.copy()
        for i in range(len(self.some_list)):
            if len(self.some_list) != len(other.some_list):
                print(f'Ошибочка! Длины списков разные')
                exit(code=1)
            for j in range(len(self.some_list[i])):
                if len(self.some_list[i]) != len(other.some_list[i]):
                    print(f'Ошибочка! Длины списков разные')
                    exit(code=1)
                res[i][j] = self.some_list[i][j] + other.some_list[i][j]
        return res


# Версия после, оптимизированная:
class Matrix_2:
    __slots__ = ('some_list')  # здесь добавлен "слот"

    def __init__(self, some_list):
        self.some_list = some_list

    def __str__(self):
        for el in self.some_list:
            print('|', end=' ')
            for i in el:
                print(f'{i}', end=' ')
            print('|')
        return ''

    def __add__(self, other):

        res = self.some_list.copy()
        for i in range(len(self.some_list)):
            if len(self.some_list) != len(other.some_list):
                print(f'Ошибочка! Длины списков разные')
                exit(code=1)
            for j in range(len(self.some_list[i])):
                if len(self.some_list[i]) != len(other.some_list[i]):
                    print(f'Ошибочка! Длины списков разные')
                    exit(code=1)
                res[i][j] = self.some_list[i][j] + other.some_list[i][j]
        return res


a_list = [[31, 22], [37, 43], [51, 86], [3, 5, 32], [2, 4, 6], [-1, 64, -8], [3, 5, 8, 3], [8, 3, 7, 1]]
c_list = [[31, 22], [37, 43], [51, 86], [3, 5, 32], [2, 4, 6], [-1, 64, -8], [3, 5, 8, 3], [8, 3, 7, 1]]
b = Matrix(a_list)
d = Matrix(c_list)
result_list = b + d
result = Matrix(result_list)
print(asizeof.asizeof(result))  # => результат до оптимизации: размер 1728
print(result)
a_list = [[31, 22], [37, 43], [51, 86], [3, 5, 32], [2, 4, 6], [-1, 64, -8], [3, 5, 8, 3], [8, 3, 7, 1]]
c_list = [[31, 22], [37, 43], [51, 86], [3, 5, 32], [2, 4, 6], [-1, 64, -8], [3, 5, 8, 3], [8, 3, 7, 1]]
b = Matrix_2(a_list)
d = Matrix_2(c_list)
result_list = b + d
result = Matrix_2(result_list)
print(asizeof.asizeof(result))  # => результат после оптимизации: размер 40
print(result)
