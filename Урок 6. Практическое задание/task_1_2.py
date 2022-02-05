"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

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
# Урок 2 задание 2
from memory_profiler import profile
number = 3478004182736455068704


@profile
def rec(num):
    def even_odd_recur(num, even=[], odd=[]):
        if num == 0:
            return even, odd
        else:
            n = num % 10
            num = num // 10
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
            return even_odd_recur(num,even,odd)


@profile
def even_odd_cycle(num, even=[], odd=[]):
    nums = str(num)
    for i in range(len(nums)):
        if int(nums[i]) % 2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    return even, odd


rec(number)
even_odd_cycle(number)
