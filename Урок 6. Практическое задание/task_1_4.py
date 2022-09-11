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

Это файл для четвертого скрипта
"""

import json
import random
from collections import deque
from timeit import timeit
from memory_profiler import profile


# код из задачи 3, 5-го урока, зпмеры быстродействия дека и списка

@profile
def shell():
    some_list = []
    some_deq = deque()
    test_num = random.randint(-100, 100)

    def list_append(some_list, test_num):
        for i in range(100000):
            some_list.append(test_num)

    def deq_append(some_deq, test_num):
        for i in range(100000):
            some_deq.append(test_num)

    def list_pop(some_list):
        for i in range(50000):
            some_list.pop(len(some_list) - 1)

    def deq_pop(some_deq):
        for i in range(50000):
            some_deq.pop()

    list_append(some_list, test_num)
    deq_append(some_deq, test_num)
    list_pop(some_list)
    deq_pop(some_deq)


# в модифицированной версии, в месте вызова функций, делаем дамп списка до момента его следующего использования
# до этого момента, он почти не занимает память
@profile
def shell_2():
    some_list = []
    some_deq = deque()
    test_num = random.randint(-100, 100)

    def list_append(some_list, test_num):
        for i in range(100000):
            some_list.append(test_num)

    def deq_append(some_deq, test_num):
        for i in range(100000):
            some_deq.append(test_num)

    def list_pop(some_list):
        for i in range(50000):
            some_list.pop(len(some_list) - 1)

    def deq_pop(some_deq):
        for i in range(50000):
            some_deq.pop()

    list_append(some_list, test_num)
    some_list = json.dumps(some_list)  # сериализация
    deq_append(some_deq, test_num)
    some_list = json.loads(some_list)  # десириализация
    list_pop(some_list)
    deq_pop(some_deq)


shell()
shell_2()
