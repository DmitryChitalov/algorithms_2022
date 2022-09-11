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
from sys import getsizeof


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        self.elems = []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class QueueClassOpti:
    __slots__ = ['elems']

    def __init__(self):
        self.elems = []

    def is_empty(self):
        self.elems = []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


def create_queue(num):
    queue_stand = QueueClass()
    for i in range(num):
        queue_stand.to_queue(i)
    return queue_stand


def create_queue_opti(num):
    queue_opti = QueueClassOpti()
    for i in range(num):
        queue_opti.to_queue(i)
    return queue_opti


if __name__ == '__main__':
    my_num = 10 ** 4

    print('Размер объекта класса созданного со слотами: ', getsizeof(create_queue_opti(my_num)))
    print('Размер объекта класса созданного без слотов: ', getsizeof(create_queue(my_num)))
    """
    Результаты замеров:
    Размер объекта класса созданного со слотами:  40
    Размер объекта класса созданного без слотов:  48
    
    Создания класса - очередь, с использованием слота и без.
    Показал, что созданный объект с использованием слота,
    занимает меньше памяти
    """
