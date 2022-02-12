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

Это файл для пятого скрипта
"""

# basics_Урок 2. task_2.

import random
from memory_profiler import profile


@profile
def concat_list(lst):
    my_list_2 = []
    for value in lst:
        if value.isdigit():
            my_list_2.append('"' + value.zfill(2) + '"')
        elif value[1::].isdigit():
            my_list_2.append('"' + value[0] + value[1::].zfill(2) + '"')
        else:
            my_list_2.append(value)
    return ' '.join(my_list_2)


@profile
def concat_list_v2(lst):
    def str_gen():
        for value in lst:
            if value.isdigit():
                yield f'"{value.zfill(2)}"'
            elif value[1::].isdigit():
                yield f'"{value[0]}{value[1::].zfill(2)}"'
            else:
                yield value

    return ' '.join(str_gen())


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_lc = [(''.join((random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(4)))) for i in range(100000)]
my_list.extend(my_lc)
concat_list(my_list)
concat_list_v2(my_list)

"""
Для наглядного анализа были применены следующие изменения:
    исходный скрипт "обёрнут" в функцию, 
    добавлен lc, который извлекается в исходный список для увеличения объёма.

В v2 конкатенация заменена f-строками, убран дублирующий список, сделан генератор.

Результаты замеров:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    40     26.0 MiB     26.0 MiB           1   @profile
    41                                         def concat_list(lst):
    42     26.0 MiB      0.0 MiB           1       my_list_2 = []
    43     27.2 MiB      0.0 MiB      100011       for value in lst:
    44     27.2 MiB      0.0 MiB      100010           if value.isdigit():
    45     27.2 MiB      0.0 MiB         602               my_list_2.append('"' + value.zfill(2) + '"')
    46     27.2 MiB      0.0 MiB       99408           elif value[1::].isdigit():
    47     27.2 MiB      0.0 MiB        1572               my_list_2.append('"' + value[0] + value[1::].zfill(2) + '"')
    48                                                 else:
    49     27.2 MiB      1.2 MiB       97836               my_list_2.append(value)
    50     28.2 MiB      1.0 MiB           1       return ' '.join(my_list_2)
    
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    53     26.6 MiB     26.6 MiB           1   @profile
    54                                         def concat_list_v2(lst):
    55     26.6 MiB      0.0 MiB           2       def str_gen():
    56     27.1 MiB      0.0 MiB      100011           for value in lst:
    57     27.1 MiB      0.0 MiB      100010               if value.isdigit():
    58     27.1 MiB      0.0 MiB        1204                   yield f'"{value.zfill(2)}"'
    59     27.1 MiB      0.0 MiB       99408               elif value[1::].isdigit():
    60     27.1 MiB      0.0 MiB        3144                   yield f'"{value[0]}{value[1::].zfill(2)}"'
    61                                                     else:
    62     27.1 MiB      0.5 MiB      195672                   yield value
    63     27.9 MiB      0.8 MiB           1       return ' '.join(str_gen())
"""
