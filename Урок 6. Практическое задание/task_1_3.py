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

Это файл для третьего скрипта

3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"], 
    "М": ["Мария"], "П": ["Петр"]
}
"""
from memory_profiler import memory_usage, profile
from pympler import asizeof
from random import random


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


def thesaurus(*args):
    my_dict = {}

    for i in range(len(args)):
        if my_dict.get(args[i][0]) is not None:
            list = my_dict[args[i][0]]
            list.append(args[i])
            my_dict.update({args[i][0]: list})
        else:
            my_dict.update({args[i][0]: [args[i]]})

    return my_dict


def sort_dict(dict_init):
    dict_sorted = {}
    list_keys = list(dict_init.keys())
    list_keys.sort()
    for i in list_keys:
        dict_sorted.update({i: dict_init[i]})
    print(dict_sorted)


def thesaurus2(*args):
    my_dict = {}

    for ar in args:
        if my_dict.get(ar[0]) is not None:
            words = my_dict[ar[0]]
            words.append(ar)
            my_dict.update({ar[0]: words})
        else:
            my_dict.update({ar[0]: [ar]})

    return my_dict


def sort_dict2(dict_init):
    dict_sorted = {}
    list_keys = list(dict_init.keys())
    list_keys.sort()
    for key in list_keys:
        dict_sorted.update({key: dict_init[key]})
    return dict_sorted





@memory
def func_call1():
    sort_dict(thesaurus(*gen()))
    print(asizeof.asizeof(thesaurus(*gen()))) # -> 649800


@memory
def func_call2():
    mydict = thesaurus2(*gen())
    print(sort_dict2(mydict))
    print(asizeof.asizeof(mydict)) # -> 648968


def gen():
    array = (chr(65+int(random()*25)) + chr(60+int(random()*25)) for i in range(10000))
    return array

func_call2()
# func_call1()
# func_call2()


#
# снижение размера памяти произошло в результате перехода от перебора по индексу к перебору самих элементов,
# а также использования одного и того же объекта для сортированного и несортированного словаря

# оригинал
# 649352 * 2
# Выполнение заняло 1.97265625 Mib

# оптимизация
# 648904
# Выполнение заняло 0.77734375 Mib

