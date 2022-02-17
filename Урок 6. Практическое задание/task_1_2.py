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
import copy
import hashlib


from memory_profiler import profile


@profile
def test(text):
    hash_tabl = {}
    for n in range(len(text)):
        for i in range(len(text)):
            if text[i:n + 1:] != '' and text[i:n + 1:] != text:  # Можно убрать второе условие если нужна строка
                hash_tabl.setdefault(hashlib.sha256(text[i:n + 1:].encode()).hexdigest(), text[i:n + 1:])
    result = list(hash_tabl.values())
    del hash_tabl
    return result

# for el in test(input('Введите строку: ')):
#     print(el)

s = 'asdoihasiohdui'\
    'oashdahdsoihaoigjasdoijgoiadsjoigadsoigdasoihgouipahgoiadosigjasdo' \
    'ijgiadgoiahsdoghaosdhoihsaoifoiajsdfoija[jfdoisadjajsidopjasoipjdoiasdofihsadoighoa' \
    'sdijg[asdjgoipasdpofhsadoifhsapodifhopasidhfosdahf'
test(s)

"""
До:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    40     19.4 MiB     19.4 MiB           1   @profile
    41                                         def test(text):
    42     19.4 MiB      0.0 MiB           1       hash_tabl = {}
    43     26.2 MiB      0.0 MiB         214       for n in range(len(text)):
    44     26.2 MiB      0.4 MiB       45582           for i in range(len(text)):
    45     26.2 MiB      0.5 MiB       45369               if text[i:n + 1:] != '' and text[i:n + 1:] != text:  # Можно убрать второе условие если нужна строка
    46     26.2 MiB      5.9 MiB       22790                   hash_tabl.setdefault(hashlib.sha256(text[i:n + 1:].encode()).hexdigest(), text[i:n + 1:])
    47     26.2 MiB      0.0 MiB           1       return hash_tabl.values()
    
После:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    40     19.4 MiB     19.4 MiB           1   @profile
    41                                         def test(text):
    42     19.4 MiB      0.0 MiB           1       hash_tabl = {}
    43     26.2 MiB      0.0 MiB         214       for n in range(len(text)):
    44     26.2 MiB      1.6 MiB       45582           for i in range(len(text)):
    45     26.2 MiB      0.5 MiB       45369               if text[i:n + 1:] != '' and text[i:n + 1:] != text:  # Можно убрать второе условие если нужна строка
    46     26.2 MiB      4.8 MiB       22790                   hash_tabl.setdefault(hashlib.sha256(text[i:n + 1:].encode()).hexdigest(), text[i:n + 1:])                                        
    47     26.4 MiB      0.2 MiB           1       result = list(hash_tabl.values())
    48     25.2 MiB     -1.2 MiB           1       del hash_tabl
    49     25.2 MiB      0.0 MiB           1       return result
"""