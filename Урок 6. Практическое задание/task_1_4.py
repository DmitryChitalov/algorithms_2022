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
'''курс основы Python урок 8 задание 1
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает
их в виде словаря. Если адрес не валиден, выбросить исключение ValueError'''
from random import choice
from collections import deque
from memory_profiler import memory_usage
import re

def get_emails(quantity):
    digits = [2,3,4,5,6,7]
    chrs = list('abcdefghlmnoprstufhjk')
    names = []
    for _ in range(quantity):
        size = choice(digits)
        name = ''
        for _ in range(size):
            ch = choice(chrs)
            name += ch
        names.append(f'{name}@geekbrains.ru')
    return names

def decor(func):
    def wrapper(arg):
        m1 = memory_usage()
        res = func(arg)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper

# 1) До оптимизации

@decor
def email_parse1(li_email):
    di = {}
    for email in li_email:
        if '@' not in email:
            raise ValueError('email don`t have - @')
        elif '.' not in email:
            raise ValueError('email don`t have - .')
        all = re.findall(r'[a-zA-Z1-9]*', email)
        di[all[0]] = all[2]

    # print(di)

# 2) После оптимизации

@decor
def email_parse2(li_email):
    # user_domain = namedtuple('user_domain', ('username', 'domain'))
    users = [] # deque()
    for email in li_email:
        if '@' not in email:
            raise ValueError('email don`t have - @')
        elif '.' not in email:
            raise ValueError('email don`t have - .')
        all = re.findall(r'[a-zA-Z1-9]*', email)
        
        users.append(all[0])

    # print(users)

emails = get_emails(20000)
# print(emails)
res1, mem1 = email_parse1(emails)
res2, mem2 = email_parse2(emails)
print(mem1, mem2)  # 0.46484375 0.03515625
'''В результате оптимизации словарь был заменен на список
в результате чего использование памяти было уменьшено более чем в 10 раз
deque показал сходные со списком значения 0.453125 0.03515625
'''