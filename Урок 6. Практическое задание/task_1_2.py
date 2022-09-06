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

# Урок 3, задание 3

import hashlib
from memory_profiler import memory_usage


def mem_profiler(function):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        result = function(*args, **kwargs)
        m2 = memory_usage()
        print(m2[0] - m1[0])
        return result
    return wrapper


@mem_profiler
def func(string):
    hashes = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j + 1]
            if substring != string:
                hashes.add(hashlib.sha256(substring.encode(encoding='utf-8')).hexdigest())
    return len(hashes)


@mem_profiler
def func_opt(string):
    hashes = list()
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j + 1]
            if substring != string:
                hash_str = hashlib.sha256(substring.encode(encoding='utf-8')).hexdigest()
                if hash_str not in hashes:
                    hashes.append(hash_str)
    res = len(hashes)
    del hashes
    return res


line = 'papkhjsdsfgsdsfkfhjkaertyugfkgndfkjgnsdkfgjsdkfgjsdkfa'
# func(line)
func_opt(line)

"""
Для уменьшения потребления памяти заменил множество на список,
а также перед завершением выполнения функции удалил ссылку на него после использования.
"""
