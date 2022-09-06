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
from memory_profiler import profile
"""
Взял задание с курса алгоритмы 
Оптимизировавал решение использовав простой цикл место рекурсии
Убрал дополнительную проверку if
"""


def funct(k):
    n = k - 1
    return ((-1) ** n) / (2 ** n)


"""
Старое решение
"""


@profile
def recurs(n, summ=0):
    if n != 0:
        summ = summ + funct(n)
        return recurs(n - 1, summ)
    else:
        return summ


"""
Новое решение
"""


@profile
def func_for(n):
    summ = 0
    for i in range(n):
        summ = summ + funct(i + 1)
    return summ


@profile
def func_for1(n):
    summ = 0
    i = 0
    while i != n:
        summ = summ + funct(i + 1)
        i += 1

    return summ


print(recurs(100))
print("For - ", func_for(100))
print("While - ", func_for1(100))
