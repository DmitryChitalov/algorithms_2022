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
# Урок 10 задание 3
# Реализовать программу работы с органическими
# клетками, состоящими из ячеек

from pympler import asizeof


class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            raise ValueError('Cell number should be above zero')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, number_in_row):
        number_of_rows = self.number // number_in_row
        cells_in_last_row = self.number % number_in_row
        cell = '*'
        cells_in_row = cell * number_in_row + '\n'
        return f'{cells_in_row * number_of_rows + cell * cells_in_last_row}'


my_obj = Cell(10)
print(asizeof.asizeof(my_obj))


class ModyCell:
    __slots__ = ['number']

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            raise ValueError('Cell number should be above zero')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, number_in_row):
        number_of_rows = self.number // number_in_row
        cells_in_last_row = self.number % number_in_row
        cell = '*'
        cells_in_row = cell * number_in_row + '\n'
        return f'{cells_in_row * number_of_rows + cell * cells_in_last_row}'


my_obj_2 = ModyCell(10)
print(asizeof.asizeof(my_obj_2))