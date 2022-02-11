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

Это файл для пятого скрипта
"""

# Алгоритмы и структуры данных на Python. Базовый курс Урок 1, Задание 5.

from pympler import asizeof


def sep():
    print('_' * 50)


class PlatesStack:
    def __init__(self, max_plates):
        self.plates = [[]]
        self.max_plates = max_plates

    def __str__(self):
        return str(self.plates)

    def is_empty(self):
        return self.plates == [[]]

    def push_in(self, items):
        if len(self.plates[len(self.plates) - 1]) < self.max_plates:
            self.plates[len(self.plates) - 1].append(items)
        else:
            self.plates.append([])
            self.plates[len(self.plates) - 1].append(items)

    def pop_out(self):
        res = self.plates[len(self.plates) - 1].pop()
        if len(self.plates[len(self.plates) - 1]) == 0:
            self.plates.pop()
        return res

    def get_val(self):
        return self.plates[len(self.plates) - 1]

    def stack_size(self):
        plates_count = 0
        for stack in self.plates:
            plates_count += len(stack)
            return len(self.plates)

    def stack_count(self):
        return len(self.plates)


p = PlatesStack(7)
print(asizeof.asizeof(p))
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
print(p)
print(asizeof.asizeof(p))
"""
424
[['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-']]
664
"""

sep()


class PlatesStack:
    __slots__ = ['plates', 'max_plates']

    def __init__(self, max_plates):
        self.plates = [[]]
        self.max_plates = max_plates

    def __str__(self):
        return str(self.plates)

    def is_empty(self):
        return self.plates == [[]]

    def push_in(self, items):
        if len(self.plates[len(self.plates) - 1]) < self.max_plates:
            self.plates[len(self.plates) - 1].append(items)
        else:
            self.plates.append([])
            self.plates[len(self.plates) - 1].append(items)

    def pop_out(self):
        res = self.plates[len(self.plates) - 1].pop()
        if len(self.plates[len(self.plates) - 1]) == 0:
            self.plates.pop()
        return res

    def get_val(self):
        return self.plates[len(self.plates) - 1]

    def stack_size(self):
        plates_count = 0
        for stack in self.plates:
            plates_count += len(stack)
            return len(self.plates)

    def stack_count(self):
        return len(self.plates)


p = PlatesStack(7)
print(asizeof.asizeof(p))
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
print(p)
print(asizeof.asizeof(p))

"""
200
[['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-']]
440
"""

# В данной задаче я использовал оптимизацию за счет конструкции __slots__,
# что позволило снизить объём памяти, потребляемой экземплярами класса
# Оптимизиция прошла успешно, показатели используемой памяти уменьшились
