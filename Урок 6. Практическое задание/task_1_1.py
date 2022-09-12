import collections
from collections import namedtuple
from recordclass import recordclass
from memory_profiler import memory_usage
import numpy as np

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

# неоптимизированное решение задания 5.1, алгоритмы:

def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper

@decor
def profit_counter():
    try:
        amount = int(input('Введите количество предприятий для расчета прибыли: '))
        avrg = 0
        s = 0
        dct = {}
        big_prft = []
        small_prft = []
        for i in range(amount):
            name = input('Введите название предприятия: ')
            try:
                profit = (input('Через пробел введите прибыль данного предприятия за'
                           ' каждый квартал(Всего 4 квартала): ')).split(' ')
                prft = [int(x) for x in profit]
                summa = sum(prft)
                prft.append(summa)
                dct[name] = prft
                s += summa
                avrg = s / amount
            except ValueError:
                print("Ошибка ввода! Вы ввели не числа!")
                profit_counter()

        for i, j in dct.items():
            Company = namedtuple(i, 'quater1 quater2 quater3 quater4 summa')
            try:
                i = Company._make(j)
                if i.summa >= avrg:
                    big_prft.append(Company.__name__)
                else:
                    small_prft.append(Company.__name__)
            except TypeError:
                print(("Ошибка ввода! Введите четыре числа через пробел!"))
                profit_counter()

        print(f'Средняя годовая прибыль всех предприятий: {avrg}')
        print(f'Предприятия, с прибылью выше (или равной) среднего значения: {big_prft}')
        if small_prft:
            print(f'Предприятия, с прибылью ниже среднего значения: {small_prft}')
        else:
            print("У кампаний одинаковая прибыль")
    except ValueError:
        print("Ошибка ввода! Вы ввели не число!")
        profit_counter()

if __name__ == '__main__':
    res, mem_diff = profit_counter()
    print(f"Выполнение заняло {mem_diff} Mib")

# оптимизированное решение:

@decor
def profit_counter_2():
    try:
        amount = int(input('Введите количество предприятий для расчета прибыли: '))
        avrg = 0
        s = 0
        dct = {}
        big_prft = []
        small_prft = []
        for i in range(amount):
            name = input('Введите название предприятия: ')
            try:
                profit = (input('Через пробел введите прибыль данного предприятия за'
                           ' каждый квартал(Всего 4 квартала): ')).split(' ')
                prft = [int(x) for x in profit]
                summa = sum(prft)
                prft.append(summa)
                dct[name] = prft
                s += summa
                avrg = s / amount
            except ValueError:
                print("Ошибка ввода! Вы ввели не числа!")
                profit_counter_2()

        for i, j in dct.items():
            Company = recordclass(i, 'quater1 quater2 quater3 quater4 summa')
            try:
                i = Company._make(j)
                if i.summa >= avrg:
                    big_prft.append(Company.__name__)
                else:
                    small_prft.append(Company.__name__)
            except TypeError:
                print(("Ошибка ввода! Введите четыре числа через пробел!"))
                profit_counter_2()

        print(f'Средняя годовая прибыль всех предприятий: {avrg}')
        print(f'Предприятия, с прибылью выше (или равной) среднего значения: {big_prft}')
        if small_prft:
            print(f'Предприятия, с прибылью ниже среднего значения: {small_prft}')
        else:
            print("У кампаний одинаковая прибыль")
    except ValueError:
        print("Ошибка ввода! Вы ввели не число!")
        profit_counter_2()

if __name__ == '__main__':
    res, mem_diff = profit_counter_2()
    print(f"Выполнение заняло {mem_diff} Mib")

""" При использовании namedtuple выполнение заняло 0.04Mib,
при использовании recordclass - 0.019Mib (в 2 раза меньшее потреблеие памяти).
0.04734375 Mib против 0.015625 Mib"""