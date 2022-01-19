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

Это файл для второго скрипта
"""
from memory_profiler import profile
from pympler import asizeof


class Road:
    def __init__(self, lenght, widht, weight, high):
        self._lenght = lenght
        self._widht = widht
        self.weight = weight
        self.high = high
    def calculate_mass(self):
        calculate_mass = self._lenght * self._widht * self.weight * self.high / 1000
        print(f'Для покрытия дорожного полотна полностью потребуется: {round(calculate_mass)} тонн асфальта')
@profile
def func_1():
    r = Road(1000, 1000, 50, 1)
    r.calculate_mass()
    print(asizeof.asizeof(r))
func_1()


class Road_2:
    __slots__ = ['lenght', 'widht', 'high', 'weight']
    def __init__(self, lenght, widht,weight, high):
        self.lenght = lenght
        self.widht = widht
        self.high = high
        self.weight = weight
    def calculate_mass(self):
        calculate_mass = self.lenght * self.widht * self.weight * self.high / 1000
        print(f'Для покрытия дорожного полотна полностью потребуется: {round(calculate_mass)} тонн асфальта')
@profile
def func_2():
    r = Road_2(1000, 1000, 50, 1)
    r.calculate_mass()
    print(asizeof.asizeof(r))
func_2()

"""
Применил слоты в ооп, но показатель MIB остался таким же
зато размер обьекта уменьшился в 3 раза
"""