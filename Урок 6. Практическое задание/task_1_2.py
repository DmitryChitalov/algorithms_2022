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

import hashlib
from uuid import uuid4
from memory_profiler import memory_usage

def memory_decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        func(args[0])
        m2 = memory_usage()
        return m2[0] - m1[0]
    return wrapper

'''
Скрипт из урока 3 задания 3. Положила его в функцию
'''

@memory_decor
def get_substrings(some_string):
    substrings = set()
    salt = str(uuid4().hex)
    for id in range(len(some_string)):
        end = len(some_string) if id == 0 else len(some_string) + 1
        for id2 in range(id + 1, end):
            substr = some_string[id:id2]
            hashed_substr = hashlib.sha256((salt + substr).encode('utf-8')).hexdigest()
            substrings.add(hashed_substr)
    return substrings

'''
В оптимизированной версии следующие изменения:
1. убрала переменную substr
2. заменила вывод обычных строк на вывод f-строк
'''

@memory_decor
def get_substrings_2(some_string):
    substrings = set()
    salt = str(uuid4().hex)
    for id in range(len(some_string)):
        end = len(some_string) if id == 0 else len(some_string) + 1
        for id2 in range(id + 1, end):
            hashed_substr = hashlib.sha256((salt + some_string[id:id2]).encode('utf-8')).hexdigest()
            substrings.add(hashed_substr)
    return substrings

some_string = 'abcdefg' * 100

print(get_substrings(some_string))
print(get_substrings_2(some_string))

'''
Мои результаты:

get_substrings()     - 0.203125
get_substrings_2()   - 0.171875

Оптимизированная версия занимает меньше памяти
'''
