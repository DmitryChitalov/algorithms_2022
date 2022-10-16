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

"""Профилировка затрат памяти"""

from copy import deepcopy
from memory_profiler import profile
import hashlib

"1 Mebibyte = 1048576 Bytes"


# Task 3_3.
# Определить количество различных (уникальных) подстрок
# с использованием хеш-функции

@profile
def count():
    s = 'раdfghdfmsergesrgesgesgdgbfgbsdfgghnmdрараdfghdfmsergesrgesgesgdgbfgbsdfgghnmdрараdfghdfmsergesrgesgesgdgbfgbsdfgghnmdрараdfghdfmsergesrgesgesgdgbfgbsdfgghnmdрараdfghdfmsergesrgesgesgdgbfgbsdfgghnmdра'
    n = len(s)
    my_set = set()
    my_hash_set = set()
    for el in range(n):
        for i in range(n + 1):
            substring = s[el:i]
            if substring != '' and substring != s:
                my_set.add(substring)
                my_hash = hashlib.sha256(substring.encode()).hexdigest()
                my_hash_set.add(my_hash)
    print(f'{s} - {len(my_hash_set)} уникальных подстрок.')


@profile
def count_2():
    s = 'раdfghdfmsergesrgesgesgdgbfgbsdfgghnmdрараdfghdfmsergesrgesgesgdgbfgbsdfgghnmdрараdfghdfmsergesrgesgesgdgbf' \
        'gbsdfgghnmdрараdfghdfmsergesrgesgesgdgbfgbsdfgghnmdрараdfghdfmsergesrgesgesgdgbfgbsdfgghnmdра'
    n = len(s)
    my_set = set()
    my_hash_set = set()
    for el in range(n):
        for i in range(n + 1):
            substring = s[el:i]
            if substring != '' and substring != s:
                my_set.add(substring)
                my_hash = hashlib.sha256(substring.encode()).hexdigest()
                my_hash_set.add(my_hash)
    print(f'{s} - {len(my_hash_set)} уникальных подстрок.')
    del my_set
    del my_hash_set


if __name__ == "__main__":
    count()
    count_2()

# в этом примере мы оптимизируем затраты памяти с помощью удаления из памяти ненужных данных
