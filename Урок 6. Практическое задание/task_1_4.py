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

# LESSON 6, TASK 2.
# * Найти IP адрес спамера и количество отправленных
# им запросов по данным файла логов из предыдущего задания.
#
# Примечания: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

from requests import get, utils
from memory_profiler import profile
from recordclass import recordclass
import re
from collections import Counter

@profile
def catch_spammer(link):
    link = get(link)
    encodings = utils.get_encoding_from_headers(link.headers)
    raw_content = link.content.decode(encoding=encodings).split(')"')

    tmp_, ips, max_, spamer = [], [], 0, ''

    for i, val in enumerate(raw_content):
        tmp_.append((val.replace('"', '').split(' ')))

    ips = [(tmp_[i][0].replace('\n', '')) for i, _ in enumerate(tmp_)]

    for val in ips:
        if ips.count(val) > max_:
            max_, spamer = ips.count(val), val

    return spamer, max_

ref = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
# s, m = catch_spammer(ref)
# print(f'Спамер: {s}, вот столько запросов он отправил: {m}')

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    43     26.2 MiB     26.2 MiB           1   @profile
    44                                         def catch_spammer(link):
    45     44.4 MiB     18.2 MiB           1       link = get(link)
    46     44.4 MiB      0.0 MiB           1       encodings = utils.get_encoding_from_headers(link.headers)
    47     60.4 MiB     16.0 MiB           1       raw_content = link.content.decode(encoding=encodings).split(')"')
    48                                         
    49     60.4 MiB      0.0 MiB           1       tmp_, ips, max_, spamer = [], [], 0, ''
    50                                         
    51    107.5 MiB      0.0 MiB       48874       for i, val in enumerate(raw_content):
    52    107.5 MiB     47.1 MiB       48873           tmp_.append((val.replace('"', '').split(' ')))
    53                                         
    54    110.6 MiB      3.1 MiB       48876       ips = [(tmp_[i][0].replace('\n', '')) for i, _ in enumerate(tmp_)]
    55                                         
    56    110.6 MiB   -724.6 MiB       48874       for val in ips:
    57    110.6 MiB   -724.6 MiB       48873           if ips.count(val) > max_:
    58    110.6 MiB      0.0 MiB           4               max_, spamer = ips.count(val), val
    59                                         
    60    110.6 MiB     -0.0 MiB           1       return spamer, max_
'''


@profile
def catch_the_spamer_opt(user_link):
    link = get(user_link)
    encodings = utils.get_encoding_from_headers(link.headers)
    raw_content = link.content.decode(encoding=encodings)
    rc = recordclass('catched', ('ip', 'count_ip'))
    data = re.findall(r'(?i)(?P<ip>[0-9.]{8,15})', raw_content)
    _ = max(set(data), key=data.count)
    spamer = rc(ip=_,
                count_ip=data.count(_)
                )
    return spamer

s = catch_the_spamer_opt(ref)
print(f'IP адрес спамера: {s.ip}.\n'
      f'С него поступило {s.count_ip} запросов к серверу.')

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   102     26.9 MiB     26.9 MiB           1   @profile
   103                                         def catch_the_spamer_opt(user_link):
   104     45.3 MiB     18.5 MiB           1       link = get(user_link)
   105     45.3 MiB      0.0 MiB           1       encodings = utils.get_encoding_from_headers(link.headers)
   106     52.0 MiB      6.7 MiB           1       raw_content = link.content.decode(encoding=encodings)
   107     52.0 MiB      0.0 MiB           1       rc = recordclass('catched', ('ip', 'count_ip'))
   108     55.4 MiB      3.4 MiB           1       data = re.findall(r'(?i)(?P<ip>[0-9.]{8,15})', raw_content)
   109     55.4 MiB      0.0 MiB           1       _ = max(set(data), key=data.count)
   110     55.4 MiB      0.0 MiB           2       spamer = rc(ip=_,
   111     55.4 MiB      0.0 MiB           1                   count_ip=data.count(_)
   112                                                         )
   113     55.4 MiB      0.0 MiB           1       return spamer
'''

# удалось улучшить показатели профайлинга почти в два раза,
# за счёт перехода на менее упоротый код, regex и recordclass