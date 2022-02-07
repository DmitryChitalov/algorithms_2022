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
import operator
from timeit import timeit

import memory_profiler
from pympler import asizeof
from recordclass import recordclass
from functools import reduce
""" исходное """
""" задание 2 из курса основ:
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина *
масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода. Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road:
    def __init__(self, length, width):
        self._length = length  # м
        self._width = width  # м
        self.thickness = 5  # см
        self.mass = 25  # кг

    @memory_profiler.profile
    def mass_calc(self):
        result = self.mass * self.thickness * self._width * self._length / 1000
        print(f"Результат вычислений массы: {round(result)} т")




""" оптимизированное """

class RoadOpt:
    __slots__ = ("_constants_list", "_constants" )

    def __init__(self, length: int, width: int):
        self._constants_list = recordclass("props", "thickness mass width length")
        self._constants = self._constants_list(thickness=5, mass=25, width=width, length=length)

    @memory_profiler.profile
    def mass_calc(self) -> float:
        result = reduce(operator.mul, self._constants) / 1000
        print(f"Результат вычислений массы: {round(result)} т")
        return result


if __name__ == "__main__":
    instance1 = Road(20, 5000)
    instance2 = RoadOpt(20, 5000)
    instance1.mass_calc()
    instance2.mass_calc()
    #print(f'Время исполнения функции instance1.mass_calc(): {timeit("instance1.mass_calc()", globals=globals())} s')
    #print(f'Время исполнения функции instance2.mass_calc(): {timeit("instance2.mass_calc()", globals=globals())} s')


    print(f"Размер instance1 класса Road: {asizeof.asizeof(instance1)}")
    print(f"Размер instance2 класса RoadOpt: {asizeof.asizeof(instance2)}")

    """
    Результаты: 
        Размер instance1 класса Road: 528
        Размер instance2 класса RoadOpt: 104
        Время исполнения функции instance1.mass_calc(): 0.2583027 s
        Время исполнения функции instance2.mass_calc(): 0.46080449999999995 s
    Вывод:
        Использование слотов сокращает потбление памяти на переменные, однако слоты ограничивает колличество атрибутов
        в классе и это стоит помнить. Тоесть Класс как бы теряет свою диниамичность к созданию новых атрибутов. 
        В дополнение recordclass отлично экономит память, и следует заметить что в него можно записать огромное 
        количество атрибутов для класса. Из минусов то, что нужно импортировать модуль для работы с ним.
        
        timeit number: 1000000
        Время на вычисление в оптимизированном классе увеличелось на 40%, но временем можно пожертвовать так как 
        вычисления максимально простые что не создает никаких проблем. 
        
    Профилирование памяти:
        Для данного примера оптимизация в принципе не нужна. Но как для практика оптимизации на мой взгляд неплохо 
        выполнена. Из профилирования видно что данный код итак потребляет мало памяти.
        
    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
    55     31.7 MiB     31.7 MiB           1       @memory_profiler.profile
    56                                             def mass_calc(self):
    57     31.7 MiB      0.0 MiB           1           result = self.mass * self.thickness * self._width * self._length / 1000
    58     31.7 MiB      0.0 MiB           1           print(f"Результат вычислений массы: {round(result)} т")
    
    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
    72     31.8 MiB     31.8 MiB           1       @memory_profiler.profile
    73                                             def mass_calc(self):
    74     31.8 MiB      0.0 MiB           1           result = reduce(operator.mul, self._constants) / 1000
    75     31.8 MiB      0.0 MiB           1           print(f"Результат вычислений массы: {round(result)} т")
    """
