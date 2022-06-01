"""
Курс: Основы языка Python
Урок: 8
Задание: 7
-----------------------------------------------------------------------------
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение
созданных экземпляров. Проверьте корректность полученного результата.
"""

from pympler.asizeof import asizeof
from random import randint


##############################################################################
"""
ИСХОДНОЕ РЕШЕНИЕ

Размер отдельного объекта: 312 байт(а)
Размер всех объектов: 1248 байт(а)
"""

class Complex:

    def __init__(self, a=0, b=0):
        try:
            self.a = float(a)
        except ValueError:
            self.a = 0
        try:
            self.b = float(b)
        except ValueError:
            self.b = 0

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    @property
    def record(self):
        return f'{self.a} + {self.b} * i'


a = Complex(randint(0,10_000), randint(0,10_000))
b = Complex(randint(0,10_000), randint(0,10_000))
c = a + b
d = a * b
print('---> ИСХОДНОЕ РЕШЕНИЕ')
print(f'Комплесное число a = {a.record}. Размер объекта: {asizeof(a)} байт(а)')
print(f'Комплесное число b = {b.record}. Размер объекта: {asizeof(b)} байт(а)')
print(f'Комплесное число c = {c.record}. Размер объекта: {asizeof(c)} байт(а)')
print(f'Комплесное число d = {d.record}. Размер объекта: {asizeof(d)} байт(а)')
print('----------------------------------')
print(f'Размер всех объектов: {asizeof(a) * 4} байт(а)')
print('----------------------------------')


##############################################################################
"""
ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ

Описание: использовал слоты для атрибутов действительной и мнимой части
комплексного числа.

Размер отдельного объекта: 96 байт(а)
Размер всех объектов: 384 байт(а)
"""

class Complex:
    __slots__ = ['a', 'b']

    def __init__(self, a=0, b=0):
        try:
            self.a = float(a)
        except ValueError:
            self.a = 0
        try:
            self.b = float(b)
        except ValueError:
            self.b = 0

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    @property
    def record(self):
        return f'{self.a} + {self.b} * i'


a = Complex(randint(0,10_000), randint(0,10_000))
b = Complex(randint(0,10_000), randint(0,10_000))
c = a + b
d = a * b
print('---> ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ')
print(f'Комплесное число a = {a.record}. Размер объекта: {asizeof(a)} байт(а)')
print(f'Комплесное число b = {b.record}. Размер объекта: {asizeof(b)} байт(а)')
print(f'Комплесное число c = {c.record}. Размер объекта: {asizeof(c)} байт(а)')
print(f'Комплесное число d = {d.record}. Размер объекта: {asizeof(d)} байт(а)')
print('----------------------------------')
print(f'Размер всех объектов: {asizeof(a) * 4} байт(а)')
print('----------------------------------')