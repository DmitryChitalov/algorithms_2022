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

from pympler import asizeof


# Задача про сложение 16-тиричных чисел
class Hex():

    def __init__(self, digits):
        self.digits = digits

    @staticmethod
    def hex_to_dec(digits_string):
        return int(''.join(digits_string), 16)

    def __add__(self, other):
        sum_dec = self.hex_to_dec(self.digits) + self.hex_to_dec(other.digits)
        return hex(sum_dec).replace('0x', '').upper()

    def __mul__(self, other):
        sum_dec = self.hex_to_dec(self.digits) * self.hex_to_dec(other.digits)
        return hex(sum_dec).replace('0x', '').upper()


class HexSlots():  # оптимизация по хранению
    __slots__ = ['digits']

    def __init__(self, digits):
        self.digits = digits

    @staticmethod
    def hex_to_dec(digits_string):
        return int(''.join(digits_string), 16)

    def __add__(self, other):
        sum_dec = self.hex_to_dec(self.digits) + self.hex_to_dec(other.digits)
        return hex(sum_dec).replace('0x', '').upper()

    def __mul__(self, other):
        sum_dec = self.hex_to_dec(self.digits) * self.hex_to_dec(other.digits)
        return hex(sum_dec).replace('0x', '').upper()


if __name__ == '__main__':
    hex_1 = Hex(input('Первое число: ').split())
    hex_2 = Hex(input('Второе число: ').split())
    print(f'Сумма: {(hex_1 + hex_2)}')
    print(f'Произведение: {(hex_1 * hex_2)}')
    hex_3 = HexSlots(input('Третье число: ').split())

    print(asizeof.asizeof(hex_1))  # 416
    print(asizeof.asizeof(hex_3))  # 248
    # Хранение свойств объекта в кортеже, а не словаре, оптимизирует использование памяти
