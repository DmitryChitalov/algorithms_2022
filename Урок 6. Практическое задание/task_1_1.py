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

from memory_profiler import profile

# Урок 1 задание 5

@profile
def unslotted():
    class Stack:
        def __init__(self, max_one_stack : int = 7):
            self.stack = []
            self.max_stack = max_one_stack
            self.index_list = 0

        def stack_put(self, item):
            if len(self.stack) == 0:
                self.stack.append(list())
            if len(self.stack[self.index_list]) == self.max_stack:
                self.stack.append(list())
                self.index_list += 1
            self.stack[self.index_list].append(item)

        def stack_get(self):
            if len(self.stack) == 0:
                print('Стэк пустой')
                return None
            else:
                item = self.stack[self.index_list].pop()

            if len(self.stack[self.index_list]) == 0:
                self.stack.pop()
                self.index_list -= 1
                if self.index_list == -1: self.index_list = 0

            return item

        def stack_print(self):
            print(self.stack)

@profile
def slotted():
    class StackMemory:
        __slots__ = ('stack', 'max_stack', 'index_list')

        def __init__(self, max_one_stack : int = 7):
            self.stack = []
            self.max_stack = max_one_stack
            self.index_list = 0

        def stack_put(self, item):
            if len(self.stack) == 0:
                self.stack.append(list())
            if len(self.stack[self.index_list]) == self.max_stack:
                self.stack.append(list())
                self.index_list += 1
            self.stack[self.index_list].append(item)

        def stack_get(self):
            if len(self.stack) == 0:
                print('Стэк пустой')
                return None
            else:
                item = self.stack[self.index_list].pop()

            if len(self.stack[self.index_list]) == 0:
                self.stack.pop()
                self.index_list -= 1
                if self.index_list == -1: self.index_list = 0

            return item

        def stack_print(self):
            print(self.stack)


# ПРОВЕРКА:
if __name__ == '__main__':
    slotted()           # Чуть меньше задействовано памяти при использовании __slots__ (19.9 MiB)
    unslotted()         # Без __slots__ (20.0)