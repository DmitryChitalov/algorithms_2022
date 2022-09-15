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

Это файл для второго скрипта
"""
from memory_profiler import profile
from collections import deque

# class DequeClass:
#     def __init__(self):
#         self.elems = []
#
#     def is_empty(self):
#         return self.elems == []
#
#     def add_to_front(self, elem):
#         self.elems.append(elem)
#
#     def add_to_rear(self, elem):
#         self.elems.insert(0, elem)
#
#     def remove_from_front(self):
#         return self.elems.pop()
#
#     def remove_from_rear(self):
#         return self.elems.pop(0)
#
#     def size(self):
#         return len(self.elems)
@profile
def pal_checker(string):
    dc_obj = deque()
    str = string.replace(' ', '')
    for letter in str:
        dc_obj.append(letter)

    still_equal = True

    while len(dc_obj) > 1 and still_equal:
        first = dc_obj.pop()
        last = dc_obj.popleft()
        if first != last:
            still_equal = False

    return still_equal

@profile
def pal_checker2(string): # вариант проще. Без DequeClass
    string = string.replace(' ', '')
    reverse_string = string[::-1]
    if string == reverse_string:
        return True
    return False



print(pal_checker("лом о смокинги гни комсомол"))
print(pal_checker2("лом о смокинги гни комсомол"))


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    56     14.9 MiB     14.9 MiB           1   @profile
    57                                         def pal_checker(string):
    58     14.9 MiB      0.0 MiB           1       dc_obj = DequeClass()
    59     14.9 MiB      0.0 MiB           1       tup = string.replace(' ', '')
    60     14.9 MiB      0.0 MiB          24       for el in tup:
    61     14.9 MiB      0.0 MiB          23           dc_obj.add_to_rear(el)
    62                                         
    63     14.9 MiB      0.0 MiB           1       still_equal = True
    64                                         
    65     14.9 MiB      0.0 MiB          12       while dc_obj.size() > 1 and still_equal:
    66     14.9 MiB      0.0 MiB          11           first = dc_obj.remove_from_front()
    67     14.9 MiB      0.0 MiB          11           last = dc_obj.remove_from_rear()
    68     14.9 MiB      0.0 MiB          11           if first != last:
    69                                                     still_equal = False
    70                                         
    71     14.9 MiB      0.0 MiB           1       return still_equal




Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    73     15.0 MiB     15.0 MiB           1   @profile
    74                                         def pal_checker2(string): # вариант проще. Без DequeClass
    75     15.0 MiB      0.0 MiB           1       string = string.replace(' ', '')
    76     15.0 MiB      0.0 MiB           1       reverse_string = string[::-1]
    77     15.0 MiB      0.0 MiB           1       if string == reverse_string:
    78     15.0 MiB      0.0 MiB           1           return True
    79                                             return False
    
Так же код, не использующий специально написанный класс и использующий встроенные инструменты, заеимает больше памяти.   
"""