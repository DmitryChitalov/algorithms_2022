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
import collections

array = list(range(100000))


@profile
def func_4(array):
    counter = collections.Counter(array)
    m = counter.most_common(1)
    return f'Чаще всего встречается число {m[0][0]}, ' \
           f'оно появилось в массиве {m[0][1]} раз(а)'

func_4(array[:])


@profile
def func_3(array):
    m = 0
    num = 0
    for i in array:
        i = array.pop()
        count = array.count(i)+1
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'
func_3(array[:])

'''
из задания 4-4, суть в том, что при работе с коллекцией, с объемом списка возврастает объем используемой памяти,
при обходе циклом списка с удалением элемента, память практически не расходуется.
'''