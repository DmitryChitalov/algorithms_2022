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
import time

from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение {func} заняло {mem_diff} Mib")
        return res

    return wrapper


@memory
def my_revers(enter_num):
    my_list = []
    for el in reversed(str(enter_num)):
        my_list.append(el)
    return ''.join(my_list)


# Выполнение <function my_revers at 0x00000246DD455798> заняло 0.2890625 Mib

@memory
def my_revers_optimized(enter_num):
    for el in reversed(str(enter_num)):
        yield ''.join(el)


# Выполнение <function my_revers_optimized at 0x000001F1968753A8> заняло 0.00390625 Mib

n = 88 ** 8888
my_revers_optimized(n)
my_revers(n)
# my_gen = my_revers_optimized(n)
# get_elem = [elem for elem in my_gen]
# print(''.join(get_elem))

"""Здесь оптимизируем работу через ключевое слово yield. В данном случае в памяти не хранится вся
последовательность данных, а просто генерируется объект на каждый вызов данной функции, что существенно снижает
затраты памяти. Для наглядности передаю достаточно крепкое число))"""
