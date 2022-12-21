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

from memory_profiler import profile, memory_usage
from itertools import zip_longest
from pympler.asizeof import asizeof


def memory(func):
    def wrapper():
        start = memory_usage()
        my_func = func()
        stop = memory_usage()
        result = stop[0] - start[0]
        return my_func, print(result)

    return wrapper()


@memory
def appendhobby():
    with open('Users.csv', encoding='utf-8') as f_users:
        users = []
        for line in f_users:
            users.append(line.strip().replace('"', ''))
    with open('Hobby.csv', encoding='utf-8') as f_hobby:
        hobby = []
        for line in f_hobby:
            hobby.append(line.strip().replace('"', ''))

    if len(users) > len(hobby):
        exit(1)

    else:
        dict_zip = ((users, hobby) for users, hobby in zip_longest(users, hobby, fillvalue=None))
        print(dict(dict_zip))


# appendhobby()
# print(asizeof(appendhobby()))

@memory
def appendhobby_nitro():
    with open('Users.csv', encoding='utf-8') as f_users:
        users = [line.strip().replace('"', '') for line in f_users]
    with open('Hobby.csv', encoding='utf-8') as f_hobby:
        hobby = [line.strip().replace('"', '') for line in f_hobby]
    if len(users) > len(hobby):
        exit(1)

    else:
        dict_zip = ((users, hobby) for users, hobby in zip_longest(users, hobby, fillvalue=None))
        print(dict(dict_zip))


# print(asizeof(appendhobby_nitro()))

'''Использовал LC, вместо цикла for, тем самым используется меньше памяти, 6 урок базовый курс Python'''

