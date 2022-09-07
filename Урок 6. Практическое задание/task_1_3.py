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


"""
Python Basic - https://github.com/Frvzr/gb_python_basics/blob/master/Koposhilov_Ivan_dz_2/task_2_4.py

# На вход будет подаваться список, содержащий искажённые данные с должностями и именами сотрудников:
# Известно, что имя сотрудника всегда в конце строки!
# Обработать все элементы списка и вернуть в качестве результата список, состоящий из фраз вида:
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
"""




from memory_profiler import profile, memory_usage
from collections import namedtuple
def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@profile
def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = []
    for item in list_in:
        join_item = ''.join(item)
        split_item = join_item.split()
        list_out.append(f'Привет, {split_item[-1].capitalize()}!')
    return list_out

# Оптимизированная функция


@decor
def convert_name_extract_3(list_in: list):
    """
    Генератор
    """
    list_out = [f'Привет, {"".join(split_item).split()[-1].capitalize()}!'
                for split_item in list_in]
    yield list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']


if __name__ == "__main__":
    convert_name_extract(my_list)

    generator, mem_diff = convert_name_extract_3(my_list)
    for item in generator:
        print(item, end='')
    print(f'\nВыполнение заняло {mem_diff} Mib')
"""
В оптимизированной функции использовал LC + генератор, результат 0.00390625 Mib

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    72     19.6 MiB     19.6 MiB           1   @profile
    73                                         def convert_name_extract_2(list_in: list) -> list:
    75     19.6 MiB      0.0 MiB          12       list_out = [f'Привет, {"".join(split_item).split()[-1].capitalize()}!'
    76     19.6 MiB      0.0 MiB           1                   for split_item in list_in]
    77     19.6 MiB      0.0 MiB           1       return list_out


['Привет, Игорь!', 'Привет, Марина!', 'Привет, Николай!', 'Привет, Аэлита!']
Выполнение заняло 0.00390625 Mib
"""
