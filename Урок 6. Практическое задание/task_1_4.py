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


class PlateStack:
    __slots__ = ['stack', 'idx']

    MAX_STACK = 2

    def __init__(self):
        self.stack = [[]]
        self.idx = 0

    def __str__(self):
        return str(self.stack)

    def add(self, plate):
        """ Добавляем тарелку """
        if len(self.stack[self.idx]) >= self.MAX_STACK:
            self.idx = self.idx + 1
            self.stack.append([])

        self.stack[self.idx].append(plate)

    def is_empty(self):
        return self.stack == [[]]

    # FIX
    def delete(self):
        """ Удаляем тарелку """
        if len(self.stack[self.idx]) > 0:
            self.stack[self.idx].pop()
            if len(self.stack[self.idx]) <= 0:
                self.idx -= 1
                self.stack.pop()

    def clear(self):
        """ Чистим всё """
        self.stack = [[]]
        self.idx = 0

    def stack_size(self):
        """Общее количество тарелок"""
        elem_sum = 0
        for stack in self.stack:
            elem_sum += len(stack)
        return elem_sum


plate = PlateStack()
# print(plate.__sizeof__()) # -> 32
# print(asizeof.asizeof(plate)) # -> 408

# Slots
print(asizeof.asizeof(plate))  # -> 192
