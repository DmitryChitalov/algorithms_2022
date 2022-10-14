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

# Урок 9 задание 1 Основы
from memory_profiler import profile
import time


class TrafficLight():
    def __init__(self) -> None:
        self.__color = 'красный'

    def __change_color(self):
        if self.__color == 'красный':
            time.sleep(7)
            self.__color = 'желтый'
        elif self.__color == 'желтый':
            time.sleep(2)
            self.__color = 'зеленый'
        else:
            time.sleep(5)
            self.__color = 'красный'

    def running(self):
        try:
            print('Для выхода нажмитие Ctrl+C')
            while True:
                print('Сигнал светофора: ', self.__color)
                self.__change_color()
        except:
            print('Завершение программы...')


class TrafficLightSlots():
    # Кортеж слотов
    __slots__ = ('__color')

    def __init__(self) -> None:
        self.__color = 'красный'

    def __change_color(self):
        if self.__color == 'красный':
            time.sleep(7)
            self.__color = 'желтый'
        elif self.__color == 'желтый':
            time.sleep(2)
            self.__color = 'зеленый'
        else:
            time.sleep(5)
            self.__color = 'красный'

    def running(self):
        try:
            print('Для выхода нажмитие Ctrl+C')
            while True:
                print('Сигнал светофора: ', self.__color)
                self.__change_color()
        except:
            print('Завершение программы...')

@profile
def trL():
    trafficLight = TrafficLight()
    trafficLight.running()

@profile
def trLS():
    trafficLight = TrafficLightSlots()
    trafficLight.running()

trL()
trLS()