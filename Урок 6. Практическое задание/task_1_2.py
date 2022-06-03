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

Это файл для второго скрипта
"""
from memory_profiler import profile


# Урок 1. Задание 5

class PlatesStack:
    def __init__(self, max_plates=3):
        self.stacks = [[]]
        self.current_stack = 0
        self.max_plates = max_plates

    def __str__(self):
        return str(self.stacks)

    def add_plate(self, plate: str):
        if len(self.stacks[self.current_stack]) == self.max_plates:
            self.stacks.append([])
            self.current_stack += 1
        self.stacks[self.current_stack].append(plate)

    def take_plate(self):
        if len(self.stacks[self.current_stack]) > 0:
            plate = self.stacks[self.current_stack].pop()
            if len(self.stacks[self.current_stack]) == 0 and len(self.stacks) > 1:
                self.stacks.pop()
                self.current_stack -= 1
            return plate

    def current_plate(self):
        return self.stacks[self.current_stack][-1]

    def stack_count(self):
        return len(self.stacks)

    def plates_count(self):
        return sum([len(x) for x in self.stacks])


# Переводим класс на слоты
class PlatesStackSlots:
    __slots__ = ('stacks', 'current_stack', 'max_plates')

    def __init__(self, max_plates=3):
        self.stacks = [[]]
        self.current_stack = 0
        self.max_plates = max_plates

    def __str__(self):
        return str(self.stacks)

    def add_plate(self, plate: str):
        if len(self.stacks[self.current_stack]) == self.max_plates:
            self.stacks.append([])
            self.current_stack += 1
        self.stacks[self.current_stack].append(plate)

    def take_plate(self):
        if len(self.stacks[self.current_stack]) > 0:
            plate = self.stacks[self.current_stack].pop()
            if len(self.stacks[self.current_stack]) == 0 and len(self.stacks) > 1:
                self.stacks.pop()
                self.current_stack -= 1
            return plate

    def current_plate(self):
        return self.stacks[self.current_stack][-1]

    def stack_count(self):
        return len(self.stacks)

    def plates_count(self):
        return sum([len(x) for x in self.stacks])


@profile
def profile_plates(plate_class):
    lst = []
    for i in range(30000):
        pl = plate_class()
        pl.add_plate(str(i))
        lst.append(pl)


if __name__ == '__main__':
    profile_plates(PlatesStack)
    profile_plates(PlatesStackSlots)


"""
Перевел хранение атрибутов класса на слоты. 
Объекты класса стали занимать меньше места.


Line #    Mem usage    Increment   Line Contents
================================================
   107     16.7 MiB      0.0 MiB   @profile
   108                             def profile_plates(plate_class):
   109     16.7 MiB      0.0 MiB       lst = []
   110     28.3 MiB     11.6 MiB       for i in range(30000):
   111     28.3 MiB      0.0 MiB           pl = plate_class()
   112     28.3 MiB      0.0 MiB           pl.add_plate(str(i))
   113     28.3 MiB      0.0 MiB           lst.append(pl)


Filename: C:\DEV\Python\algorithms_2022\Урок 6. Практическое задание\task_1_2.py

Line #    Mem usage    Increment   Line Contents
================================================
   107     20.4 MiB      0.0 MiB   @profile
   108                             def profile_plates(plate_class):
   109     20.4 MiB      0.0 MiB       lst = []
   110     25.7 MiB      5.3 MiB       for i in range(30000):
   111     25.7 MiB      0.0 MiB           pl = plate_class()
   112     25.7 MiB      0.0 MiB           pl.add_plate(str(i))
   113     25.7 MiB      0.0 MiB           lst.append(pl)

"""