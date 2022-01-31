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

Это файл для четвертого скрипта
"""


# Урок 1 Задание 4
# Для оптимизации возьмем часть создание пользователей через класс. 
# При большом количестве пользователей имеет смысл сделать их черезе слоты. 
# Тогда потребление памяти уменьшается.
# Например при 10000 пользователей 3.33203125 Mib против 2.375 Mib
from memory_profiler import memory_usage


class User:
    def __init__(self, login, password, *, is_active):
        self.login = login
        self.password = password
        self.is_active = is_active


class WebResource:
    users = {}


def profiler():
    web_resource = WebResource()
    for u in range(10**4):
        u = User(f'Ivanov{u}', f'{u}{u}', is_active=True)
        web_resource.users[u.login] = u
    return web_resource

m1 = memory_usage()
p1 = profiler()
m2 = memory_usage()
mem_diff = m2[0] - m1[0]
print(f"Выполнение заняло {mem_diff} Mib")


class User_slots:
    __slots__ = ('login', 'password', 'is_active')
    def __init__(self, login, password, *, is_active):
        self.login = login
        self.password = password
        self.is_active = is_active


def profiler2():
    web_resource = WebResource()
    for u in range(10**4):
        u = User_slots(f'Ivanov{u}', f'{u}{u}', is_active=True)
        web_resource.users[u.login] = u
    return web_resource


m1 = memory_usage()
p2 = profiler2()
m2 = memory_usage()
mem_diff = m2[0] - m1[0]
print(f"Выполнение заняло {mem_diff} Mib")
