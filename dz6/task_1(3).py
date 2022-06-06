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
from memory_profiler import profile
# from memory_profiler import memory_usage


# Декоратор для замера памяти скрипта
# def mib_size(func):
#     def wrapper(*args):
#         m1 = memory_usage()
#         res = func(*args)
#         m2 = memory_usage()
#         mem_dif = m2[0] - m1[0]
#         return mem_dif, res
#
#     return wrapper


# Скрипт урока №5 задание №2 (шестнадцатиричный калькулятор) вариант решения через ООП
# @mib_size
@profile
def func_sum():
    class SumMy:
        def __init__(self, num_1, num_2):
            self.num_1 = int(num_1, 16)
            self.num_2 = int(num_2, 16)

        def __add__(self):
            res = (hex(self.num_1 + self.num_2))[2:]
            return [char for char in res]

        def __mul__(self):
            res = (hex(self.num_1 * self.num_2))[2:]
            return [char for char in res]

    operation = input('Введите желаемую операцию "+" или "*": ')
    num_3 = input('Введите первое число: ')
    num_4 = input('Введите второе число: ')
    a = SumMy(num_3, num_4)
    if operation == '+':
        return a.__add__()
    else:
        return a.__mul__()


# @mib_size
@profile
def func_sum_optimize():
    class SumMy:
        __slots__ = ['num_1', 'num_2']

        def __init__(self, num_1, num_2):
            self.num_1 = int(num_1, 16)
            self.num_2 = int(num_2, 16)

        def __add__(self):
            res = (hex(self.num_1 + self.num_2))[2:]
            return [char for char in res]

        def __mul__(self):
            res = (hex(self.num_1 * self.num_2))[2:]
            return [char for char in res]

    operation = input('Введите желаемую операцию "+" или "*": ')
    num_3 = input('Введите первое число: ')
    num_4 = input('Введите второе число: ')
    a = SumMy(num_3, num_4)
    if operation == '+':
        return a.__add__()
    else:
        return a.__mul__()


if __name__ == '__main__':
    func_sum()
    # print(f'Выполнение заняло {mem_dif_1} Mib')
    func_sum_optimize()
    # print(f'Выполнение оптимизированного скрипта заняло {mem_dif_optimize} Mib')

'''
замер выполнял через свой декоратор
Оптимизировал скрипт при помощи __slots__, проверил на одинаковых данных,
не оптимизированный скрипт занимал 0.02734375 Mib памяти, 
оптимизированный 0.0 Mib

замер черех @profile:
55     19.8 MiB      0.1 MiB         662               return [char for char in res]
замер оптимизированного скрипта через @profile:
81     19.8 MiB     -0.0 MiB           1               res = (hex(self.num_1 * self.num_2))[2:]
Тут тоже видно что использование __slots__ экономит память.
'''
