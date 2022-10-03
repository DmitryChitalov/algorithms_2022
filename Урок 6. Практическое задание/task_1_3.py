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
"""

# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере,
# посмотреть содержимое ответа. Можно ли, используя только методы класса str,
# решить поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро

from memory_profiler import profile
from requests import get
import xmltodict
from recordclass import recordclass
from timeit import timeit


# @profile
# def currency_rates(currency='USD'):
#     """ функция поиска курса валюты, указанной пользоватлем
#         :: принимает значение формата CAD, EUR, USD, usd, cad, eur;
#         :: или Канадский доллар, ЕВРО, евро, фунт и т.п.;
#         :: или азербайджан, сша, китай, узбек, казах и всякое такое
#     """
#     raw_data = get('http://www.cbr.ru/scripts/XML_daily.asp').text
#     raw_data = raw_data[103:].split('</Valute>')
#
#     for i in raw_data:
#         if len(currency) == 3:
#             currency = currency.upper()
#         elif currency == 'доллар США' or currency == 'доллар сша' or currency == 'Доллар сша':
#             currency = 'Доллар США'
#         else:
#             currency = currency.capitalize()
#         if currency in i:
#             exchange = (i[-15:-10]).split(',')
#             exchange = float(exchange[0] + '.' + exchange[1])
#             return exchange
#
#
# print(currency_rates())

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    53     27.0 MiB     27.0 MiB           1   @profile
    54                                         def currency_rates(currency):
    55                                             """ функция поиска курса валюты, указанной пользоватлем
    56                                                 :: принимает значение формата CAD, EUR, USD, usd, cad, eur;
    57                                                 :: или Канадский доллар, ЕВРО, евро, фунт и т.п.;
    58                                                 :: или азербайджан, сша, китай, узбек, казах и всякое такое
    59                                             """
    60     28.7 MiB      1.7 MiB           1       raw_data = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    61     28.8 MiB      0.0 MiB           1       raw_data = raw_data[103:].split('</Valute>')
    62                                         
    63     28.8 MiB      0.0 MiB           1       if len(currency) == 3:  # гипотеза: пользователь ввёл код валюты
    64     28.8 MiB      0.0 MiB           1           currency = currency.upper()
    65                                             elif currency == 'доллар США' or currency == 'доллар сша' or currency == 'Доллар сша':
    66                                                 currency = 'Доллар США'
    67                                             else:
    68                                                 currency = currency.capitalize()  # гипотеза: пользователь ввёл полное название валюты
    69     28.8 MiB      0.0 MiB          11       for i in raw_data:
    70     28.8 MiB      0.0 MiB          11           if currency in i:
    71     28.8 MiB      0.0 MiB           1               exchange = (i[-15:-10]).split(',')
    72     28.8 MiB      0.0 MiB           1               exchange = float(exchange[0] + '.' + exchange[1])
    73     28.8 MiB      0.0 MiB           1               return exchange
'''


@profile
def currency_rates_opt(currency):
    currency = currency.upper()
    rc = recordclass('exchange_rate', (
        'charcode', 'value', 'nominal'
    ))
    raw_data = get('http://www.cbr.ru/scripts/XML_daily.asp')
    dicted = xmltodict.parse(raw_data.content)['ValCurs']['Valute']
    return [rc(charcode=i['CharCode'],
               value=i['Value'][:5],
               nominal=i['Nominal']) for i in dicted if i['CharCode'] == currency][0]


print(currency_rates_opt('USD'))

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   105     26.8 MiB     26.8 MiB           1   @profile
   106                                         def currency_rates_opt(currency):
   107     26.8 MiB      0.0 MiB           1       currency = currency.upper()
   108     26.8 MiB      0.0 MiB           1       rc = recordclass('exchange_rate', (
   109                                                 'charcode', 'value', 'nominal'
   110                                             ))
   111     28.3 MiB      1.5 MiB           1       raw_data = get('http://www.cbr.ru/scripts/XML_daily.asp')
   112     28.4 MiB      0.1 MiB           1       dicted = xmltodict.parse(raw_data.content)['ValCurs']['Valute']
   113     28.4 MiB      0.0 MiB          41       return [rc(charcode=i['CharCode'],  value=i['Value'][:5],
   114     28.4 MiB      0.0 MiB          37                     nominal=i['Nominal']) for i in dicted if i['CharCode'] == currency][0]
'''

'''
не уверен, что изменения можно назвать ощутимой оптимизацией, но сделал, что смог.
использовал библиотеки recordclass и xmltodict.
и хоть такой задачи не стояло, но код стал значительно удобнее.
и теперь есть номинал))
'''
