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

from numpy import array
from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


# ДЗ 2, Задание 5 из Основ. Вывести из списка цены на товары в формате "x руб. yy коп."
# Без оптимизации:

prices = [56.4, 23.57, 24, 67.89, 1.2, 123.68, 90, 34.3, 46.50, 80.01, 90.00, 68, 0, 100, 56.4, 23.57, 24,
          67.89, 1.2, 123.68, 90, 34.3, 46.50, 80.01, 90.00, 68, 0, 100]


@memory
def get_price(prices):
    for i in prices:
        rub = int(i)
        kop = int(round((i % 1 * 100), 2))
        print(f'{rub} руб. {kop if kop >= 10 else str(0) + str(kop)} коп.')


print(get_price(prices))

# С оптимизацией:

prices_arr = array([56.4, 23.57, 24, 67.89, 1.2, 123.68, 90, 34.3, 46.50, 80.01, 90.00, 68, 0, 100, 56.4, 23.57, 24,
                    67.89, 1.2, 123.68, 90, 34.3, 46.50, 80.01, 90.00, 68, 0, 100])


@memory
def get_price_arr(prices_arr):
    for i in prices:
        rub = int(i)
        kop = int(round((i % 1 * 100), 2))
        print(f'{rub} руб. {kop if kop >= 10 else str(0) + str(kop)} коп.')


print(get_price_arr(prices_arr))

# До оптимизации: 0.0117 MiB, после оптимизации: 0.0 MiB.
# Что изменил: Использовал array из NumPy вместо стандартного списка
