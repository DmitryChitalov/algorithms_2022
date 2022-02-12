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

Это файл для четвертого скрипта
"""
# Курс основ, урок 6, задание 2.
# Из списка найти элементы кратные 3 , положительные , не кратные 4
from memory_profiler import profile
from random import randint
from numpy import array


@profile
def original():
    numbers = [randint(-200, 200) for i in range(10000)]
    res = [num for num in numbers if num > 0 and num % 3 == 0 and num % 4 != 0]
    del numbers
    return res


@profile
def optimized():
    numbers = array([randint(-200, 200) for i in range(10000)])
    res = array([num for num in numbers if num > 0 and num % 3 == 0 and num % 4 != 0])
    del numbers
    return res


print(original())
print(optimized())

"""
Помогло изпользование NumPy
До:    31.0 MiB      0.2 MiB       10003       numbers = [randint(-200, 200) for i in range(10000)]
После: 31.0 MiB      0.0 MiB       10003       numbers = array([randint(-200, 200) for i in range(10000)])
"""
