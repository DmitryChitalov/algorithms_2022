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

Это файл для третьего скрипта
"""

"""
Основы языка Python
Урок 9. Объектно-ориентированное программирование (ООП)
1. Создать класс TrafficLight (светофор).
"""

import time
from pympler import asizeof

'''
Класс Светофор с защищенным аргументом color и методом running
Атрибут определяет с какого цвета начинает работать светофор циклически
'''



class TrafficLight:
    def __init__(self, color):
        self._color = color

    def running(self):
        if self._color == 'красный':
            while True:
                self._color = 'красный'
                print(self._color)
                time.sleep(7)
                self._color = 'желтый'
                print(self._color)
                time.sleep(2)
                self._color = 'зеленый'
                print(self._color)
                time.sleep(4)
        elif self._color == 'желтый':
            while True:
                self._color = 'желтый'
                print(self._color)
                time.sleep(2)
                self._color = 'зеленый'
                print(self._color)
                time.sleep(4)
                self._color = 'красный'
                print(self._color)
                time.sleep(7)
        elif self._color == 'зеленый':
            while True:
                self._color = 'зеленый'
                print(self._color)
                time.sleep(4)
                self._color = 'красный'
                print(self._color)
                time.sleep(7)
                self._color = 'желтый'
                print(self._color)
                time.sleep(2)


a = TrafficLight('желтый')
print(a.__dict__)
print(asizeof.asizeof((a)))

"""Оптимизация, добавляем слоты"""

class TrafficLightOpt:
    __slots__ = ('_color')
    def __init__(self, color):
        self._color = color

    def running(self):
        if self._color == 'красный':
            while True:
                self._color = 'красный'
                print(self._color)
                time.sleep(7)
                self._color = 'желтый'
                print(self._color)
                time.sleep(2)
                self._color = 'зеленый'
                print(self._color)
                time.sleep(4)
        elif self._color == 'желтый':
            while True:
                self._color = 'желтый'
                print(self._color)
                time.sleep(2)
                self._color = 'зеленый'
                print(self._color)
                time.sleep(4)
                self._color = 'красный'
                print(self._color)
                time.sleep(7)
        elif self._color == 'зеленый':
            while True:
                self._color = 'зеленый'
                print(self._color)
                time.sleep(4)
                self._color = 'красный'
                print(self._color)
                time.sleep(7)
                self._color = 'желтый'
                print(self._color)
                time.sleep(2)


b = TrafficLightOpt('желтый')
print(b.__slots__)
print(asizeof.asizeof((b)))

"""Слоты в виде кортежа сократили размер с 296 до 40"""