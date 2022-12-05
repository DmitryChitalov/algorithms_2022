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
from memory_profiler import profile
from sys import getsizeof


"""
Основы Python (10 урок, 3 задание)
3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка». 
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). И т.д...
"""


class Cell:

    def __init__(self, cells: int):
        self.cells = cells

    def __add__(self, other):
        return int(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return int(self.cells - other.cells)
        elif other.cells > self.cells:
            return int(other.cells - self.cells)
        else:
            return 'Разность 2 клеток должна быть больше 0'

    def __mul__(self, other):
        cell_result = Cell(self.cells * other.cells)
        return cell_result

    def __str__(self):
        return str(self.cells)

    def __floordiv__(self, other):
        if self.cells > other.cells:
            cell_result_1 = Cell(self.cells // other.cells)
            return cell_result_1
        elif other.cells > self.cells:
            cell_result_1 = Cell(other.cells // self.cells)
            return cell_result_1

    def __truediv__(self, other):
        if self.cells > other.cells:
            cell_result_1 = Cell(self.cells / other.cells)
            return cell_result_1
        elif other.cells > self.cells:
            cell_result_1 = Cell(other.cells / self.cells)
            return cell_result_1

    @profile
    def make_order(self, cell_row):
        self.cell_row = cell_row
        i = cell_row
        n = r'\n'
        row = ''
        while i <= self.cells:
            rft = cell_row * '*'
            row += f'{rft}{n}'
            i += cell_row
        counter = row.count('*')
        if counter < self.cells:
            bb = str((self.cells % cell_row) * '*')
            return f'{row}{bb}'
        else:
            return row


c1 = Cell(25)
c2 = Cell(30)
dd = c1 / c2
print(type(dd))
print(dd)
c3 = Cell(12)
print(Cell.make_order(c3, 5), getsizeof(c3))


class Cell_1:
    __slots__ = ['cells', 'cell_row']

    def __init__(self, cells: int):
        self.cells = cells

    def __add__(self, other):
        return int(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return int(self.cells - other.cells)
        elif other.cells > self.cells:
            return int(other.cells - self.cells)
        else:
            return 'Разность 2 клеток должна быть больше 0'

    def __mul__(self, other):
        cell_result = Cell(self.cells * other.cells)
        return cell_result

    def __str__(self):
        return str(self.cells)

    def __floordiv__(self, other):
        if self.cells > other.cells:
            cell_result_1 = Cell(self.cells // other.cells)
            return cell_result_1
        elif other.cells > self.cells:
            cell_result_1 = Cell(other.cells // self.cells)
            return cell_result_1

    def __truediv__(self, other):
        if self.cells > other.cells:
            cell_result_1 = Cell(self.cells / other.cells)
            return cell_result_1
        elif other.cells > self.cells:
            cell_result_1 = Cell(other.cells / self.cells)
            return cell_result_1

    @profile
    def make_order(self, cell_row):
        self.cell_row = cell_row
        i = cell_row
        n = r'\n'
        row = ''
        while i <= self.cells:
            rft = cell_row * '*'
            row += f'{rft}{n}'
            i += cell_row
        counter = row.count('*')
        if counter < self.cells:
            bb = str((self.cells % cell_row) * '*')
            return f'{row}{bb}'
        else:
            return row


c1_1 = Cell_1(25)
c3_1 = Cell_1(12)
print(Cell_1.make_order(c3_1, 5), getsizeof(c3_1))


# По аналогии с предыдущем кодом я сделал этот.