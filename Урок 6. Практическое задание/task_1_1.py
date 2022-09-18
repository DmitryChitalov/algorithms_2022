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
from memory_profiler import profile
from random import randrange


#  Исходный  код
class ComplexNumber():
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            s = args[0].split('+')
            self.re = float(s[0].strip())
            self.im = float(s[1].strip()[:-1])
        elif len(args) == 2 and isinstance(args[0], (float, int)) and isinstance(args[1], (float, int)):
            self.re = args[0]
            self.im = args[1]
        else:
            raise ValueError(f'Невозможно превратить в комплексное число {args} ')

    def __str__(self):
        return f'{self.re} + {self.im}i'

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re + other.re, self.im + other.im)
        elif isinstance(other, (float, int)):
            return ComplexNumber(self.re + other, self.im)
        else:
            raise ValueError('Комплексные числа можно складывать только с числами.')

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re * other.re - self.im * other.im,
                                 self.im * other.re + self.re * other.im)
        elif isinstance(other, (float, int)):
            return ComplexNumber(self.re * other, self.im * other)
        else:
            raise ValueError('Комплексные числа можно умножать только на числа.')

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            c = ComplexNumber(other.re, -1 * other.im)
            c1 = self * c
            c2 = other * c
            return ComplexNumber(c1.re / c2.re, c1.im / c2.re)
        elif isinstance(other, (float, int)):
            return ComplexNumber(self.re / other, self.im / other)
        else:
            raise ValueError('Комплексные числа можно делить только на числа.')

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re - other.re, self.im - other.im)
        elif isinstance(other, (float, int)):
            return ComplexNumber(self.re - other, self.im)
        else:
            raise ValueError('Комплексные числа можно вычитать только с числами.')


@profile
def many_numbers():
    l = [ComplexNumber(randrange(100), randrange(100)) for _ in range(100000)]
    return l


#  Оптимизированный код
class ComplexNumber1():
    __slots__ = ('re', 'im')

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            s = args[0].split('+')
            self.re = float(s[0].strip())
            self.im = float(s[1].strip()[:-1])
        elif len(args) == 2 and isinstance(args[0], (float, int)) and isinstance(args[1], (float, int)):
            self.re = args[0]
            self.im = args[1]
        else:
            raise ValueError(f'Невозможно превратить в комплексное число {args} ')

    def __str__(self):
        return f'{self.re} + {self.im}i'

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re + other.re, self.im + other.im)
        elif isinstance(other, (float, int)):
            return ComplexNumber(self.re + other, self.im)
        else:
            raise ValueError('Комплексные числа можно складывать только с числами.')

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re * other.re - self.im * other.im,
                                 self.im * other.re + self.re * other.im)
        elif isinstance(other, (float, int)):
            return ComplexNumber(self.re * other, self.im * other)
        else:
            raise ValueError('Комплексные числа можно умножать только на числа.')

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            c = ComplexNumber(other.re, -1 * other.im)
            c1 = self * c
            c2 = other * c
            return ComplexNumber(c1.re / c2.re, c1.im / c2.re)
        elif isinstance(other, (float, int)):
            return ComplexNumber(self.re / other, self.im / other)
        else:
            raise ValueError('Комплексные числа можно делить только на числа.')

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re - other.re, self.im - other.im)
        elif isinstance(other, (float, int)):
            return ComplexNumber(self.re - other, self.im)
        else:
            raise ValueError('Комплексные числа можно вычитать только с числами.')


@profile
def many_numbers1():
    l = [ComplexNumber1(randrange(100), randrange(100)) for _ in range(100000)]
    return l


if __name__ == '__main__':
    print("Используем словарь")
    many_numbers()
    print("Используем __slots__")
    many_numbers1()

"""
Результаты работы ниже.
Для комплексных чисел не нужен словарь атрибутов; они у числа неизменные, и их два. Можно сделать кортеж 
или  список

Используем словарь


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   141     20.0 MiB     20.0 MiB           1   @profile
   142                                         def many_numbers():
   143     36.7 MiB     16.8 MiB      100003       l=[ComplexNumber(randrange(100),randrange(100)) for _ in range(100000)]
   144     36.7 MiB      0.0 MiB           1       return l


Используем __slots__


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   146     23.3 MiB     23.3 MiB           1   @profile
   147                                         def many_numbers1():
   148     26.1 MiB -32984.0 MiB      100003       l=[ComplexNumber1(randrange(100),randrange(100)) for _ in range(100000)]
   149     26.1 MiB      0.0 MiB           1       return l 
"""
