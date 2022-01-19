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

Это файл для первого скрипта
"""
#src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#result = [i for i in src if src.count(i) == 1]
#print(result)

from random import randint
from memory_profiler import profile
src = [randint(0, 1000000) for i in range(1000000)]

@profile
def for_list():
    result = [elem for idx, elem in enumerate(src) if elem > src[idx - 1] and idx > 0]
    return result
for_list()
@profile
def for_generator():
    result = (elem for idx, elem in enumerate(src) if elem > src[idx - 1] and idx > 0)
    return result
for_generator()

"""
В первой функции 61.8 MIB 0.0 MIB во второй функции 57.9 MIB 0.0 MIB 
"""