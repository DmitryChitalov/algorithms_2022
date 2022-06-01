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
from memory_profiler import memory_usage, profile

"""
Изначальный вариант взял из текущего курса.
Задача: перевернуть число.
Урок 2, task 3
"""


def dec(func):
    def wrapper(*args):
        start = memory_usage()
        res = func(*args)
        return f'Заняло пямяти = {memory_usage()[0] - start[0]}'

    return wrapper


@dec
def get_rev(n):
    return func(n)


def func(num, reversed=''):
    if num == 0:
        return reversed
    reversed += str(num % 10)
    return func(num // 10, reversed)


@dec
def revers_while(enter_num, revers_num=''):
    while enter_num != 0:
        revers_num = revers_num + str(enter_num % 10)
        enter_num //= 10
    return revers_num


print(get_rev(123456789059823704558235236346547456645294689234465330))
print(revers_while(123456789059823704558235236346547456645294689234465330))

"""
Вывод:
        Рекурсия:
                Заняло пямяти = 0.1171875
        Цикл:
                Заняло пямяти = 0.0
        Повторные вызовы функции в рекурсивном методе существенно влияют на память т. к. результаты
        каждого вызова функции сохраняются в памяти. цикл и быстрее рекурсии и занимеет меньше памяти
"""
