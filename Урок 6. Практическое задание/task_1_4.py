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
"""
Основы Python урок 6.
2. *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
) для получения информации вида: (<remote_addr>, <request_datetime>,
<request_type>, <requested_resource>, <response_code>, <response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET
/downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
'/downloads/product_2', '304', '0')
© geekbrains.ru 15
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

"""

from memory_profiler import profile
import re
import requests


# В первом случае использовали парсинг файла находящегося на локальном носителе, для пролучения даннных пользователей
# с использованием регулярных выражений.
@profile
def get_par_url():
    pattern = r"(?P<addres>^\S+)[\s-]*\[(?P<datatime>.*)]\s*\"(?P<resp>\w*)\s*(?P<file>" \
              r"[/\w]+)[^\"]+\"\s+(?P<code>\d+)\s+(?P<size>\d+)"

    PARSE_RE = re.compile(pattern)

    with open("nginx_logs.txt", "r", encoding="utf-8") as file:
        print(*(tuple(x.groupdict().values())
                for line in file for x in PARSE_RE.finditer(line)), sep="\n")

    return


# Во втором случае парсили данные находящиеся на веб-ресурсе.
@profile
def get_par_url_1():
    PAD = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - '
                     r'(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}]) .(\w+) '
                     r'([/\w+]{0,}) (?:[^\"]*)\" ([0-9]+) ([0-9]+)')
    url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    content = requests.get(url).text
    for arg in PAD.findall(content):
        addr, datetime, r_type, resource, code, size = arg
        print(addr, datetime, r_type, resource, code, size)

    return


get_par_url()
get_par_url_1()

"""
В первом случае расход памяти меньше и она высвобождается после прочтения файла.
Во втором случае память занята на всем протяжении работы функции, её объём снижается на 50% когда она заканчивает
работать.
Вывод: первый метод эффективнее, но при удаленной работе придётся воспользоваться вторым!!! 

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    58     26.1 MiB     26.1 MiB           1   @profile
    59                                         def get_par_url():
    60                                         
    61     26.1 MiB      0.0 MiB           1       pattern = r"(?P<addres>^\S+)[\s-]*\[(?P<datatime>.*)]\s*\"
                                                                        (?P<resp>\w*)\s*(?P<file>" \
    62                                                       r"[/\w]+)[^\"]+\"\s+(?P<code>\d+)\s+(?P<size>\d+)"
    63                                         
    64     26.1 MiB      0.0 MiB           1       PARSE_RE = re.compile(pattern)
    65                                         
    66     30.3 MiB    -20.7 MiB           2       with open("nginx_logs.txt", "r", encoding="utf-8") as file:
    67     51.0 MiB      4.1 MiB      205853           print(*(tuple(x.groupdict().values())
    68     51.0 MiB      0.0 MiB       51464                   for line in file for x in PARSE_RE.finditer(line)), 
                                                                                                            sep="\n")
    69                                         
    70     30.3 MiB      0.0 MiB           1       return



Process finished with exit code 0

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    73     26.1 MiB     26.1 MiB           1   @profile
    74                                         def get_par_url_1():
    75                                         
    76     26.1 MiB      0.0 MiB           1       PAD = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - '
    77                                                              r'(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2}
                                                                        \+[0-9]{4}]) .(\w+) '
    78                                                              r'([/\w+]{0,}) (?:[^\"]*)\" ([0-9]+) ([0-9]+)')
    79     26.1 MiB      0.0 MiB           1       url = 'https://github.com/elastic/examples/raw/master/Common%20Data%
                                                                    20Formats/nginx_logs/nginx_logs'
    80     36.1 MiB     10.0 MiB           1       content = requests.get(url).text
    81     61.4 MiB      4.3 MiB       51413       for arg in PAD.findall(content):
    82     61.4 MiB      0.0 MiB       51412           addr, datetime, r_type, resource, code, size = arg
    83     61.4 MiB      0.0 MiB       51412           print(addr, datetime, r_type, resource, code, size)
    84                                         
    85     40.4 MiB    -21.0 MiB           1       return



Process finished with exit code 0

"""
