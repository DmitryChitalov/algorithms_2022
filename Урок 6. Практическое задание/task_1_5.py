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

from memory_profiler import memory_usage
from json import dumps, loads


def decor(func):
    def wrapper(args):
        m1 = memory_usage()
        res = func(args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# Исходное решение - задание 3_4 из курса 'Основы языка Python'
@decor
def thesaurus(workers):
    dict_of_workers = {}
    for worker in workers:
        surname, name = worker.split(' ')
        b = surname[0]
        surname_workers = list(filter(lambda el: el.startswith(b), workers))
        for x in range(len(surname_workers)):
            name_surname = ' '.join(list(reversed(surname_workers[x].split(' '))))
            surname_workers[x] = name_surname
        surname_workers.sort()
        some_workers = {}
        for member in surname_workers:
            member_name, member_surname = member.split(' ')
            c = member_name[0]
            name_workers = list(filter(lambda el: el.startswith(c), surname_workers))
            some_workers.setdefault(c, name_workers)
        dict_of_workers.setdefault(b, some_workers)
    return dict_of_workers


# Оптимизированное решение
@decor
def thesaurus2(workers):
    dict_of_workers = {}
    for worker in workers:
        surname, name = worker.split(' ')
        b = surname[0]
        surname_workers = list(filter(lambda el: el.startswith(b), workers))
        for x in range(len(surname_workers)):
            name_surname = ' '.join(list(reversed(surname_workers[x].split(' '))))
            surname_workers[x] = name_surname
        surname_workers.sort()
        some_workers = {}
        for member in surname_workers:
            member_name, member_surname = member.split(' ')
            c = member_name[0]
            name_workers = list(filter(lambda el: el.startswith(c), surname_workers))
            some_workers.setdefault(c, name_workers)
        dict_of_workers.setdefault(b, some_workers)
    dumped_dict = dumps(dict_of_workers)
    return dumped_dict


if __name__ == '__main__':
    your_workers = input('Введите имя и фамилию сотрудников через запятую: ')
    workers = your_workers.split(', ')
    for x in range(len(workers)):
        surname_name = ' '.join(list(reversed(workers[x].split(' '))))
        workers[x] = surname_name
    workers.sort()
    print('Исходное решение')
    res1, mem_dif = thesaurus(workers)
    print(res1)
    print(f'Выполнение исходного решения заняло {mem_dif} Mib')  # 0.01171875 Mib
    print('\nОптимизированное решение')
    res2, mem_dif = thesaurus2(workers)
    print(loads(res2))
    print(f'Выполнение оптимизированного решения заняло {mem_dif} Mib')  # 0.00390625 Mib

'''В оптимизированном решении была использована сериализация словаря в формат json-строк'''
