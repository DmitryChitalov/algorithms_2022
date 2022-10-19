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

# Урок 9, задание 1 python basics
# Создать класс TrafficLight (светофор)
from pympler import asizeof
import time
from itertools import cycle


class TrafficLight:
    colors_time = {'красный': 7, 'желтый': 2, 'зеленый': 5}

    def __init__(self, color='красный'):
        self.__color = color

    def state(self):
        return f'Цвет светофора {self.__color}'

    def running(self, duration):
        i = 0
        for color in cycle(self.colors_time.keys()):
            self.__color = color
            print(self.state())
            time.sleep(self.colors_time[color])
            i += self.colors_time[color]
            if self.__color == 'зеленый':
                self.__color = 'желтый'
                print(self.state())
                time.sleep(self.colors_time[self.__color])
                i += self.colors_time[self.__color]
            if i >= duration or i >= 50:
                break


class ModyTrafficLight:
    __slots__ = ['color']
    colors_time = {'красный': 7, 'желтый': 2, 'зеленый': 5}

    def __init__(self, color='красный'):
        self.color = color

    def state(self):
        return f'Цвет светофора {self.color}'

    def running(self, duration):
        i = 0
        for color in cycle(self.colors_time.keys()):
            self.color = color
            print(self.state())
            time.sleep(self.colors_time[color])
            i += self.colors_time[color]
            if self.color == 'зеленый':
                self.color = 'желтый'
                print(self.state())
                time.sleep(self.colors_time[self.color])
                i += self.colors_time[self.color]
            if i >= duration or i >= 50:
                break


if __name__ == '__main__':
    a = TrafficLight()
    print(asizeof.asizeof(a))
    b = ModyTrafficLight()
    print(asizeof.asizeof(b))