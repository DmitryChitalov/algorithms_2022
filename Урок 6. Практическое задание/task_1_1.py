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

"""
Алгоритмы и структуры данных на Python.
Урок 3, Задание 3:
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв
"""
from hashlib import sha256
from memory_profiler import profile
from numpy import array, empty


begin_str = "рараappppaaaaapaaaaappppaaaapapapрараappppaaaaapaaaaappppaaaapapapрараappppaaaaapaaaaappppaaaapapapрараappppaaaaapaaaaappppaaaapapap"


@profile
def fn_hash(str1):
    result_set = set()
    len_str = len(str1)
    for i in range(len_str):
        for j in range(i+1, len_str+1):
            result_set.add(sha256(str1[i:j].encode()).hexdigest())
    return f"Уникальных подстроек: {len(result_set)}"


@profile
def fn_hash1(str1):
    result_set = empty()
    len_str = len(str1)
    for i in range(len_str):
        for j in range(i+1, len_str+1):
            result_set.add(sha256(str1[i:j].encode()).hexdigest())
    return f"Уникальных подстроек: {len(result_set)}"




fn_hash(begin_str)
fn_hash1(begin_str)



