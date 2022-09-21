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

# Алгоритмы и структуры данных на Python. Базовый курс.
# Урок 1. Задание 5.

from memory_profiler import memory_usage
from pympler import asizeof


def decor_m(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


@decor_m
class PlateStackClass:
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.max_size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1][len(self.elems[len(self.elems) - 1]) - 1]

    def stack_size(self):
        elems_sum = 0
        for stack in self.elems:
            elems_sum += len(stack)
        return elems_sum

    def stack_count(self):
        return len(self.elems)


if __name__ == "__main__":
    plates = PlateStackClass(3)
    print(asizeof.asizeof(plates))
    plates.push_in('Plate1')
    plates.push_in('Plate2')
    plates.push_in('Plate3')
    plates.push_in('Plate4')
    plates.push_in('Plate5')
    print(plates)
    print(plates.pop_out())
    print(plates.get_val())
    print(plates.stack_size())
    print(plates.stack_count())
    print(plates)
    print(asizeof.asizeof(plates))
    print('_' * 50)


@decor_m
class PlateStackClass:
    __slots__ = ['elems', 'max_size']

    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.max_size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1][len(self.elems[len(self.elems) - 1]) - 1]

    def stack_size(self):
        elems_sum = 0
        for stack in self.elems:
            elems_sum += len(stack)
        return elems_sum

    def stack_count(self):
        return len(self.elems)


if __name__ == "__main__":
    plates = PlateStackClass(3)
    print(asizeof.asizeof(plates))
    plates.push_in('Plate1')
    plates.push_in('Plate2')
    plates.push_in('Plate3')
    plates.push_in('Plate4')
    plates.push_in('Plate5')
    print(plates)
    print(plates.pop_out())
    print(plates.get_val())
    print(plates.stack_size())
    print(plates.stack_count())
    print(plates)
    print(asizeof.asizeof(plates))


"""
С помощью memory_usage считает некорректно, я нечего не менял, но при первом вызове класса 
выполнение заняло 0.00390625 Mib при последующем выполнение заняло 0.0 Mib.
Поэтому, я использовал для посчёта модуль pympler.asizeof.

Я использовал __slots__, т.к. он позволяет снизить объём памяти, потребляемой экземплярами класса, 
ограничивая количество атрибутов ими поддерживаемых.

Выполнение заняло 0.00390625 Mib
424
[['Plate1', 'Plate2', 'Plate3', 'Plate4', 'Plate5']]
Plate5
Plate4
4
1
[['Plate1', 'Plate2', 'Plate3', 'Plate4']]
712
__________________________________________________
Выполнение заняло 0.0 Mib
200
[['Plate1', 'Plate2', 'Plate3', 'Plate4', 'Plate5']]
Plate5
Plate4
4
1
[['Plate1', 'Plate2', 'Plate3', 'Plate4']]
488

"""
