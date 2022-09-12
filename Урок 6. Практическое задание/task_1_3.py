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

Это файл для третьего скрипта
"""

# Урок 5. Курс Алгоритмы.
# Задание 2.
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив,
# элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# 2) через ООП

from memory_profiler import profile
from numpy import array
from pympler import asizeof


# __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
class IncreaseNumbers:
    """ Сложениу и умножение двух шестнадцатеричных чисел """

    def __init__(self, num):
        self.num = list(num)
        print(f'объект list занимает {asizeof.asizeof(self.num)} байт.')
        #  При использовании списка массив занимает более, чем в 2 раза больше места в памяти, чем
        #  при использовании функции array() из библиотеки NumPy.

    def __repr__(self):
        return self.num

    def __str__(self):
        return f'Число сохранено : {self.num}'

    def __add__(self, other):
        self.num = ''.join(self.num)
        other.num = ''.join(other.num)
        add_nums = list(hex(int(self.num, 16) + int(other.num, 16)).upper())
        print(f'объект list занимает {asizeof.asizeof(add_nums)} байт.')
        #  При использовании списка массив занимает более, чем в 2 раза больше места в памяти, чем
        #  при использовании функции array() из библиотеки NumPy.
        return f'Сумма чисел: {add_nums[2:]}'

    def __mul__(self, other):
        self.num = ''.join(self.num)
        other.num = ''.join(other.num)
        mul_nuns = list(hex(int(self.num, 16) * int(other.num, 16)).upper())
        #  При использовании списка массив занимает более, чем в 2 раза больше места в памяти, чем
        #  при использовании функции array() из библиотеки NumPy.
        print(f'объект list занимает {asizeof.asizeof(mul_nuns)} байт.')
        return f'Произведение - {mul_nuns[2:]}'


# __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
class IncreaseNumbersSlots:
    """ Сложениу и умножение двух шестнадцатеричных чисел """

    __slots__ = ['num']  # воспользовалась конструкции __slots__ при определении класса.

    #  В результате использования конструкции __slots__ при определении класса и
    #  функцию array() из библиотеки NumPy
    #  уменьшился общий размер создаваемого объекта класса более, чем в 2 раза.

    def __init__(self, num):
        self.num = array(list(num))
        print(f'объект array занимает {asizeof.asizeof(self.num)} байт.')
        #  При использовании функции array() из библиотеки NumPy
        #  массив стал занимать более, чем в 2 раза меньше места в памяти.

    def __repr__(self):
        return self.num

    def __str__(self):
        return f'Число сохранено : {self.num}'

    def __add__(self, other):
        self.num = ''.join(self.num)
        other.num = ''.join(other.num)
        add_nums = array(list(hex(int(self.num, 16) + int(other.num, 16)).upper()))
        print(f'объект array занимает {asizeof.asizeof(add_nums)} байт.')
        #  При использовании функции array() из библиотеки NumPy
        #  массив стал занимать более, чем в 2 раза меньше места в памяти.
        return f'Сумма чисел: {add_nums[2:]}'

    def __mul__(self, other):
        self.num = ''.join(self.num)
        other.num = ''.join(other.num)
        mul_nuns = array(list(hex(int(self.num, 16) * int(other.num, 16)).upper()))
        print(f'объект array занимает {asizeof.asizeof(mul_nuns)} байт.')
        #  При использовании функции array() из библиотеки NumPy
        #  массив стал занимать более, чем в 2 раза меньше места в памяти.
        return f'Произведение - {mul_nuns[2:]}'


if __name__ == '__main__':
    # __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
    @profile
    def sum_and_mul(my_num):  # Исполнение скрипта помещено в функцию для производства замеров.
        # first_number = input('Введите первое число: ')
        first_number = my_num
        first_num = IncreaseNumbers(first_number)
        print(first_num)
        print(f'Объект класса IncreaseNumbers(first_number) занимает: {asizeof.asizeof(first_num)} байт.')
        # second_number = input('Введите второе число: ')
        second_number = my_num
        second_num = IncreaseNumbers(second_number)
        print(second_num)
        print(f'Объект класса IncreaseNumbers(second_num) занимает: {asizeof.asizeof(second_num)} байт.')
        print(first_num + second_num)
        print(first_num * second_num)
        return "Все"


    # __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
    @profile
    def sum_and_mul_new(my_nam):
        # first_number = input('Введите первое число: ')
        first_number = my_nam
        first_num = IncreaseNumbersSlots(first_number)
        print(first_num)
        print(f'Объект класса IncreaseNumbersSlots(first_num) занимает: {asizeof.asizeof(first_num)} байт.')
        # second_number = input('Введите второе число: ')
        second_number = my_nam
        second_num = IncreaseNumbersSlots(second_number)
        print(second_num)
        print(f'Объект класса IncreaseNumbersSlots(second_num) занимает: {asizeof.asizeof(second_num)} байт.')
        print(first_num + second_num)
        print(first_num * second_num)
        return "Все"


    # __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
    sum_and_mul(str(sum(i ** i for i in range(700))))
    # Использование декоратора @profiler из профилировщика memory_profiler
    # проблем с использованием памяти при работе скрипта не выявляет.
    # Increment практически везде 0, за исключением вычисления произведения (0,1 MiB).
    # Значение Mem usage практически не меняетя.
    # Оно увеличивается на 0,1 MiB при создании первого объекта класса IncreaseNumbers (без слота),
    # и при вычислении произведения чисел (строки 129, 137).
    # После завершения скрипта Mem usage увеличилось на 0.2 MiB.

    # __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
    sum_and_mul_new(str(sum(i ** i for i in range(700))))
    # Использование декоратора @profiler из профилировщика memory_profiler
    # проблем с использованием памяти при работе скрипта не выявляет.
    # Increment везде 0. Mem usage не меняется.
