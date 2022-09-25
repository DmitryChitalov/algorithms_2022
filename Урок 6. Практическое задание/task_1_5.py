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

# 1. Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и
# возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

# Примечание: подумайте о возможных ошибках в адресе и
# постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

from memory_profiler import profile
from requests import get
import re
from json import loads, dumps

@profile
def email_parse(email):
    task = {}
    pattern = '[a-zA-Z0-9_.]+@[a-zA-Z0-9.]+\.[a-zA-z]'
    if re.search(pattern, email):
        task['Username'], task['Domain'] = re.split('@', email)[0], re.split('@', email)[1]
        try:
            if get('https://' + task['Domain']).ok or get('http://' + task['Domain']).ok:
                return task
        except:
            raise ValueError(f'Wrong email: {email}, Domain {task["Domain"]} does not exist')
    else:
        raise ValueError(f'Wrong email: {email}')

# print(email_parse(input('Введите email: ')))

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    57     25.9 MiB     25.9 MiB           1   @profile
    58                                         def email_parse(email):
    59     25.9 MiB      0.0 MiB           1       task = {}
    60     25.9 MiB      0.0 MiB           1       pattern = '[a-zA-Z0-9_.]+@[a-zA-Z0-9.]+\.[a-zA-z]'
    61     25.9 MiB      0.0 MiB           1       if re.search(pattern, email):
    62     25.9 MiB      0.0 MiB           1           task['Username'], task['Domain'] = re.split('@', email)[0], re.split('@', email)[1]
    63     25.9 MiB      0.0 MiB           1           try:
    64     30.1 MiB      4.2 MiB           1               if requests.get('https://' + task['Domain']).ok or requests.get('http://' + task['Domain']).ok:
    65                                                         # print(task)
    66     30.1 MiB      0.0 MiB           1                   return task
    67                                                 except:
    68                                                     raise ValueError(f'Wrong email: {email}, Domain {task["Domain"]} does not exist')
    69                                             else:
    70                                                 raise ValueError(f'Wrong email: {email}')
'''
@profile
def email_parse_opt(email):
    pattern = r'(?P<login>[a-zA-Z0-9_.]+)@(?P<domain>[a-zA-Z0-9.]+\.[a-zA-Z]+)'
    res = re.search(pattern, email).groupdict()
    if res:
        return dumps(res)
    else:
        raise ValueError(f'Wrong email address: {email}')

print(loads(email_parse_opt('me@google.com++')))

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    91     25.7 MiB     25.7 MiB           1   @profile
    92                                         def email_parse_opt(email):
    93     25.7 MiB      0.0 MiB           1       pattern = r'(?P<login>[a-zA-Z0-9_.]+)@(?P<domain>[a-zA-Z0-9.]+\.[a-zA-Z]+\b)'
    94     25.7 MiB      0.0 MiB           1       res = re.search(pattern, email).groupdict()
    95     25.7 MiB      0.0 MiB           1       if res:
    96     25.7 MiB      0.0 MiB           1           return filter(lambda k: k, res)
    97                                             else:
    98                                                 raise ValueError(f'Wrong email address: {email}')
'''

# расход памяти снизился почти на 20%
# за счёт сериализации и урезки лишнего функционала, не обозначенного в ТЗ.
