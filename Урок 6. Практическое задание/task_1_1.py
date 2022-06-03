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

Алгоритмы. Д/р №2, задание №2
"""
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(mem_diff)
        return res
    return wrapper


def counting(num, *, even=0, odd=0):
    if num == 0:
        return f'Количество четных: {even}, Количество нечетных: {odd}'
    if num % 10 % 2 == 0:
        return counting(num // 10, odd=odd, even=even + 1)
    if num % 10 % 2 == 1:
        return counting(num // 10, even=even, odd=odd + 1)


@decor
def counting_2(num):
    even, odd = 0, 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return f'Количество четных: {even}, Количество нечетных: {odd}'


@decor
def start_counting():
    counting(3456018645612818496412861204846315351467418663676741896453221837)


start_counting()  # 0.035 MiB
counting_2(3456018645612818496412861204846315351467418663676741896453221837)  # 0.0 MiB

# Использование цикла в функции снизило потребление памяти
