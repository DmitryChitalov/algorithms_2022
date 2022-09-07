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

Это файл для второго скрипта
"""
# Исходный код: Урок 5. Практическое задание task_2.py
#
# Способ 2 минимизации расходования памяти. Слоты в ООП
#
"""
Функция 'sys.getsizeof' возвращает размер переданного ей объекта, этот размер 
не включает в себя сложные структуры классов и т.д.

Функция 'pympler.asizeof' рекурсивно ищет все вложенные поля и элементы  и 
отображает общий размер объекта. 
"""
from pympler import asizeof


class Hex:
    def __init__(self, number):
        self.lst_hexnumber = list(number)

    def get_number(self):
        return self.lst_hexnumber

    def __add__(self, other):
        return list(format(int(''.join(self.lst_hexnumber), 16) +
                           int(''.join(other.lst_hexnumber), 16),
                           'X'
                           )
                    )

    def __mul__(self, other):
        return list(format(int(''.join(self.lst_hexnumber), 16) *
                           int(''.join(other.lst_hexnumber), 16),
                           'X'
                           )
                    )


print("* * * Решение через ООП * * *")
str_hexnumber_1 = input("Введите 1-е шестнадцатеричное число: ")
str_hexnumber_2 = input("Введите 2-е шестнадцатеричное число: ")

hex_1 = Hex(str_hexnumber_1)
hex_2 = Hex(str_hexnumber_2)
print(f"The hex_1 has size is: {asizeof.asizeof(hex_1)} bytes")
print(f"The hex_2 has size is: {asizeof.asizeof(hex_2)} bytes")
"""
The hex_1 has size is: 400 bytes
The hex_2 has size is: 464 bytes
"""


class Hex:
    __slots__ = ['lst_hexnumber']

    def __init__(self, number):
        self.lst_hexnumber = list(number)

    def get_number(self):
        return self.lst_hexnumber

    def __add__(self, other):
        return list(format(int(''.join(self.lst_hexnumber), 16) +
                           int(''.join(other.lst_hexnumber), 16),
                           'X'
                           )
                    )

    def __mul__(self, other):
        return list(format(int(''.join(self.lst_hexnumber), 16) *
                           int(''.join(other.lst_hexnumber), 16),
                           'X'
                           )
                    )


hex_1 = Hex(str_hexnumber_1)
hex_2 = Hex(str_hexnumber_2)
print(f"The hex_1 has size is: {asizeof.asizeof(hex_1)} bytes")
print(f"The hex_2 has size is: {asizeof.asizeof(hex_2)} bytes")
"""
The hex_1 has size is: 224 bytes
The hex_2 has size is: 288 bytes
"""


print(f"Числа сохранены как: "
      f"{hex_1.get_number()} {hex_2.get_number()}",
      end=' ')
print("Сумма: ", hex_1 + hex_2)
print("Произведение: ", hex_1 * hex_2)
print('-' * 80)
