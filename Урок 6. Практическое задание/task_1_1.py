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
from numpy import array

'''
Dz 2, task 5. Основы языка Python 
Выполнил задачу я в таком виде, т.к. не знал что такое ф-ции,
но для выполнения текущего д/з усовершенствовал решение. 

original_list = [57.8, 46.51, 97, 33, 44.2, 11, 12.1, 32, 22.1, 15.1, 89, 7]
correct_list = []

for i in original_list:
    r = int(i)
    kk = int(round((i - r), 2)*10)
    correct_list.append(f'{r:02d} руб. {kk:02d} коп.')

print(*correct_list, sep =', ')
'''


#  Исходный код
@profile
def converter():
    original_list = [i for i in range(10000)]
    correct_list = []
    for i in original_list:
        rub = int(i)
        kop = int(round((i - rub), 2) * 10)
        correct_list.append(f'{rub:02d} руб. {kop:02d} коп.')
    return correct_list


#  Оптимизированный код
@profile
def converter_numpy():
    original_list = array([i for i in range(10000)])
    correct_list = []
    for i in original_list:
        rub = int(i)
        kop = int(round((i - rub), 2) * 10)
        correct_list.append(f'{rub:02d} руб. {kop:02d} коп.')
    return correct_list


if __name__ == '__main__':
    converter()
    converter_numpy()

'''
=============================================================
    53     30.9 MiB     30.9 MiB           1   @profile
    54                                         def filtrus():
    55     31.4 MiB      0.5 MiB       10003       original_list = [i for i in range(10000)]
    56     31.4 MiB      0.0 MiB           1       correct_list = []
    57     32.5 MiB      1.1 MiB       10001       for i in original_list:
    58     32.5 MiB      0.0 MiB       10000           rub = int(i)
    59     32.5 MiB      0.0 MiB       10000           kop = int(round((i - rub), 2) * 10)
    60     32.5 MiB      0.1 MiB       10000           correct_list.append(f'{rub:02d} руб. {kop:02d} коп.')
    61     32.5 MiB      0.0 MiB           1       return correct_list
'''

'''
=============================================================
    64     30.9 MiB     30.9 MiB           1   @profile
    65                                         def filtrus_numpy_2():
    66     31.3 MiB      0.4 MiB       10003       original_list_numpy = numpy.array([i for i in range(10000)])
    67     31.3 MiB      0.0 MiB           1       correct_list_numpy = []
    68     32.2 MiB      0.8 MiB       10001       for i in original_list_numpy:
    69     32.2 MiB      0.0 MiB       10000           rub = int(i)
    70     32.2 MiB      0.0 MiB       10000           kop = int(round((i - rub), 2) * 10)
    71     32.2 MiB      0.1 MiB       10000           correct_list_numpy.append(f'{rub:02d} руб. {kop:02d} коп.')
    72     32.2 MiB      0.0 MiB           1       return correct_list_numpy
'''

'''
Как мы видем, с помощью библиотеки NumPy и ф-ции array удалость добиться 
уменьшения выделяемой памяти.
'''
