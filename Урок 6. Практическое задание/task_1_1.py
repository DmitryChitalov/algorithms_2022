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
from collections import defaultdict
from functools import reduce
from memory_profiler import profile
from numpy import array

# Решение через ООПС


class HexNum:
    __slots__ = ('digits')

    def __init__(self, digits):
        """
        Функция инициализации класса, в качестве аргумента требует список цифр.
        """
        #self.digits = digits
        self.digits = array(digits)

    def from_str(input_str):
        """
        Метод возвращает список символов для представления 16-ричного числа.
        Все буквенные символы переводятся в заглавные.
        В качестве аргумента берет строку.
        """
        return HexNum(list(input_str.upper()))

    def __add__(self, other):
        """
        Метод возвращает экземпляр класса, который является суммой двух таковых.
        """
        result = hex(int(''.join(self.digits), 16) +
                     int(''.join(other.digits), 16))
        return HexNum.from_str(str(result)[2:])

    def __mul__(self, other):
        """
        Метод возвращает экземпляр класса, который является произведением двух таковых.
        """
        result = hex(int(''.join(self.digits), 16) *
                     int(''.join(other.digits), 16))
        return HexNum.from_str(str(result)[2:])

    def __str__(self):
        """
        Перегруженный магический метод для удобного вывода через print.
        """
        return f'{self.digits}'


@profile
def hex_sum():
    return reduce(
        lambda x, y: x + y,
        [HexNum.from_str('F') for _ in range(10**5)]
    )


print(HexNum.from_str('F') + HexNum.from_str('F'))

hex_sum()


"""
No  Slots:
Filename: E:\Programming\hexnum_oop.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    44     20.6 MiB     20.6 MiB           1   @profile
    45                                         def hex_sum():
    46     22.4 MiB    -10.9 MiB           2       return reduce(
    47     33.4 MiB      0.0 MiB      199999           lambda x, y: x + y,
    48     33.4 MiB     12.7 MiB      100003           [HexNum.from_str('F') for _ in range(10**5)]
    49

    
Slots:
Filename: E:\Programming\hexnum_oop.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    44     20.7 MiB     20.7 MiB           1   @profile
    45                                         def hex_sum():
    46     22.3 MiB     -5.2 MiB           2       return reduce(
    47     27.5 MiB      0.0 MiB      199999           lambda x, y: x + y,
    48     27.5 MiB      6.8 MiB      100003           [HexNum.from_str('F') for _ in range(10**5)]
    49
    

Slots + numpay array
Filename: E:\Programming\hexnum_oop.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    45     43.9 MiB     43.9 MiB           1   @profile
    46                                         def hex_sum():
    47     44.6 MiB    -15.6 MiB           2       return reduce(
    48     60.3 MiB      0.0 MiB      199999           lambda x, y: x + y,
    49     60.3 MiB      4.9 MiB      100003           [HexNum.from_str('F') for _ in range(10**5)]
    50 


Вывод: используя слоты и преобразование в массив Numpy, удалось сильно сократить расход памяти на хранение экземпляра класса.

Почему так:

1. Используя слоты, можно хранить данные класа не в dict, а в tuple, что значительно снижает затраты памяти, но класс в невозможно
динамически добавлять атрибуты.

2. Вместо обычного list, использался намного более оптимальный тип из модуля Numpy

"""
