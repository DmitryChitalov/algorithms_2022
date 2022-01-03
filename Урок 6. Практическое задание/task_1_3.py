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

Это файл для третьего скрипта
Урок 5 курс алгоритмов. Задание 2.
"""
from memory_profiler import profile
from pympler.asizeof import asizeof


# Original
class Hex:

    def __init__(self, number: str):
        self.number = list(number)

    def __add__(self, other):
        if isinstance(other, Hex):
            return Hex('%X' % (int(''.join(self.number), 16) + int(''.join(other.number), 16)))
        elif isinstance(other, str):
            return Hex('%X' % (int(''.join(self.number), 16) + int(''.join(other), 16)))

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Hex):
            return Hex('%X' % (int(''.join(self.number), 16) * int(''.join(other.number), 16)))
        elif isinstance(other, str):
            return Hex('%X' % (int(''.join(self.number), 16) * int(other, 16)))

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return f'{self.number}'

    def __repr__(self):
        return 'Hexadecimal'


# Optimize
class Hex2:
    __slots__ = 'number',

    def __init__(self, number: str):
        self.number = list(number)

    def __add__(self, other):
        if isinstance(other, Hex2):
            return Hex2('%X' % (int(''.join(self.number), 16) + int(''.join(other.number), 16)))
        elif isinstance(other, str):
            return Hex2('%X' % (int(''.join(self.number), 16) + int(''.join(other), 16)))

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Hex2):
            return Hex2('%X' % (int(''.join(self.number), 16) * int(''.join(other.number), 16)))
        elif isinstance(other, str):
            return Hex2('%X' % (int(''.join(self.number), 16) * int(other, 16)))

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return f'{self.number}'

    def __repr__(self):
        return 'Hexadecimal'


if __name__ == '__main__':
    print(asizeof(Hex('F3B')))
    print(asizeof(Hex2('F3B')))
    print("""Используя __slots__ (слоты) в создании класса, мы ограничиваем объект в создании дополнительных атрибутов, 
что позволяет сэкономить память 
    """)
