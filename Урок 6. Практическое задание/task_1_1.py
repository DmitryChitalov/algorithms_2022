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

# LESSON 6, TASK 1.
# Не используя библиотеки для парсинга, распарсить
# (получить определённые данные) файл логов web-сервера nginx_logs.txt
#
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

from requests import get, utils
from memory_profiler import profile
import re
from recordclass import recordclass


@profile
def unparse(user_link):
    link = get(user_link)
    encodings = utils.get_encoding_from_headers(link.headers)
    raw_content = link.content.decode(encoding=encodings).split(')"')

    tmp_ = []
    for i, val in enumerate(raw_content):
        tmp_.append((val.replace('"', '').split(' ')))

    return [(tmp_[i][0].replace('\n', ''), tmp_[i][5], tmp_[i][6]) for i, _ in enumerate(tmp_) if len(_) >= 7]


u_link = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
# res = (unparse(u_link))
# for i in res:
#     print(i)
#     break

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    56     26.1 MiB     26.1 MiB           1   @profile
    57                                         def unparse(user_link):
    58     44.7 MiB     18.6 MiB           1       link = get(user_link)
    59     44.7 MiB      0.0 MiB           1       encodings = utils.get_encoding_from_headers(link.headers)
    60     60.8 MiB     16.2 MiB           1       raw_content = link.content.decode(encoding=encodings).split(')"')
    61                                         
    62     60.8 MiB      0.0 MiB           1       tmp_ = []
    63    108.1 MiB      0.0 MiB       48874       for i, val in enumerate(raw_content):
    64    108.1 MiB     47.2 MiB       48873           tmp_.append((val.replace('"', '').split(' ')))
    65                                         
    66    114.6 MiB      6.5 MiB       48876       return [(tmp_[i][0].replace('\n', ''), tmp_[i][5], tmp_[i][6]) for i, _ in enumerate(tmp_) if len(_) >= 7]
"""


@profile
def unparse_opt(user_link):
    link = get(user_link)
    encodings = utils.get_encoding_from_headers(link.headers)
    raw_content = link.content.decode(encoding=encodings)
    rc = recordclass('parsed', ('ip', 'req', 'source'))
    grab = re.findall(r'(?i)(?P<ip>[0-9.]{8,15}).*(?P<req>GET|POST).'
                      r'(?P<source>\/[a-z\/_0-9]+)', raw_content)
    return (rc(ip=i, req=r, source=s) for i, r, s in grab)


res = unparse_opt(u_link)
print(res)
for i in res:
    print(i)
    break

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    93     26.4 MiB     26.4 MiB           1   @profile
    94                                         def unparse_opt(user_link):
    95     45.0 MiB     18.6 MiB           1       link = get(user_link)
    96     45.0 MiB      0.0 MiB           1       encodings = utils.get_encoding_from_headers(link.headers)
    97     51.7 MiB      6.7 MiB           1       raw_content = link.content.decode(encoding=encodings)
    98     51.7 MiB      0.0 MiB           1       rc = recordclass('parsed', ('ip', 'req', 'source'))
    99     65.6 MiB     13.9 MiB           1       _ = re.findall(r'(?P<ip>[0-9.]{8,15}).*(?P<req>GET|POST).(?P<source>\/[a-z\/_0-9]+)', raw_content)
   100     65.6 MiB      0.0 MiB           1       return (rc(ip=i, req=r, source=s) for i, r, s in _)
"""

# за счёт перехода на regex и recordclass получилось
# значительно улучшить показатели, отображаемые в профайлинге

