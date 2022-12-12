"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

from task_2 import password_hash_sha as hash_gen
from random import randint
import os.path
import sqlite3
import shutil


def check_web_cache(cache: dict):
    """
    Функция запрашивает URL. Вычисляет хэш URL по алгоритму sha512. Ищет хэш в кэше.
    Если находит, выводит хэш. Если нет, добавляет в кэш.
    После каждого обращения к кэшу функция запрашивает пользователя о продолжении работы.
    """
    try:
        print('Пожалуйста, введите URL-адрес страницы: ', end='')
        url = input()
        url_hash = hash_gen(url, salt='qwerty', algorithm='sha512')
        if cache.get(url_hash) is None:
            cache.setdefault(url_hash, url)
            print(f'В кэш добавлена запись:\n{url_hash}: {url}')
        else:
            print(f'В кэше есть данный URL-адрес. Хэш URL:\n{url_hash}')
        print('Хотите продолжить? (1 - да, 0 - закончить работу)')
        to_continue = int(input())
        if to_continue:
            check_web_cache(cache)
        else:
            return
    except ValueError:
        return


def copy_history_db():
    """
    Функция копирует историю Google Chrome в папку <User>\Documents
    Возвращает адрес файла-копии в строковом формате.
    Работает только для Windows.
    """
    history_path_original = ''.join((os.path.expanduser('~'),
                                    '\AppData\Local\Google\Chrome\/User Data/\Default'))
    history_db_original = os.path.join(history_path_original, 'History')
    history_path_copy = ''.join((os.path.expanduser('~'), '\Documents'))
    history_db_copy = os.path.join(history_path_copy, 'History')
    shutil.copy(history_db_original, history_db_copy)
    return history_db_copy


def create_web_cache(history_db: str):
    """
    Функция парсит БД истории Google Chrome и добавляет URL-адреса вида http:// и https://
    в словарь в качестве значений, а в качестве ключей добавляет хэши URL-адресов.
    Возвращает словарь-кэш.
    Также выводит подсказку для пользователя о том, какие страницы он посещал.
    """
    connection = sqlite3.connect(history_db)
    pointer = connection.cursor()
    select_statement = 'SELECT urls.url FROM urls;'
    pointer.execute(select_statement)
    web_cache_raw = pointer.fetchall()
    web_cache_aux = list()
    web_cache = dict()
    for i in range(0, len(web_cache_raw)):
        current_rec = web_cache_raw[i][0]
        is_url = (current_rec[0:8] == 'https://') or (current_rec[0:7] == 'http://')
        if is_url:
            web_cache[hash_gen(current_rec, salt='qwerty', algorithm='sha512')] = current_rec
            # web_cache[current_rec] = hash_gen(current_rec, salt='qwerty', algorithm='sha512')
            web_cache_aux.append(current_rec)
    print('Подсказка. Вы посещали страницы:')
    for i in range(0, 5):
        print(f'{i + 1}: {web_cache_aux[randint(0, len(web_cache_aux))]}')
    return web_cache


user_history_db = copy_history_db()
user_web_cache = create_web_cache(user_history_db)
check_web_cache(user_web_cache)

