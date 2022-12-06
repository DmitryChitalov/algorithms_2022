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

Это файл для пятого скрипта
"""

import sys
from random import randint
from pympler import asizeof
from numpy import array


# Задание с курса "Основы языка Python".

src = [randint(0, 10) for _ in range(1000)]
tmp = set()
res = set()
for el in src:
    if el in tmp:
        res.discard(el)
        continue
    if not el in res:
        res.add(el)
    tmp.add(el)
print(res)

result = [num for num in src if num in res]
print(result)
print(f'Memory used by "src" list: {sys.getsizeof(src)} *getsizeof')
print(f'Memory used by "src" list: {asizeof.asizeof(src)} *asizeof')
print(f'Memory used by "result" list: {sys.getsizeof(result)} *getsizeof')
print(f'Memory used by "result" list: {asizeof.asizeof(result)} *asizeof')



src = array([randint(0, 100) for _ in range(1000)])
tmp = set()
res = set()
for el in src:
    if el in tmp:
        res.discard(el)
        continue
    if not el in res:
        res.add(el)
    tmp.add(el)
print(res)

result = array([num for num in src if num in res])
print(result)
print(f'Memory used by "src" numpy: {sys.getsizeof(src)} *getsizeof')
print(f'Memory used by "src" numpy: {asizeof.asizeof(src)} *asizeof')
print(f'Memory used by "result" numpy: {sys.getsizeof(result)} *getsizeof')
print(f'Memory used by "result" numpy: {asizeof.asizeof(result)} *asizeof')

# numpy для списка src дает явное приемущество по памяти, однако для списка result, наоборот увеличивает память
