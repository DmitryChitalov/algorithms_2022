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
from memory_profiler import memory_usage
import time


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


"""Курс "Основы языка Python" Урок №9 Задача №1 """


@memory
class TrafficLight:

    def __init__(self):
        self.__color_red = 'red'
        self.__color_yellow = 'yellow'
        self.__color_green = 'green'

    def running(self):
        # while True:
        print(f'\033[31m{self.__color_red}')
        time.sleep(7)
        print(f'\033[33m{self.__color_yellow}')
        time.sleep(2)
        print(f'\033[32m{self.__color_green}')
        time.sleep(5)


result = TrafficLight()
result.running()


@memory
class TrafficLight:
    __slots__ = ('__color_red', '__color_yellow', '__color_green')

    def __init__(self):
        self.__color_red = 'red'
        self.__color_yellow = 'yellow'
        self.__color_green = 'green'

    def running(self):
        # while True:
        print(f'\033[31m{self.__color_red}')
        time.sleep(7)
        print(f'\033[33m{self.__color_yellow}')
        time.sleep(2)
        print(f'\033[32m{self.__color_green}')
        time.sleep(5)


result = TrafficLight()
result.running()

"""Задала ограниченный набор атрибутов класса, что существенно сократило размер объекта"""
