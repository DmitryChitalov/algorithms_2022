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

from collections import defaultdict
from functools import reduce
from sys import exit
from memory_profiler import memory_usage, profile
from pympler import asizeof


def convert(user_input: str, output_dict=None, key=1, mode=0):
    """
    Функция convert имеет 3 режима работы (mode).
    mode 0. В качетсве аргументов подаются шестнадцатиричное число в формате строки, экземпляр словаря defaultdict и
    ключ. Создается пара ключ-значение, значение в которой - это введенная пользователем строка,
    преобразованная в список.
    mode 1. В качестве аргумента задается шестнадцатиричное число в формате строки. Возвращается список,
    состоящий из цифр числа.
    mode 2.  В качестве аргумента задается десятичное число в формате строки. Возращается эквивалентное
    шестандцатиричное число в формате списка (как в mode 1).
    :param user_input: входное число в формате строки
    :param output_dict: словарь, в который нужно положить пару ключ-значение (только для mode 0)
    :param key: ключ (только для mode 0)
    :param mode: режим работы
    :return: list или defaultdict, зависит от режима
    """
    if mode == 0:
        for i in range(len(user_input)):
            output_dict[key].append(user_input[i].upper())
        key += 1
        return output_dict
    elif mode == 1:
        output_list = list()
        for i in range(len(user_input)):
            output_list.append(user_input[i].upper())
        return output_list
    elif mode == 2:
        result = str(hex(int(user_input)))[2:].upper()
        return convert(result, mode=1)


def convert_opt(user_input: str, output_dict=None, key=1, mode=0):
    if mode == 0:
        for i in range(len(user_input)):
            output_dict[key].append(user_input[i].upper())
        key += 1
        return output_dict
    elif mode == 1:
        output_list = list()
        for i in range(len(user_input)):
            output_list.append(user_input[i].upper())
        output_tup = tuple(output_list)
        del output_list
        return output_tup
    elif mode == 2:
        result = str(hex(int(user_input)))[2:].upper()
        return convert_opt(result, mode=1)


def calc(num_1: str, num_2: str, operator: str):
    """
    Функция принимает в качетсве аргументов 2 шестандцатиричных числа и оператор (сложение или
    умножение) и выводит результат операции в формате списка. Возвращает экземпляр defaultdict,
    где хранятся оба числа и результат.
    :param num_1: число 1
    :param num_2: число 2
    :param operator: математическая операция
    :return:
    """
    try:
        numbers = defaultdict(list)
        convert(num_1, numbers, 1)
        convert(num_2, numbers, 2)
        num_1 = int(reduce(lambda a, b: a + b, numbers[1]), base=16)
        num_2 = int(reduce(lambda a, b: a + b, numbers[2]), base=16)
        if operator == '*':
            result = num_1 * num_2
        elif operator == '+':
            result = num_1 + num_2
        else:
            print('Недопустимая операция.')
            return
        result = str(hex(result))[2:].upper()
        convert(result, numbers, 3)
        print(f'{numbers[1]} {operator} {numbers[2]} = {numbers[3]}')
        return numbers
    except ValueError:
        print('Некорректное число.')
        return


class HexNumber:
    """
    Класс HexNumber. Для инициализации экземпляра класса необходимо указать шестнадцатиричное число
    в строковом формате.
    В атрибутах экземпляра класса хранятся шестнадцатиричное число в формате списка (атрибут hex_list)
    и эквивалент в десятичной системе в формате integer (атрибут base10_equiv)
    Для экземпляров класса доступны операции сложения и умножения.
    Корректность вводимого числа отслеживается при инициализации экземпляра класса.
    Если указано некорректное число, выводится сообщение и работа программы прекращается.
    """
    def __init__(self, user_input):
        try:
            self.user_input = user_input
            self.hex_list = convert(self.user_input, mode=1)
            self.base10_equiv = int(reduce(lambda a, b: a + b, self.hex_list), base=16)
        except ValueError:
            print('Некорректное число')
            exit()

    def __add__(self, other):
        result = self.base10_equiv + other.base10_equiv
        return convert(result, mode=2)

    def __mul__(self, other):
        result = self.base10_equiv * other.base10_equiv
        return convert(result, mode=2)


class HexNumberOpt:
    """
    Класс HexNumber. Для инициализации экземпляра класса необходимо указать шестнадцатиричное число
    в строковом формате.
    В атрибутах экземпляра класса хранятся шестнадцатиричное число в формате списка (атрибут hex_list)
    и эквивалент в десятичной системе в формате integer (атрибут base10_equiv)
    Для экземпляров класса доступны операции сложения и умножения.
    Корректность вводимого числа отслеживается при инициализации экземпляра класса.
    Если указано некорректное число, выводится сообщение и работа программы прекращается.
    """
    __slots__ = ('user_input', 'hex_list', 'base10_equiv')

    def __init__(self, user_input):
        try:
            self.user_input = user_input
            self.hex_list = convert_opt(self.user_input, mode=1)
            self.base10_equiv = int(reduce(lambda a, b: a + b, self.hex_list), base=16)
        except ValueError:
            print('Некорректное число')
            exit()

    def __add__(self, other):
        result = self.base10_equiv + other.base10_equiv
        return convert_opt(result, mode=2)

    def __mul__(self, other):
        result = self.base10_equiv * other.base10_equiv
        return convert_opt(result, mode=2)


if __name__ == '__main__':
    print('\nСкрипт №2 из д/з №5 курса "Алгоритмы и структуры данных Python".\n'
          'Код оптимизирован за счет применения:\n'
          '   1. конструкции __slots__ в конструкторе класса HexNumbersOpt.\n'
          '   2. tuple вместо list в функции convert_opt\n')
    print('Пожалуйста, введите 1-ое число: ', end='')
    num_a1 = input()
    print('Пожалуйста, введите 2-ое число: ', end='')
    num_b1 = input()
    print('Пожалуйста, укажите арифметическую операцию (* или +): ', end='')
    operation = input()
    # print('Метод 1: collections: ', end='')
    # calc(num_a, num_b, operation)
    print('Метод 2: ООП (старый вариант): ', end='')
    num_a = HexNumber(num_a1)
    num_b = HexNumber(num_b1)
    if operation == '+':
        print(f'{num_a.hex_list} + {num_b.hex_list} = {num_a + num_b}')
        print(f'Объем, занимаемый 1-м слагаемым: {round(asizeof.asizeof(num_a) / 1024, 5)} MiB')
        print(f'Объем, занимаемый 2-м слагаемым: {round(asizeof.asizeof(num_b) / 1024, 5)} MiB')
        print(f'Объем, занимаемый результатом: {round(asizeof.asizeof(num_a + num_b) / 1024, 5)} MiB')
    elif operation == '*':
        print(f'{num_a.hex_list} * {num_b.hex_list} = {num_a * num_b}')
        print(f'Объем, занимаемый 1-м множителем: {round(asizeof.asizeof(num_a) / 1024, 5)} MiB')
        print(f'Объем, занимаемый 2-м множителем: {round(asizeof.asizeof(num_b) / 1024, 5)} MiB')
        print(f'Объем, занимаемый результатом: {round(asizeof.asizeof(num_a * num_b) / 1024, 5)} MiB')
    else:
        print('Недопустимая операция.')
    print('Метод 2: ООП (оптимизированный с помощью __slots__ вариант): ', end='')
    num_a = HexNumberOpt(num_a1)
    num_b = HexNumberOpt(num_b1)
    if operation == '+':
        print(f'{num_a.hex_list} + {num_b.hex_list} = {num_a + num_b}')
        print(f'Объем, занимаемый 1-м слагаемым: {round(asizeof.asizeof(num_a) / 1024, 5)} MiB')
        print(f'Объем, занимаемый 2-м слагаемым: {round(asizeof.asizeof(num_b) / 1024, 5)} MiB')
        print(f'Объем, занимаемый результатом: {round(asizeof.asizeof(num_a + num_b) / 1024, 5)} MiB')
    elif operation == '*':
        print(f'{num_a.hex_list} * {num_b.hex_list} = {num_a * num_b}')
        print(f'Объем, занимаемый 1-м множителем: {round(asizeof.asizeof(num_a) / 1024, 5)} MiB')
        print(f'Объем, занимаемый 2-м множителем: {round(asizeof.asizeof(num_b) / 1024, 5)} MiB')
        print(f'Объем, занимаемый результатом: {round(asizeof.asizeof(num_a * num_b) / 1024, 5)} MiB')
    else:
        print('Недопустимая операция.')
