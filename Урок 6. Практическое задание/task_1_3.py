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

Это файл для третьего скрипта

# Техническое задание:
#
# Лог файл: https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# Функция парсинга строки лог-файла:
# Принимает параметр: строка для пасинга, при необходимости и другие параметры
# возвращает кортеж из 6 элементов вида: ('<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)'
# Вы можете не обращать внимание на IPv6 или явно учесть их в регулярном выражении, это будет очень хорошо.
# Проверьте работоспособность функции на нескольких строках лог файла.
# Распарсите весь файл и сформируйте список всех IP лог файла, без повторений. Выведите в консоль его длину.
# Примеры/Тесты:
#
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
#
# Усложнение:
#
# Ваша функция должна корректно обрабатывать как IPv4, так и IPv6 - найдите их в лог-файле.
# Посмотрите спецификацию IPv6. Что такое шестнадцатеричное число и какие буквы/цифры оно может включать. Сколько их может быть в IPv6.
# Совсем хорошо, если вы обработаете cокращенные адреса IPv6, которые тоже в есть в лог файле.
# Ваш шаблон должен пропускать только то, что нужно, не используйте «избыточно широкие» шаблоны.

Аналитика:
вариант ip_list() выводит список IP адресов в формате list
Использует память:
    87     35.6 MiB      3.3 MiB           1       with urllib.request.urlopen(url_addr) as content:
    90     36.0 MiB      0.1 MiB       25731               line_content = str(content.readline().decode('utf-8'))
    93     36.0 MiB      0.2 MiB       25731                   parse_res = RE_PATERN.search(line_content)

вариант ip_array(): выводит список IP адресов в формате numpy.array
Использует память:
   117     36.1 MiB      0.1 MiB           1       with urllib.request.urlopen(url_addr) as content:
   136     38.3 MiB      0.2 MiB       25731               if ip_address not in list(ip_array):
   137     38.3 MiB      1.9 MiB        2113                   ip_array = numpy.append(ip_array, [ip_address])

В варианте с ip_array() памяти требуется меньше
"""
import re
import urllib.request
from memory_profiler import profile
from memory_profiler import memory_usage
import numpy



RE_PATERN = re.compile(r"""
    (^|\A|\s)
    (?P<rem_addr>((\d{1,3})(\.\d{1,3}){3})|
    (([0-9]|[a-f]){,4})(:([0-9]|[a-f]){,4}){6,7})
    \s-\s-\s
    (?P<request_datetime>\[\d{2}\/[A-Z][a-z]{2}\/\d{4}(:\d{2}){3}\s\+0000\])\s\"
    (?P<request_type>[A-Z]+)\s
    (?P<requested_resource>/downloads/product_\d\sHTTP/1.1)\"\s
    (?P<response_code>\d+)\s
    (?P<response_size>\d+)
""", re.VERBOSE)

#string = input('Please enter string from mail : ')

url_addr = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"

# response = urllib.request.get(url_addr)
# print(response)
#print(type(response)) # <class 'requests.models.Response'>
#print(dir(response))


@profile
def ip_list():
    ip_list = []
    with urllib.request.urlopen(url_addr) as content:
        #print(f'url opened')
        for _ in content:
            line_content = str(content.readline().decode('utf-8'))
            # print("\n",line_content)
            try:
                parse_res = RE_PATERN.search(line_content)
                result = parse_res.groupdict()
            except AttributeError as e:
                result = e
            finally:
                pass
                # print(f"ГРУППЫ словарем: {result} ")
            ip_address=result['rem_addr']
            #print(result)
            #print(type(result))
            # print (f'ip_address = ',ip_address)

            #print  ('ip_address= ', ip_address)
            if ip_address not in ip_list :
                ip_list.append(ip_address)
                # print (f'IP added {ip_address}')
    # print(ip_list)
    # print(f'\n\nLength of IP list, including IPv6  is : {len(ip_list)}')
    return ip_list


@profile
def ip_array():
    ip_array = numpy.array([])
    with urllib.request.urlopen(url_addr) as content:
        #print(f'url opened')
        for _ in content:
            line_content = str(content.readline().decode('utf-8'))
            # print("\n",line_content)
            try:
                parse_res = RE_PATERN.search(line_content)
                result = parse_res.groupdict()
            except AttributeError as e:
                result = e
            finally:
                pass
                # print(f"ГРУППЫ словарем: {result} ")
            ip_address=result['rem_addr']
            #print(result)
            #print(type(result))
            # print (f'ip_address = ',ip_address)

            #print  ('ip_address= ', ip_address)
            if ip_address not in list(ip_array):
                ip_array = numpy.append(ip_array, [ip_address])
                # print (f'IP added {ip_address}')
    # print(ip_list)
    # print(f'\n\nLength of IP list, including IPv6  is : {len(ip_list)}')
    return ip_array

res1 = ip_list()
print(type(res1))
print(res1[1:20])


res2 = ip_array()
print(type(res2))
print(res2[1:20])

# Script listing:
#
#
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     84     32.3 MiB     32.3 MiB           1   @profile
#     85                                         def ip_list():
#     86     32.3 MiB      0.0 MiB           1       ip_list = []
#     87     35.6 MiB      3.3 MiB           1       with urllib.request.urlopen(url_addr) as content:
#     88                                                 #print(f'url opened')
#     89     36.0 MiB      0.0 MiB       25732           for _ in content:
#     90     36.0 MiB      0.1 MiB       25731               line_content = str(content.readline().decode('utf-8'))
#     91                                                     # print("\n",line_content)
#     92     36.0 MiB      0.0 MiB       25731               try:
#     93     36.0 MiB      0.2 MiB       25731                   parse_res = RE_PATERN.search(line_content)
#     94     36.0 MiB      0.0 MiB       25731                   result = parse_res.groupdict()
#     95                                                     except AttributeError as e:
#     96                                                         result = e
#     97                                                     finally:
#     98     36.0 MiB      0.0 MiB       25731                   pass
#     99                                                         # print(f"ГРУППЫ словарем: {result} ")
#    100     36.0 MiB      0.0 MiB       25731               ip_address=result['rem_addr']
#    101                                                     #print(result)
#    102                                                     #print(type(result))
#    103                                                     # print (f'ip_address = ',ip_address)
#    104
#    105                                                     #print  ('ip_address= ', ip_address)
#    106     36.0 MiB      0.0 MiB       25731               if ip_address not in ip_list :
#    107     36.0 MiB      0.0 MiB        2113                   ip_list.append(ip_address)
#    108                                                         # print (f'IP added {ip_address}')
#    109                                             # print(ip_list)
#    110                                             # print(f'\n\nLength of IP list, including IPv6  is : {len(ip_list)}')
#    111     36.0 MiB      0.0 MiB           1       return ip_list
#
#
# <class 'list'>
# ['93.180.71.3', '217.168.17.5', '188.138.60.101', '46.4.66.76', '91.234.194.89', '37.26.93.214', ....
# Filename: C:\Users\VMAL\GB\Courses\14_Algorithms\Algorithm_Lesson6_HW\task_1_3.py
#
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#    114     36.0 MiB     36.0 MiB           1   @profile
#    115                                         def ip_array():
#    116     36.0 MiB      0.0 MiB           1       ip_array = numpy.array([])
#    117     36.1 MiB      0.1 MiB           1       with urllib.request.urlopen(url_addr) as content:
#    118                                                 #print(f'url opened')
#    119     38.3 MiB     -0.2 MiB       25732           for _ in content:
#    120     38.3 MiB     -0.2 MiB       25731               line_content = str(content.readline().decode('utf-8'))
#    121                                                     # print("\n",line_content)
#    122     38.3 MiB     -0.2 MiB       25731               try:
#    123     38.3 MiB     -0.1 MiB       25731                   parse_res = RE_PATERN.search(line_content)
#    124     38.3 MiB     -0.2 MiB       25731                   result = parse_res.groupdict()
#    125                                                     except AttributeError as e:
#    126                                                         result = e
#    127                                                     finally:
#    128     38.3 MiB     -0.2 MiB       25731                   pass
#    129                                                         # print(f"ГРУППЫ словарем: {result} ")
#    130     38.3 MiB     -0.2 MiB       25731               ip_address=result['rem_addr']
#    131                                                     #print(result)
#    132                                                     #print(type(result))
#    133                                                     # print (f'ip_address = ',ip_address)
#    134
#    135                                                     #print  ('ip_address= ', ip_address)
#    136     38.3 MiB      0.2 MiB       25731               if ip_address not in list(ip_array):
#    137     38.3 MiB      1.9 MiB        2113                   ip_array = numpy.append(ip_array, [ip_address])
#    138                                                         # print (f'IP added {ip_address}')
#    139                                             # print(ip_list)
#    140                                             # print(f'\n\nLength of IP list, including IPv6  is : {len(ip_list)}')
#    141     38.3 MiB      0.0 MiB           1       return ip_array
#
#
# <class 'numpy.ndarray'>
# ['93.180.71.3' '217.168.17.5' '188.138.60.101' ... '88.198.106.237'
#  '195.1.24.132' '141.138.90.60']
