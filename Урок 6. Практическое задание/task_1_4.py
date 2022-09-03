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

Это файл для четвертого скрипта
"""
from memory_profiler import memory_usage, profile
from numpy import array, append, delete
from uuid import uuid4
from pympler import asizeof

# lesson 1 task 3
#@profile
def test1():
    m1 = memory_usage()
    our_dict = {}
    for i in range(100000):
        our_dict[(uuid4().hex)] = uuid4().int

    print(asizeof.asizeof(our_dict))
    def biggest_value_in_dict(dict):
        new_list = []
        for i in range(3):
            richest_company, biggest_value = list(dict.items())[0]
            for item in dict:
                if dict[item] > biggest_value:
                    biggest_value = dict[item]
                    richest_company = item
            new_list.append(richest_company)
            dict.pop(richest_company)
        return new_list

    biggest_value_in_dict(our_dict)

    m2 = memory_usage()
    mem_usage = m2[0] - m1[0]
    print(f"Выполнение заняло {mem_usage} Mib")


#@profile
def test2():
    m3 = memory_usage()

    names_array = array([uuid4().hex for i in range(100000)])
    prof_array = array([uuid4().int for i in range(100000)])
    print(asizeof.asizeof(names_array)+asizeof.asizeof(prof_array))
    def biggest_value_in_array(names_array, prof_array):
        new_list = []
        for i in range(3):
            idx = 0
            richest_company, biggest_value = names_array[0], prof_array[0]
            for j in range(len(prof_array)):
                if prof_array[j] > biggest_value:
                    biggest_value = prof_array[j]
                    richest_company = names_array[j]
                    idx = j
            new_list.append(richest_company)
            delete(names_array, idx)
            delete(prof_array, idx)
        return new_list

    biggest_value_in_array(names_array, prof_array)
    m4 = memory_usage()
    mem_usage = m4[0] - m3[0]
    print(f"Выполнение заняло {mem_usage} Mib")

test1()
test2()

"""
Вывод. Работа функции оптимизирована с помощью использования 2 массивов array вместо словаря. 
До оптимизации:
Выполнение заняло 20.98046875 Mib
После оптимизации:
Выполнение заняло 15.10546875 Mib
"""