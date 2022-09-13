"""
КУРС: "Основы языка Python". Урок 4: "Работа с модулями и пакетами". Задание 2.
Написать функцию `currency_rates()`, принимающую в качестве аргумента код валюты
(например, USD, EUR, SGD, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку `requests`.
В качестве API можно использовать `http://www.cbr.ru/scripts/XML_daily.asp`.
* Можно ли, используя только методы класса `str`, решить поставленную задачу?
* Функция должна возвращать результат числового типа, например `float`...
"""

import requests
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


# https://github.com/AzarnykhOleg/Python-Basics/pull/5
@decor
def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_dict = {}
    currency_list = response.text.split('ID=')
    del currency_list[0]
    for element in currency_list:
        exchange_rate = element[(element.find('<Value>') + 7):element.find('</Value>')]
        exchange_rate = float(exchange_rate.replace(',', '.'))
        amendment = int(element[(element.find('<Nominal>') + 9):element.find('</Nominal>')])
        currency_dict[(element[(element.find('<CharCode>') + 10):
                               element.find('</CharCode>')])] = exchange_rate / amendment
        result_value = currency_dict.get(code.upper(), None)
    return result_value


# Обновлённый вариант
@decor
def currency_rates_adv(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_list = response.text.split('ID=')
    del currency_list[0]
    for element in currency_list:
        if element[(element.find('<CharCode>') + 10):element.find('</CharCode>')] == code:
            exchange_rate = element[(element.find('<Value>') + 7):element.find('</Value>')]
            exchange_rate = float(exchange_rate.replace(',', '.'))
            amendment = int(element[(element.find('<Nominal>') + 9):element.find('</Nominal>')])
    return exchange_rate / amendment


res, mem_diff = currency_rates("USD")
print(res)
print(f"Выполнение заняло {mem_diff} Mib")  # -> Выполнение заняло 0.6796875 Mib
print('----------------- Новый вариант -----------------')
res, mem_diff = currency_rates_adv("USD")
print(res)
print(f"Выполнение заняло {mem_diff} Mib")  # -> Выполнение заняло 0.0 Mib

"""
Отказ от создания словаря для хранения данных позволил сэкономить 0.6796875 Mib.
"""
