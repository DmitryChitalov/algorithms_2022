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

Это файл для пятого скрипта
"""


"""ДЗ 2.2"""


from memory_profiler import profile
from random import randint


def ch_even(n, oddnum=0, evennum=0):
    if (n % 2) == 1:
        oddnum += 1
    else:
        evennum += 1
    return oddnum, evennum


@profile
def num_dig(a):
    def num_dig1(n, oddnum=0, evennum=0):
        if len(str(n)) == 1:
            oddnum, evennum = ch_even(n, oddnum, evennum)
            return oddnum, evennum
        else:
            oddnum, evennum = ch_even(n, oddnum, evennum)
            n //= 10
            return num_dig1(n, oddnum, evennum)
    result = num_dig1(a)
    return result


m = randint(10e200, 10e201)
print(num_dig(m))

"""Без рекурсии экономия 0.2MiB (15 строка)"""
@profile
def num_dig2(n, oddnum=0, evennum=0):
    while len(str(n)) != 1:
        oddnum, evennum = ch_even(n, oddnum, evennum)
        n //= 10
    oddnum, evennum = ch_even(n, oddnum, evennum)
    return oddnum, evennum


print(num_dig2(m))