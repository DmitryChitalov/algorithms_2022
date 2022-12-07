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

from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args):
        mem_1 = memory_usage(max_usage=True)
        res = func(*args)
        mem_2 = memory_usage(max_usage=True)
        mem_diff = mem_2 - mem_1
        return res, mem_diff
    return wrapper


@memory
def convert_time_old(duration: str):
    """Исходный скрипт"""
    duration = int(duration)
    result = str()
    if duration < 60:
        result = str(duration) + ' сек'
    if duration >= 60:
        result = str(duration // 60) + ' мин ' + str(duration % 60) + ' сек'
    if duration < 86400:
        hours = duration // 3600
        minutes = (duration - 3600 * hours) // 60
        seconds = duration - 3600 * hours - 60 * minutes
        result = str(hours) + ' ч ' + str(minutes) + ' мин ' + str(seconds) + ' сек'
    if duration >= 86400:
        days = duration // 86400
        hours = (duration - 86400 * days) // 3600
        minutes = (duration - 86400 * days - 3600 * hours) // 60
        seconds = duration - 86400 * days - 3600 * hours - 60 * minutes
        result = str(days) + ' сут ' + str(hours) + ' ч ' + str(minutes) + ' мин ' + str(seconds) + ' сек'
    return result


@memory
def convert_time_new(duration: str):
    """Оптимизированный за счет f-строк скрипт"""
    duration = int(duration)
    result = str()
    if duration < 60:
        result = f'{duration} сек'
    if duration >= 60:
        result = f'{duration // 60} мин {duration % 60} сек'
    if duration < 86400:
        hours = duration // 3600
        minutes = (duration - 3600 * hours) // 60
        seconds = duration - 3600 * hours - 60 * minutes
        result = f'{hours} ч {minutes} мин {seconds} сек'
    if duration >= 86400:
        days = duration // 86400
        hours = (duration - 86400 * days) // 3600
        minutes = (duration - 86400 * days - 3600 * hours) // 60
        seconds = duration - 86400 * days - 3600 * hours - 60 * minutes
        result = f'{days} сут {hours} ч {minutes} мин {seconds} сек'
    return result


print('\nСкрипт №1 из д/з №1 курса "Основы Python".\nФункция, которая переводит временной интервал'
      ' в секундах в формат "сутки, часы, минуты, секунды".')
user_duration = input('Введите временной интервал в секундах: ')
print('Работу какой функции вы хотите проверить? (1 - исходная, 2 - оптимизированная): ', end='')
mode = input()
if mode == '1':
    converted, mem = convert_time_old(user_duration)
    print(f'Результат работы исходной функции: {converted}. ', end='')
    print(f'Использование памяти {mem} MiB')
elif mode == '2':
    converted, mem = convert_time_new(user_duration)
    print(f'Результат работы оптимизированной функции: {converted}. ', end='')
    print(f'Использование памяти {mem} MiB')
