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

Это файл для пятого скрипта
"""
from memory_profiler import profile


class Task_Board1:

    def __init__(self):
        self.tasks = []
        self.problems = []
        self.done = []

    def __str__(self):
        return (f' tasks {self.tasks} problems {self.problems} done {self.done}')

    def is_empty(self, degue):
        return degue == []

    def to_queue(self, degue, item):
        degue.insert(0, item)

    def from_queue(self, degue):
        return degue.pop()

    def to_queue(self, degue, item):
        degue.insert(0, item)

    def from_queue_to_queue(self, fr, to):
        item = fr.pop()
        to.insert(0, item)

    def size(self, degue):
        return len(degue)


class Task_Board2:
    __slots__ = ('tasks', 'problems', 'done')

    def __init__(self):
        self.tasks = []
        self.problems = []
        self.done = []

    def __str__(self):
        return (f' tasks {self.tasks} problems {self.problems} done {self.done}')

    def is_empty(self, degue):
        return degue == []

    def to_queue(self, degue, item):
        degue.insert(0, item)

    def from_queue(self, degue):
        return degue.pop()

    def to_queue(self, degue, item):
        degue.insert(0, item)

    def from_queue_to_queue(self, fr, to):
        item = fr.pop()
        to.insert(0, item)

    def size(self, degue):
        return len(degue)

@profile
def main1():
    tb = Task_Board1()
    print(tb.is_empty(tb.tasks))  # -> True. Очередь пустая

    # помещаем объекты в очередь
    for i in range(100000):
        tb.to_queue(tb.tasks, i)


    tb.from_queue_to_queue(tb.tasks, tb.problems)
    tb.from_queue_to_queue(tb.tasks, tb.done)
    # print(tb)

    tb.from_queue(tb.done)
    # print(tb)

    print(tb.is_empty(tb.tasks))  # -> False. Очередь пустая
    print(tb.size(tb.tasks))  # -> 3

@profile
def main2():
    tb = Task_Board2()
    print(tb.is_empty(tb.tasks))  # -> True. Очередь пустая

    # помещаем объекты в очередь
    for i in range(100000):
        tb.to_queue(tb.tasks, i)

    tb.from_queue_to_queue(tb.tasks, tb.problems)
    tb.from_queue_to_queue(tb.tasks, tb.done)
    # print(tb)

    tb.from_queue(tb.done)
    # print(tb)

    print(tb.is_empty(tb.tasks))  # -> False. Очередь пустая
    print(tb.size(tb.tasks))  # -> 3

main1()
main2()
'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   116     22.9 MiB     22.9 MiB           1   @profile
   117                                         def main2():
   118     22.9 MiB      0.0 MiB           1       tb = Task_Board2()
   119     22.9 MiB      0.0 MiB           1       print(tb.is_empty(tb.tasks))  # -> True. Очередь пустая
   120                                         
   121                                             # помещаем объекты в очередь
   122     25.1 MiB  -6001.7 MiB      100001       for i in range(100000):     -   что это обозначает?                           
   123     25.1 MiB  -5999.6 MiB      100000           tb.to_queue(tb.tasks, i)
   124                                         
   125     25.1 MiB      0.0 MiB           1       tb.from_queue_to_queue(tb.tasks, tb.problems)
   126     25.1 MiB      0.0 MiB           1       tb.from_queue_to_queue(tb.tasks, tb.done)
   127                                             # print(tb)
   128                                         
   129     25.1 MiB      0.0 MiB           1       tb.from_queue(tb.done)
   130                                             # print(tb)
   131                                         
   132     25.1 MiB      0.0 MiB           1       print(tb.is_empty(tb.tasks))  # -> False. Очередь пустая
   133     25.1 MiB      0.0 MiB           1       print(tb.size(tb.tasks))  # -> 3

Использовал __Slots__. Экономия по памяти. Вопрос в отрицательных значениях в profile (см выше). 
'''
