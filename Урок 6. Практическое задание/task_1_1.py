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
В данном задании использовался код с задания:
Урок 1, задание 5
https://github.com/DmitryChitalov/algorithms_2022/pull/717
__slots__
"""
from pympler import asizeof


class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def stack_size(self):
        return len(self.elems)

    def push_in(self, el):
        if self.is_empty() or len(self.elems[self.stack_size() - 1]) == 2:
            nlist = []
            nlist.append(el)
            self.elems.append(nlist)
        else:
            self.elems[(self.stack_size() - 1)].append(el)

    def pop_out(self):
        if len(self.elems[self.stack_size() - 1]) == 1:
            self.elems.pop()
        else:
            self.elems[self.stack_size() - 1].pop()

    def get_val(self):
        return self.elems[self.stack_size() - 1][len(self.elems[len(self.elems) - 1]) - 1]


class StackClassSlots:

    __slots__ = ['elems']

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def stack_size(self):
        return len(self.elems)

    def push_in(self, el):
        if self.is_empty() or len(self.elems[self.stack_size() - 1]) == 2:  # указываем, что пороговое значение стопки == 2, для примера
            nlist = []
            nlist.append(el)
            self.elems.append(nlist)
        else:
            self.elems[(self.stack_size() - 1)].append(el)

    def pop_out(self):
        if len(self.elems[self.stack_size() - 1]) == 1:
            self.elems.pop()
        else:
            self.elems[self.stack_size() - 1].pop()

    def get_val(self):
        return self.elems[self.stack_size() - 1][len(self.elems[len(self.elems) - 1]) - 1]




SC_OBJ = StackClass()
print('Стандартный класс: ', asizeof.asizeof(SC_OBJ), '\n')

SC_SLOT_OBJ = StackClassSlots()
print('Класс с использованием конструкции __slots__: ', asizeof.asizeof(SC_SLOT_OBJ))

"""
Для оптимизации памяти при создании класса использовал конструкцию __slots__
Результаты при запуске скрипта

Стандартный класс:  264 

Класс с использованием конструкции __slots__:  96
"""