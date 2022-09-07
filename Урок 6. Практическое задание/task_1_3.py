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

Это файл для третьего скрипта
"""
from memory_profiler import memory_usage

"""
Курс основ python урок 2 задание 2:
Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками 
(добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
"""

def dec(func):
    def wrapper():
        start = memory_usage()
        res = func()
        print(f'Заняло пямяти = {memory_usage()[0] - start[0]}')
        return res
    return wrapper


@dec
def original():
    list_1 = [str(x) for x in range(10000)]
    num_list = []
    for i in list_1:
        if i[0] in '+' or i[0] in '-':
            a = list_1.index(i)
            num_list.append(i)
            list_1[a] = 'isdunfi'
            list_1.insert(a, '"')
            a += 2
            list_1.insert(a, '"')

        elif i.isdigit():
            a = list_1.index(i)
            num_list.append(i)
            list_1[a] = 'isdunfi'
            list_1.insert(a, '"')
            a += 2
            list_1.insert(a, '"')

    num = ''
    for i in num_list:
        if i[0] == '+':
            num += f'{i[0]}{int(i):02d}.'
        elif i[0] == '-':
            num += f"{i[0]}{int(i.replace('-', '', 1)):02d}."
        else:
            num += f'{int(i):02d}.'

    num1 = num.split('.')

    inx = 0
    for i in list_1:
        if i == 'isdunfi':
            a = list_1.index(i)
            list_1[a] = num1[inx]
            inx += 1

    my_str = ' '.join(list_1)
    print(my_str)


@dec
def optimized():
    lst = (str(x) for x in range(10000))
    for i in lst:
        if i.isdigit():
            print(f'"{i.zfill(2)}"', end=' ')
        elif i[0] == '+' or i[0] == '-':
            print(f'"{i.zfill(3)}"', end=' ')
        else:
            print(i, end=' ')
    print()


original()
optimized()


"""
Вывод: Используя генератор получилось выйграть в памяти но не на много
"""