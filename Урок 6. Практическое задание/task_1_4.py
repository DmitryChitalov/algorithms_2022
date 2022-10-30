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

Это файл для четвертого скрипта
"""
# курс алгоритмы урок 5 задание 2
# сложение шестнадцатеричных чисел
from collections import defaultdict
from functools import reduce
from memory_profiler import memory_usage, profile


def sum_func(*args):
    sum_res = 0
    for value in args:
        sum_res += int(''.join(value), 16)
    return list(f'{sum_res:X}')


def map_sum(*args):
    sum_res = sum(map(lambda value: int(''.join(value), 16), args))
    return list(f'{sum_res:X}')


if __name__ == '__main__':
    first_number = '1DE5AFDC0E5F31D'
    second_number = '4EEFC7E8435D4BE9'

    hex_numbers = defaultdict(list)
    hex_numbers['first'] = list(first_number)
    hex_numbers['second'] = list(second_number)

    start = memory_usage()[0]
    sum_result = reduce(sum_func, hex_numbers.values())
    end = memory_usage()[0]
    memory_used = end - start
    print('Использовано памяти:', memory_used)
    print('сумма через цикл: ', sum_result)

    start = memory_usage()[0]
    sum_result_2 = reduce(map_sum, hex_numbers.values())
    end = memory_usage()[0]
    memory_used = end - start
    print('Использовано памяти:', memory_used)
    print('сумма через lambda функцию: ', sum_result_2)

# Использовано памяти: 0.01953125
# сумма через цикл:  ['5', '0', 'C', 'E', '2', '2', 'E', '6', '0', '4', '4', '3', '3', 'F', '0', '6']
# Использовано памяти: 0.0
# сумма через lambda функцию:  ['5', '0', 'C', 'E', '2', '2', 'E', '6', '0', '4', '4', '3', '3', 'F', '0', '6']

# С помощью встроенных функций sum и map, удалось добиться уменьшения используемой памяти
