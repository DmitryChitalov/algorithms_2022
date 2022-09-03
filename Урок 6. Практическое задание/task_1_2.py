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
from memory_profiler import memory_usage
from recordclass import recordclass

#lesson 3 task 4

import hashlib
from uuid import uuid4


class CacheWeb:
    def __init__(self):
        self.web_dict = {}
        self.salt_dict = {}

    def web_to_cache(self, url):
        if self.web_dict.get(url):
            return self.web_dict[url]
        else:
            salt = uuid4().hex
            self.salt_dict.setdefault(url, salt)
            self.web_dict.setdefault(url, hashlib.sha256(url.encode('utf-8') + salt.encode()).hexdigest())

urlrec = recordclass('urlrec', ('salt', 'hash'))
class CacheWebO:
    __slots__ = ['web_dict', 'salt_dict']

    def __init__(self):
        self.web_dict = {}

    def web_to_cache(self, url):
        if self.web_dict.get(url):
            return self.web_dict[url].hash
        else:
            salt = uuid4().hex
            self.web_dict[url] = urlrec(salt=salt, hash=hashlib.sha256(url.encode('utf-8') + salt.encode()).hexdigest())


m1 = memory_usage()
our_web_cache = CacheWeb()
for i in range(1000000):
    our_web_cache.web_to_cache(uuid4().hex)
m2 = memory_usage()
print(f"Выполнение заняло {m2[0] - m1[0]} Mib")


m3 = memory_usage()
our_web_cache2 = CacheWebO()
for i in range(1000000):
    our_web_cache2.web_to_cache(uuid4().hex)
m4 = memory_usage()
print(f"Выполнение заняло {m4[0] - m3[0]} Mib")


'''
Вывод. Использование recordclass позволило сократить расход памяти. Использование слотов не повлияло на память.
До оптимизации:
Выполнение заняло 386.828125 Mib
После оптимизации:
Выполнение заняло 377.60546875 Mib
'''


